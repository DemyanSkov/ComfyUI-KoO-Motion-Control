# ComfyUI-KoO-Motion-Control

Six original KoO nodes and two namespaced local compatibility variants used by the release workflow. Copy this folder to `ComfyUI/custom_nodes/` and install the external dependencies listed in the accompanying documentation. Requires a current MiniMax H3-capable ComfyUI; see the tested versions in DEPENDENCIES.md.

Do not keep both this package and the original `koo-h3-ultimate` enabled: they register the same six KoO identifiers. Existing installations should back up and move the old KoO folder outside custom_nodes themselves before installing this release; this task did not change it.

The two compatibility identifiers avoid collisions with externally installed T8 and FaceRefine. Load the accompanying release JSON, not a renamed original JSON. Original Python classes remain intact; no sampler, trim/audio algorithm or source spatial check was rewritten.

There is no KoO frontend extension in the inspected source. No JavaScript is needed by these eight nodes; native MarkdownNote supplies documentation. PointsEditor and other external UI scripts remain supplied by their dependencies.

See `../documentation/INSTALLATION.md`, `DEPENDENCIES.md`, `MODEL_DOWNLOADS.md`, `LICENSES.md`, and `RELEASE_AUDIT.md`. Public publication requires the owner's licensing decision for the pre-existing KoO source.

The included `model_paths.py` registers standard YOLO detector folders for the preserved Adaptive settings, retaining existing paths and creating no files.

The included `model_paths.py` registers standard YOLO detector folders for the preserved Adaptive settings, retaining existing paths and creating no files.
