# Dependencies and complete node inventory

Inspected all 123 original nodes, 60 class identifiers, and 243 links. No nodes have mode 2/4; unselected branches are controlled by lazy switches. Identifiers and inputs for these branches still need registration.

## Install these external custom-node packages

| Package | Official installation source | Use |
|---|---|---|
| ComfyUI-KJNodes | [GitHub](https://github.com/kijai/ComfyUI-KJNodes) | PointsEditor and GetImageSizeAndCount |
| Comfyui-SecNodes | [GitHub](https://github.com/9nate-drake/Comfyui-SecNodes) | SeC loader/segmentation; retain full inference and model_config folders |
| ComfyUI-Video-Depth-Anything | [GitHub](https://github.com/yuvraj108c/ComfyUI-Video-Depth-Anything) | Depth model loader, processing, visualization |
| ComfyUI-VideoHelperSuite | [GitHub](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite) | VHS_LoadVideo and audio decoding |
| ComfyUI-H3-FaceRefine | [GitHub](https://github.com/Carasibana/ComfyUI-H3-FaceRefine) | Adaptive crop, denoise, stitch; full dependency frontend remains external |
| minimax-h3-audio-T8 | [GitHub](https://github.com/T8mars/comfyui-minimax-h3-audio-T8) | Six graph classes plus MiniMaxH3FaceRefineStitchAuditT8Advanced delegated by KoO; do not rename registered IDs |
| comfyui-SelfLift | [GitHub](https://github.com/facok/comfyui-SelfLift) | Registration for retained inactive Fashion branch |

Use a ComfyUI build supporting MiniMax H3, `CLIPLoader` type `minimax`, NVFP4/AWQ, INT8 convrot, native lazy switches and the current `comfy_api.latest` API. Validation host: ComfyUI 0.45.0, frontend 1.58.5, Python 3.13.12, PyTorch 2.11.0+cu130. Compatibility with older builds is not asserted.

`UltimateSparse` additionally delegates `SolAttnMiniMax` when enabled; this is supplied by T8. It stays disabled. No DLSS, Fashion or SelfLift branch has been enabled.

## Local provenance and changes

KoO originals: KoOUltimateControls, KoOUltimateTiming, KoOUltimateLoRA, KoOUltimateExport, KoOUltimateSparse, KoOUltimateT8Stitch. The last delegates the original T8 stitch class via `nodes.NODE_CLASS_MAPPINGS`, not a copied substitute.

The local H3InjectVideoLatent has an extra pre-VAE spatial dimension check versus upstream. The local T8 trim interface and helper retain an older/smaller signature than current upstream. The author of these differences cannot be proved from available history; they are classified as local variants, not claimed as original KoO code. Both variants are retained in the package.

Two release-only identifiers are necessary to make those variants coexist deterministically with upstream repositories, without depending on custom-node load order: `H3InjectVideoLatent` → `KoOH3InjectVideoLatent` (node 1302), and `MiniMaxH3OutputTrimT8` → `KoOMiniMaxH3OutputTrimT8` (nodes 807, 922). Python class names and function bodies remain intact. The other 58 original identifiers remain unchanged. The original workflow stays untouched.

The installed fearnworksnodes initializer uses `from nodes import *` and re-exports the global ComfyUI mapping. This causes `/object_info` to misleadingly attribute many unrelated classes to fearnworksnodes. The source inventory below resolves implementations directly; fearnworksnodes is not required or bundled.

Compared with upstream: SeC node file, VDA node file, SelfLift node file and KJ PointsEditor file are normalized text-identical. KJ GetImageSizeAndCount and the three retained FaceRefine classes match by AST. T8 face-refine node file is identical. VHS loader classes/functions match by AST. This is scoped source comparison, not a claim that every file of every repository is unchanged.

No original KoO JavaScript, configuration file or private helper exists in koo-h3-ultimate.
The release adds `model_paths.py` to register the existing standard `ultralytics/` and
`ultralytics/bbox/` search directories for `.pt`/`.onnx` detectors. This supplies the
directory registration that the local environment inherited from other packs;
without it the saved person fallback detector is missing from the dropdown in an
otherwise minimal install. It creates no directories or files, downloads nothing,
and retains existing search paths. No detector algorithm is replaced.
The release adds `model_paths.py` to register the existing standard `ultralytics/` and
`ultralytics/bbox/` search directories for `.pt`/`.onnx` detectors. This supplies the
directory registration that the local environment inherited from other packs;
without it the saved person fallback detector is missing from the dropdown in an
otherwise minimal install. It creates no directories or files, downloads nothing,
and retains existing search paths. No detector algorithm is replaced. Its imports are os, fractions.Fraction (unused), folder_paths, nodes and comfy_api.latest. The extracted module drops only the unused Fraction and ComfyExtension imports and unrelated DLSSPreset class. Bundled helpers are validate_audio and trim_av_output; no simulated implementations are used.

## Every original class

| Class identifier | Node IDs | Classification | Source relative to ComfyUI/custom_nodes (native modules noted) | Inclusion reason |
|---|---|---|---|---|
| `BasicGuider` | 902, 917, 1304 | Native ComfyUI | `comfy_extras/nodes_custom_sampler.py` | Excluded; supplied by compatible ComfyUI |
| `BasicScheduler` | 1117, 1305 | Native ComfyUI | `comfy_extras/nodes_custom_sampler.py` | Excluded; supplied by compatible ComfyUI |
| `CLIPLoader` | 633 | Native ComfyUI | `nodes.py` | Excluded; supplied by compatible ComfyUI |
| `ComfySwitchNode` | 1007, 1130, 1131, 1105, 1106, 1107, 1200, 1201, 1400, 1401, 2013 | Native ComfyUI | `comfy_extras/nodes_logic.py` | Excluded; supplied by compatible ComfyUI |
| `ConditioningZeroOut` | 1116 | Native ComfyUI | `nodes.py` | Excluded; supplied by compatible ComfyUI |
| `CreateVideo` | 1601, 1603, 1605, 1607, 1612, 1621, 1623, 1625, 1627, 1629 | Native ComfyUI | `comfy_extras/nodes_video.py` | Excluded; supplied by compatible ComfyUI |
| `GetImageSizeAndCount` | 3, 1202 | Third-party KJNodes | `ComfyUI-KJNodes/nodes/image_nodes.py` | External; PointsEditor also needs KJNodes web/js/editors and shared canvas scripts |
| `GrowMask` | 33 | Native ComfyUI | `comfy_extras/nodes_mask.py` | Excluded; supplied by compatible ComfyUI |
| `H3FaceStitch` | 1310 | Third-party MIT | `ComfyUI-H3-FaceRefine/nodes.py` | Class AST matches upstream; external |
| `H3FaceTrackCrop` | 1300 | Third-party MIT | `ComfyUI-H3-FaceRefine/nodes.py` | Class AST matches upstream; external |
| `H3InjectVideoLatent` | 1302 | Locally differing MIT dependency | `ComfyUI-H3-FaceRefine/nodes.py` | Included exact local class; namespaced registration prevents upstream overwrite |
| `H3PerFrameDenoise` | 1303 | Third-party MIT | `ComfyUI-H3-FaceRefine/nodes.py` | Class AST matches upstream; external |
| `ImageBlur` | 910, 912 | Native ComfyUI | `comfy_extras/nodes_post_processing.py` | Excluded; supplied by compatible ComfyUI |
| `ImageCompositeMasked` | 21 | Native ComfyUI | `comfy_extras/nodes_mask.py` | Excluded; supplied by compatible ComfyUI |
| `ImageScaleToTotalPixels` | 2 | Native ComfyUI | `comfy_extras/nodes_post_processing.py` | Excluded; supplied by compatible ComfyUI |
| `ImageStitch` | 1610 | Native ComfyUI | `comfy_extras/nodes_images.py` | Excluded; supplied by compatible ComfyUI |
| `ImageToMask` | 911 | Native ComfyUI | `comfy_extras/nodes_mask.py` | Excluded; supplied by compatible ComfyUI |
| `KSamplerSelect` | 901, 1118, 1306 | Native ComfyUI | `comfy_extras/nodes_custom_sampler.py` | Excluded; supplied by compatible ComfyUI |
| `KoOUltimateControls` | 1000 | Original KoO | `koo-h3-ultimate/__init__.py` | Included in koo_nodes.py; only six classes used by graph |
| `KoOUltimateExport` | 1600, 1602, 1604, 1606, 1611, 1620, 1622, 1624, 1626, 1628 | Original KoO | `koo-h3-ultimate/__init__.py` | Included in koo_nodes.py; only six classes used by graph |
| `KoOUltimateLoRA` | 1110, 1111, 1112, 1113 | Original KoO | `koo-h3-ultimate/__init__.py` | Included in koo_nodes.py; only six classes used by graph |
| `KoOUltimateSparse` | 1114 | Original KoO | `koo-h3-ultimate/__init__.py` | Included in koo_nodes.py; only six classes used by graph |
| `KoOUltimateT8Stitch` | 921 | Original KoO | `koo-h3-ultimate/__init__.py` | Included in koo_nodes.py; only six classes used by graph |
| `KoOUltimateTiming` | 1001 | Original KoO | `koo-h3-ultimate/__init__.py` | Included in koo_nodes.py; only six classes used by graph |
| `LTXVAudioVAEEncode` | 811 | Native ComfyUI | `comfy_extras/nodes_lt_audio.py` | Excluded; supplied by compatible ComfyUI |
| `LTXVConcatAVLatent` | 815 | Native ComfyUI | `comfy_extras/nodes_lt.py` | Excluded; supplied by compatible ComfyUI |
| `LTXVSeparateAVLatent` | 814, 819 | Native ComfyUI | `comfy_extras/nodes_lt.py` | Excluded; supplied by compatible ComfyUI |
| `LoadImage` | 1002, 1003 | Native ComfyUI | `nodes.py` | Excluded; supplied by compatible ComfyUI |
| `LoadVideoDepthAnythingModel` | 905 | Third-party VDA | `ComfyUI-Video-Depth-Anything/node.py` | External; requires video_depth_anything/ architecture and utility modules |
| `LoraLoaderModelOnly` | 900 | Native ComfyUI | `nodes.py` | Excluded; supplied by compatible ComfyUI |
| `ManualSigmas` | 2012 | Native ComfyUI | `comfy_extras/nodes_custom_sampler.py` | Excluded; supplied by compatible ComfyUI |
| `MaskToImage` | 909 | Native ComfyUI | `comfy_extras/nodes_mask.py` | Excluded; supplied by compatible ComfyUI |
| `MiniMaxH3AVDecodeT8` | 920, 1120 | Third-party T8 | `minimax-h3-audio-T8/h3_t8/nodes.py` | External dependency; excluded from ZIP |
| `MiniMaxH3AudioConditioningT8` | 925 | Third-party T8 | `minimax-h3-audio-T8/h3_t8/nodes.py` | External dependency; excluded from ZIP |
| `MiniMaxH3FaceRefineConditioningT8Advanced` | 915 | Third-party T8 | `minimax-h3-audio-T8/h3_t8/nodes_face_refine_advanced.py` | External dependency; excluded from ZIP |
| `MiniMaxH3FaceRefinePlanT8Advanced` | 913 | Third-party T8 | `minimax-h3-audio-T8/h3_t8/nodes_face_refine_advanced.py` | External dependency; excluded from ZIP |
| `MiniMaxH3FaceRefineSamplerT8Advanced` | 916 | Third-party T8 | `minimax-h3-audio-T8/h3_t8/nodes_face_refine_advanced.py` | External dependency; excluded from ZIP |
| `MiniMaxH3ImageToVideo` | 1103 | Native ComfyUI | `comfy_extras/nodes_minimax_h3.py` | Excluded; supplied by compatible ComfyUI |
| `MiniMaxH3OutputTrimT8` | 922, 807 | Locally differing GPL dependency | `minimax-h3-audio-T8/h3_t8/nodes.py` | Included exact local class plus trim_av_output and validate_audio; schema ID namespaced |
| `MiniMaxH3ReferenceToVideo` | 805, 1104, 1108, 1301 | Native ComfyUI | `comfy_extras/nodes_minimax_h3.py` | Excluded; supplied by compatible ComfyUI |
| `MiniMaxH3SigmaShift` | 1115, 2011 | Native ComfyUI | `comfy_extras/nodes_minimax_h3.py` | Excluded; supplied by compatible ComfyUI |
| `Note` | 2001, 2003, 2004, 2005, 2006, 2007, 2009, 2010 | Native frontend note | `ComfyUI frontend Note` | Excluded; supplied by compatible ComfyUI |
| `PointsEditor` | 31 | Third-party KJNodes | `ComfyUI-KJNodes/nodes/curve_nodes.py` | External; PointsEditor also needs KJNodes web/js/editors and shared canvas scripts |
| `PrimitiveBoolean` | 1004 | Native ComfyUI | `comfy_extras/nodes_primitive.py` | Excluded; supplied by compatible ComfyUI |
| `PrimitiveInt` | 1008 | Native ComfyUI | `comfy_extras/nodes_primitive.py` | Excluded; supplied by compatible ComfyUI |
| `PrimitiveStringMultiline` | 1005, 1006 | Native ComfyUI | `comfy_extras/nodes_primitive.py` | Excluded; supplied by compatible ComfyUI |
| `RandomNoise` | 903, 918, 1307 | Native ComfyUI | `comfy_extras/nodes_custom_sampler.py` | Excluded; supplied by compatible ComfyUI |
| `ResolutionSelector` | 1102 | Native ComfyUI | `comfy_extras/nodes_resolution.py` | Excluded; supplied by compatible ComfyUI |
| `SamplerCustomAdvanced` | 904, 919, 1308 | Native ComfyUI | `comfy_extras/nodes_custom_sampler.py` | Excluded; supplied by compatible ComfyUI |
| `SeCModelLoader` | 30 | Third-party SeC | `Comfyui-SecNodes/nodes.py` | External; requires bundled inference/, model_config/, sec/ helpers from upstream |
| `SeCVideoSegmentation` | 32 | Third-party SeC | `Comfyui-SecNodes/nodes.py` | External; requires bundled inference/, model_config/, sec/ helpers from upstream |
| `SelfLiftH3Sampler` | 1119 | Third-party SelfLift | `comfyui-SelfLift/nodes.py` | External even though branch unselected; helpers h3_upscaler.py, h3_tiling.py, selflift.py, diagnostics.py |
| `SetLatentNoiseMask` | 813 | Native ComfyUI | `nodes.py` | Excluded; supplied by compatible ComfyUI |
| `SolidMask` | 812 | Native ComfyUI | `comfy_extras/nodes_mask.py` | Excluded; supplied by compatible ComfyUI |
| `UNETLoader` | 632, 914, 1100, 1101 | Native ComfyUI | `nodes.py` | Excluded; supplied by compatible ComfyUI |
| `VAEDecode` | 759, 1309 | Native ComfyUI | `nodes.py` | Excluded; supplied by compatible ComfyUI |
| `VAELoader` | 616, 617 | Native ComfyUI | `nodes.py` | Excluded; supplied by compatible ComfyUI |
| `VHS_LoadVideo` | 10 | Third-party VideoHelperSuite | `comfyui-videohelpersuite/videohelpersuite/load_video_nodes.py` | External; requires VHS frontend and ffmpeg support |
| `VideoDepthAnythingOutput` | 808 | Third-party VDA | `ComfyUI-Video-Depth-Anything/node.py` | External; requires video_depth_anything/ architecture and utility modules |
| `VideoDepthAnythingProcess` | 906 | Third-party VDA | `ComfyUI-Video-Depth-Anything/node.py` | External; requires video_depth_anything/ architecture and utility modules |

Excluded unrelated local packages include koo-h3-fusion-v2, koo-h3-ultimate/DLSSPreset, all NVIDIA/DLSS packages, Veda-on-ComfyUI, Comfyui_Minimax_h3_latent_Upscaler (SelfLift already contains the needed architecture), and other custom-node repositories absent from this graph. Impact Pack/Subpack is not mandatory here: FaceRefine contains standard-folder fallbacks for these selected detector paths.


## Relevant external runtime helper chains

- T8 audio conditioning: `h3_t8/nodes.py` → `conditioning.py`, using the repository's prompt/media preparation, native H3 conditioning interfaces, core/audio utilities and semantic bridge support. The AudioConditioning class body matches current upstream; its full package initialization imports its own supported modules, so install the official dependency normally.
- T8 AV decode: `h3_t8/nodes.py` → `audio_ops.decode_av_latent` → `core.nested_av_parts` and native `comfy_extras.nodes_audio.vae_decode_audio`. Audio data and original waveform mux links are preserved.
- T8 face plan/conditioning/sampler and delegated stitch: `nodes_face_refine_advanced.py` → `face_refine_advanced.py` → `core.py` and `sampling.setup_dual_clock_sampling`. The detector model is resolved against the standard models tree; there is no automatic YuNet download in that code.
- Adaptive FaceRefine: external `nodes.py` includes face detection, identity matching and stitch helpers. Runtime imports include ultralytics, numpy, torch, scipy and insightface. `picker_api.py` and its web scripts remain external; they are not required by the extracted latent-injection class.
- SeC: `nodes.py` imports its repository's `inference/` model classes, tokenizer configuration and SeC inference architecture. Keep the full official dependency installation; copying only nodes.py would be insufficient.
- PointsEditor: `nodes/curve_nodes.py` imports `utility/utility.py`; `web/js/editors/point_editor_canvas.js` imports `editor_base.js` and `web/js/utility.js`. These are supplied by KJNodes.

The source inventory separates the exact bundled closure (five Python files,
10 original extracted symbols) from these externally installed dependency trees.
No missing helper was replaced by a stub.


## Relevant external runtime helper chains

- T8 audio conditioning: `h3_t8/nodes.py` → `conditioning.py`, using the repository's prompt/media preparation, native H3 conditioning interfaces, core/audio utilities and semantic bridge support. The AudioConditioning class body matches current upstream; its full package initialization imports its own supported modules, so install the official dependency normally.
- T8 AV decode: `h3_t8/nodes.py` → `audio_ops.decode_av_latent` → `core.nested_av_parts` and native `comfy_extras.nodes_audio.vae_decode_audio`. Audio data and original waveform mux links are preserved.
- T8 face plan/conditioning/sampler and delegated stitch: `nodes_face_refine_advanced.py` → `face_refine_advanced.py` → `core.py` and `sampling.setup_dual_clock_sampling`. The detector model is resolved against the standard models tree; there is no automatic YuNet download in that code.
- Adaptive FaceRefine: external `nodes.py` includes face detection, identity matching and stitch helpers. Runtime imports include ultralytics, numpy, torch, scipy and insightface. `picker_api.py` and its web scripts remain external; they are not required by the extracted latent-injection class.
- SeC: `nodes.py` imports its repository's `inference/` model classes, tokenizer configuration and SeC inference architecture. Keep the full official dependency installation; copying only nodes.py would be insufficient.
- PointsEditor: `nodes/curve_nodes.py` imports `utility/utility.py`; `web/js/editors/point_editor_canvas.js` imports `editor_base.js` and `web/js/utility.js`. These are supplied by KJNodes.

The source inventory separates the exact bundled closure (five Python files,
10 original extracted symbols) from these externally installed dependency trees.
No missing helper was replaced by a stub.
