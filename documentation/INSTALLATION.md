# Installation

## Windows ComfyUI portable

1. Extract the release ZIP. Copy `ComfyUI-KoO-Motion-Control` into `ComfyUI/custom_nodes/`. Keep the package files together, directly below that folder.
2. For an existing installation, close ComfyUI, back up the original `koo-h3-ultimate`, and move that original folder outside custom_nodes before enabling the release. Do not enable duplicate registrations. No installed repository was changed by this release preparation.
3. Install the seven external repositories in DEPENDENCIES.md using ComfyUI Manager or clone their official repositories into custom_nodes. Retained experimental nodes must still be registered, even while the branch is unselected. Do not enable the experimental branches.
4. From the portable installation folder, install requirements using its own interpreter, e.g.:

```powershell
.\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\ComfyUI-KoO-Motion-Control\requirements.txt
.\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\ComfyUI-KJNodes\requirements.txt
.\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\Comfyui-SecNodes\requirements.txt
.\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\ComfyUI-Video-Depth-Anything\requirements.txt
.\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\ComfyUI-VideoHelperSuite\requirements.txt
.\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\ComfyUI-H3-FaceRefine\requirements.txt
.\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\minimax-h3-audio-T8\requirements.txt
```

Folder capitalization/clone names can differ; use the actual directory names. SelfLift declares no separate requirements file in the inspected version. Use its official installation instructions. Current SeC also declares dependencies in pyproject.toml that its requirements.txt does not fully list: install its declared runtime dependencies (`opencv-python-headless`, `scipy`, `hydra-core`, `omegaconf`, `ninja`, `iopath`, `packaging`, plus its requirements.txt) in the ComfyUI environment, keeping an existing working OpenCV/Torch stack. SeC also imports transformers supplied by its upstream setup. Resolve the dependency repository's current installation guidance if the environment differs.

5. Install the exact model files from MODEL_DOWNLOADS.md. The 7 main models are required. Saved Adaptive refinement additionally uses the face/person detectors and buffalo_l. Video Depth Anything and buffalo_l can download automatically. Better Human Motion direct download needs account/access review. Keep optional LoRAs off.
6. Restart ComfyUI and refresh the frontend. Drag `workflow/KoO_Motion_Control_RELEASE.json` onto the canvas or use Workflow > Open. Select your own source video and reference image(s); old media filenames are retained as input selectors, but no media is distributed. Reset PointsEditor points to the person in your own video; its old temporary image cache is removed.
7. Inspect the START HERE documentation, then the actual controls. Saved settings are Role Swap, Adaptive Face Refine, comparison on, debug off, sheet off. The legacy DLSS Boolean remains true as saved, but no DLSS implementation is in this graph. Do not interpret the older “Face Refinement OFF” note as the saved selection.

## Standard Python installation

Activate the Python environment used by ComfyUI. Copy the package and clone/install the same dependencies under `ComfyUI/custom_nodes/`. Replace `.\python_embeded\python.exe` above with that environment's `python`, and make the requirements paths relative to your ComfyUI directory. Install the compatible ComfyUI/CUDA stack through ComfyUI's official instructions; the KoO requirements file deliberately does not replace Torch. Restart the backend, refresh the frontend, load the release workflow and choose your own input media.

Official ComfyUI installation: https://github.com/Comfy-Org/ComfyUI

## Registration and portability

The package exposes NODE_CLASS_MAPPINGS for six unchanged KoO IDs and two deterministic compatibility IDs. It does not import external custom-node packages by hardcoded folder path. T8 stitch and optional sparse attention delegate registered node IDs at runtime. It bundles no personal files, model weights, media, credentials, local absolute paths, caches or unrelated tools.

The graph keeps every original link, node position, prompt, seed, scheduler, sampler, model filename, mode, refinement selection and audio connection. Only the two collision-free class identifiers, stale preview cache metadata and the new documentation/view metadata differ. The original desktop JSON and installed repositories remain untouched.

Review RELEASE_AUDIT.md and LICENSES.md before public publication. A successful CPU import or UI load does not establish GPU video quality or model-license permission.


## Inherited compatibility items to review before enabling optional branches

The saved T8 node 925 retains its legacy `task_type` label `Ref2VA — 参考生音视频`,
while current T8 advertises `Ref2VA`. The original value is deliberately preserved;
the current frontend may normalize an unsupported combo selection. Do not treat
optional T8 execution as validated without reviewing that selection against the
installed T8 version. The active saved selection is Adaptive, not T8.

The saved person fallback detector contains a Windows separator. Windows portable
and Windows Python loading were inspected; cross-platform execution was not tested.
On another OS review relative model selectors against the dependency dropdowns.

The release's model_paths helper registers the standard detector paths automatically,
so Impact Pack/Subpack is not required solely to populate those dropdowns. Existing
paths from other packs are preserved.


## Inherited compatibility items to review before enabling optional branches

The saved T8 node 925 retains its legacy `task_type` label `Ref2VA — 参考生音视频`,
while current T8 advertises `Ref2VA`. The original value is deliberately preserved;
the current frontend may normalize an unsupported combo selection. Do not treat
optional T8 execution as validated without reviewing that selection against the
installed T8 version. The active saved selection is Adaptive, not T8.

The saved person fallback detector contains a Windows separator. Windows portable
and Windows Python loading were inspected; cross-platform execution was not tested.
On another OS review relative model selectors against the dependency dropdowns.

The release's model_paths helper registers the standard detector paths automatically,
so Impact Pack/Subpack is not required solely to populate those dropdowns. Existing
paths from other packs are preserved.
