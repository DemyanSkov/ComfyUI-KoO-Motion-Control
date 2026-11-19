# KoO MOTION CONTROL — REQUIRED MODELS & DOWNLOADS

Verified 2026-11-16 using official source metadata and HTTP HEAD requests; no model weights were downloaded.

**Saved controls:** Role Swap + Adaptive Face Refine; `dlss_enabled=true` is inert because no DLSS branch exists. Fashion/SelfLift and optional LoRAs are unselected. All 123 original node modes are 0; lazy switches select branches. Face models below are optional by feature, but YOLO and buffalo_l are needed for the saved Adaptive selection. The older note saying “Face Refinement OFF” is stale; the release preserves the actual controls.

## A. REQUIRED — Main Pika H3 Flex Role Swap

| Model | Exact filename | Installation directory | Direct download URL | Status |
|---|---|---|---|---|
| MiniMax H3 Ref2VA INT8 | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | `ComfyUI/models/diffusion_models/` | [Download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | Required |
| Pika H3 Flex Ref2VA adapter | `pika_h3_flex_ref2va_v1_bf16.safetensors` | `ComfyUI/models/loras/` | [Download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/pika_h3_flex_ref2va_v1_bf16.safetensors) | Required |
| Qwen3-VL 32B | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | `ComfyUI/models/text_encoders/` | [Download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | Required |
| MiniMax H3 Video VAE | `minimax_h3_video_vae_int8_convrot.safetensors` | `ComfyUI/models/vae/` | [Download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) | Required |
| MiniMax H3 Audio VAE | `minimax_h3_audio_vae_fp32.safetensors` | `ComfyUI/models/vae/` | [Download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) | Required |
| SeC-4B FP16 | `SeC-4B-fp16.safetensors` | `ComfyUI/models/sams/` | [Download](https://huggingface.co/VeryAladeen/Sec-4B/resolve/main/SeC-4B-fp16.safetensors) | Required |
| Video Depth Anything ViT-S | `video_depth_anything_vits.pth` | `ComfyUI/models/videodepthanything/` | [Download](https://huggingface.co/depth-anything/Video-Depth-Anything-Small/resolve/main/video_depth_anything_vits.pth) | Required — automatic download |

- **SeC-4B FP16:** SeC model_config/tokenizer/inference helpers come from the full upstream custom-node dependency.
- **Video Depth Anything ViT-S:** Downloaded automatically by LoadVideoDepthAnythingModel if absent; manual prefetch is optional.

## B. OPTIONAL — Face Refinement

| Model | Exact filename | Installation directory | Direct download URL | Status |
|---|---|---|---|---|
| YuNet face detection | `face_detection_yunet_2023mar.onnx` | `ComfyUI/models/facedetection/` | [Download](https://github.com/opencv/opencv_zoo/raw/47534e27c9851bb1128ccc0102f1145e27f23f98/models/face_detection_yunet/face_detection_yunet_2023mar.onnx) | Optional |
| YOLOv8m face detection | `face_yolov8m.pt` | `ComfyUI/models/ultralytics/bbox/` | [Download](https://huggingface.co/Bingsu/adetailer/resolve/main/face_yolov8m.pt) | Optional |
| InsightFace buffalo_l | `buffalo_l.zip` | `ComfyUI/models/insightface/models/buffalo_l/` | [Download](https://github.com/deepinsight/insightface/releases/download/v0.7/buffalo_l.zip) | Optional — automatic download |
| YOLO person fallback detector | `person_yolov8m-seg.pt` | `ComfyUI/models/ultralytics/segm/` | [Download](https://huggingface.co/Bingsu/adetailer/resolve/main/person_yolov8m-seg.pt) | Optional |

- **YuNet face detection:** Exact saved alias is facedetection/, not T8 recommended face_detection/. T8 SHA256: 8f2383e4dd3cfbb4553ea8718107fc0423210dc964f9f4280604804ed2552fa4.
- **YOLOv8m face detection:** Needed by saved Adaptive Face Refine selection. Optional only if face refinement is intentionally switched off by the user.
- **InsightFace buffalo_l:** FaceAnalysis downloads/extracts on first use under models/insightface/models/buffalo_l/. Saved Adaptive identity tracking uses this pack. Pretrained models have non-commercial research terms by default; see upstream model license.
- **YOLO person fallback detector:** Additional model actually selected in node 1300 fallback_detector=segm\person_yolov8m-seg.pt. Keep this subfolder relative to the ultralytics registration.

## C. OPTIONAL — Experimental Branches

| Model | Exact filename | Installation directory | Direct download URL | Status |
|---|---|---|---|---|
| MiniMax H3 FL2VA | `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | `ComfyUI/models/diffusion_models/` | [Download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | Optional |
| H3 Latent Upscaler | `minimax_h3_latent_upscaler_3d_conv_v1_bf16.safetensors` | `ComfyUI/models/latent_upscale_models/` | [Download](https://huggingface.co/LBH-123-AI/Minimax_h3_latent_Upscaler/resolve/main/minimax_h3_latent_upscaler_3d_conv_v1/minimax_h3_latent_upscaler_3d_conv_v1_bf16.safetensors) | Optional |
| Better Human Motion LoRA | `mvmt_h3_lora_v1_500.safetensors` | `ComfyUI/models/loras/` | [Download](https://civitai.com/api/download/models/3256084?fileId=3139271) | Optional — MANUAL REVIEW: HTTP 401; creator API confirms URL |
| MiniMax H3 Realism People LoRA | `h3-realism-people-t2v-i2v-r2v.safetensors` | `ComfyUI/models/loras/` | [Download](https://huggingface.co/fal/MiniMax-H3-Realism-People-LoRA/resolve/main/h3-realism-people-t2v-i2v-r2v.safetensors) | Optional |
| H3 Facial Realism LoRA | `minimax-h3-facial-realism-closeup-cp2000.safetensors` | `ComfyUI/models/loras/` | [Download](https://huggingface.co/prithivMLmods/MiniMax-H3-Facial-Realism-CloseUp/resolve/main/minimax-h3-facial-realism-closeup-cp2000.safetensors) | Optional |
| H3 Anti-Burn LoRA | `h3_antiburn_universal_v1.safetensors` | `ComfyUI/models/loras/` | [Download](https://huggingface.co/Imagineer13/H3-Anti-Burn-LoRA/resolve/main/h3_antiburn_universal_v1.safetensors) | Optional |

- **H3 Latent Upscaler:** Selected by inactive SelfLift/Fashion branch; loader contains architecture so no external config is required for this route.
- **Better Human Motion LoRA:** Exact filename and direct URL verified from creator Civitai API model 2734359. Endpoint may require a Civitai account/API key; no credentials bundled.

## Verification and sources

16/17 direct endpoints returned HTTP 200. Better Human Motion is listed by the creator API, but its direct download returned HTTP 401 and needs account/access verification. No binary content hash comparison of local model weights was performed. The Pika filename is the Comfy-Org conversion selected by this workflow; no alternative adapter was substituted.

Primary sources: [Comfy-Org model tree](https://huggingface.co/Comfy-Org/MiniMax-H3/tree/main), [SeC pack](https://huggingface.co/VeryAladeen/Sec-4B), [Video Depth Anything](https://huggingface.co/depth-anything/Video-Depth-Anything-Small), [FaceRefine model instructions](https://github.com/Carasibana/ComfyUI-H3-FaceRefine#models), [InsightFace](https://github.com/deepinsight/insightface), [Better Human Motion creator API](https://civitai.com/api/v1/models/2734359).

The dependency repositories retain their own model and software license requirements. Weights are not bundled.
