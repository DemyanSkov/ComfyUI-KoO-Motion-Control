"""Register the standard detector directories required by saved FaceRefine inputs.

No files or models are created. Existing model search paths are retained.
"""
import os
import folder_paths

def register_detector_paths():
    for key, parts in [('ultralytics', ('ultralytics',)),
                       ('ultralytics_bbox', ('ultralytics', 'bbox'))]:
        folder_paths.add_model_folder_path(key, os.path.join(folder_paths.models_dir, *parts))
        paths, extensions = folder_paths.folder_names_and_paths[key]
        folder_paths.folder_names_and_paths[key] = (paths, set(extensions) | {'.pt', '.onnx'})
