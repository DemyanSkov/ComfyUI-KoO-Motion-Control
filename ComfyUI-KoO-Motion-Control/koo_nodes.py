# Original KoO implementation; extracted without algorithm changes.
import os
import folder_paths
import nodes
from comfy_api.latest import io, ui, Types


class UltimateControls(io.ComfyNode):
    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id='KoOUltimateControls', display_name='KoO H3 Ultimate | Mode & Outputs', category='KoO/H3 Ultimate',
            inputs=[
                io.Combo.Input('generation_mode', options=['Role Swap', 'Fashion Video']),
                io.Combo.Input('fashion_task', options=['Image to Video', 'Reference to Video']),
                io.Combo.Input('face_refine', options=['No Face Refine', 'T8 Face Refine', 'Adaptive Face Refine']),
                io.Boolean.Input('dlss_enabled', default=False),
                io.Boolean.Input('save_comparison', default=False),
                io.Boolean.Input('save_debug', default=False),
            ],
            outputs=[io.Boolean.Output(n) for n in ['fashion', 'reference_task', 't8', 'adaptive', 'refine', 'dlss', 'comparison', 'debug_role', 'debug_t8', 'debug_adaptive']],
        )

    @classmethod
    def execute(cls, generation_mode, fashion_task, face_refine, dlss_enabled, save_comparison, save_debug):
        fashion = generation_mode == 'Fashion Video'
        t8 = face_refine == 'T8 Face Refine'
        adaptive = face_refine == 'Adaptive Face Refine'
        return io.NodeOutput(fashion, fashion_task == 'Reference to Video', t8, adaptive, t8 or adaptive,
                             dlss_enabled, save_comparison and (t8 or adaptive), save_debug and not fashion,
                             save_debug and t8, save_debug and adaptive)


class UltimateTiming(io.ComfyNode):
    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id='KoOUltimateTiming', display_name='KoO H3 Ultimate | Duration & Native FPS', category='KoO/H3 Ultimate',
            inputs=[io.Float.Input('duration_seconds', default=5.166666667, min=0.01, max=150.0, step=0.01),
                    io.Combo.Input('fps', options=['24 (H3 native)'])],
            outputs=[io.Int.Output('frame_count'), io.Float.Output('fps'), io.Float.Output('actual_duration')],
        )

    @classmethod
    def execute(cls, duration_seconds, fps):
        requested = max(5, round(duration_seconds * 24))
        count = requested + (5 - requested) % 17
        return io.NodeOutput(count, 24.0, count / 24.0)


class UltimateLoRA(io.ComfyNode):
    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id='KoOUltimateLoRA', display_name='KoO H3 Ultimate | Optional LoRA', category='KoO/H3 Ultimate',
            inputs=[io.Model.Input('model'), io.Boolean.Input('enabled', default=False),
                    io.String.Input('lora_name', default=''), io.Float.Input('strength', default=0.75, min=-4, max=4, step=0.05)],
            outputs=[io.Model.Output()],
        )

    @classmethod
    def execute(cls, model, enabled, lora_name, strength):
        if not enabled or strength == 0:
            return io.NodeOutput(model)
        folder_paths.get_full_path_or_raise('loras', lora_name)
        patched, = nodes.LoraLoaderModelOnly().load_lora_model_only(model, lora_name, strength)
        return io.NodeOutput(patched)


class UltimateExport(io.ComfyNode):
    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id='KoOUltimateExport', display_name='KoO H3 Ultimate | Conditional Video Output', category='KoO/H3 Ultimate',
            inputs=[io.Boolean.Input('enabled', default=True), io.Video.Input('video', lazy=True),
                    io.String.Input('filename_prefix', default='KoO_H3_Ultimate/Base'),
                    io.Float.Input('crf', default=18, min=0, max=51, step=1)],
            outputs=[io.String.Output('saved_path')], is_output_node=True,
            hidden=[io.Hidden.prompt, io.Hidden.extra_pnginfo],
        )

    @classmethod
    def check_lazy_status(cls, enabled, video=None, **kwargs):
        return ['video'] if enabled and video is None else []

    @classmethod
    def execute(cls, enabled, filename_prefix, crf, video=None):
        if not enabled:
            return io.NodeOutput('')
        width, height = video.get_dimensions()
        directory, filename, counter, subfolder, _ = folder_paths.get_save_image_path(
            filename_prefix, folder_paths.get_output_directory(), width, height)
        file = f'{filename}_{counter:05}_.mp4'
        path = os.path.join(directory, file)
        metadata = dict(cls.hidden.extra_pnginfo or {})
        if cls.hidden.prompt is not None:
            metadata['prompt'] = cls.hidden.prompt
        video.save_to(path, format=Types.VideoContainer('mp4'), codec=Types.VideoCodec('h264'), metadata=metadata, crf=crf)
        return io.NodeOutput(path, ui=ui.PreviewVideo([ui.SavedResult(file, subfolder, io.FolderType.output)]))


class UltimateSparse(io.ComfyNode):
    @classmethod
    def define_schema(cls):
        return io.Schema(node_id='KoOUltimateSparse', display_name='KoO H3 Ultimate | Optional Fashion Sparse Attention',
                         category='KoO/H3 Ultimate', inputs=[io.Model.Input('model'), io.Boolean.Input('enabled', default=False),
                         io.Float.Input('tau', default=1.3, min=0, max=4, step=0.05)], outputs=[io.Model.Output()],
                         description='Optional training-free Sol-Attn from the existing installation. Dense baseline when disabled. Never connect this patch to OpenVDN. The T2VA Veda predictor is not used for I2V or R2V.')

    @classmethod
    def execute(cls, model, enabled, tau):
        if not enabled:
            return io.NodeOutput(model)
        return nodes.NODE_CLASS_MAPPINGS['SolAttnMiniMax'].execute(
            model, selection={'selection': 'adaptive tau', 'tau': tau}, start_percent=0.2,
            end_percent=0.9, min_tokens=12288, sink_conditioning='exact_kv_and_rows', verbose=False)


class UltimateT8Stitch(io.ComfyNode):
    @classmethod
    def define_schema(cls):
        return io.Schema(node_id='KoOUltimateT8Stitch', display_name='KoO H3 Ultimate | T8 Stitch & Audit (Selected Only)',
            category='KoO/H3 Ultimate', inputs=[io.Image.Input('base_frames'), io.Image.Input('refined_crops'),
            io.Custom('H3_T8_FACE_REFINE_PLAN').Input('face_plan'),
            io.Combo.Input('paste_region', options=['ellipse','rectangle','full_crop_exp']),
            io.Float.Input('feather_source_px',default=12,min=.5,max=256),
            io.Float.Input('blend_strength',default=1,min=0,max=1),
            io.Float.Input('color_match_strength',default=.65,min=0,max=1),
            io.Float.Input('max_face_mean_abs_delta',default=.4,min=.01,max=1),
            io.Int.Input('fallback_neighbor_frames',default=1,min=0,max=12),
            io.Combo.Input('processing_device',options=['cpu_memory_safe','cuda_if_available'])],
            outputs=[io.Image.Output('candidate_frames'),io.Mask.Output('changed_mask'),io.Mask.Output('fallback_mask'),
                     io.Int.Output('fallback_count'),io.String.Output('report_json')],
            description='Calls the original T8 stitch and audit unchanged. This adapter is not an output node, so an unselected T8 branch does not execute.')

    @classmethod
    def execute(cls, **kwargs):
        return nodes.NODE_CLASS_MAPPINGS['MiniMaxH3FaceRefineStitchAuditT8Advanced'].execute(**kwargs)
