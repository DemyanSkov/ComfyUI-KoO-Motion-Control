"""Portable KoO nodes plus explicitly namespaced local compatibility variants."""
from .model_paths import register_detector_paths
register_detector_paths()
from .koo_nodes import (UltimateControls, UltimateTiming, UltimateLoRA,
                        UltimateExport, UltimateSparse, UltimateT8Stitch)
from .face_latent import H3InjectVideoLatent
from .trim import MiniMaxH3OutputTrimT8

_V3 = [UltimateControls, UltimateTiming, UltimateLoRA, UltimateExport,
       UltimateSparse, UltimateT8Stitch, MiniMaxH3OutputTrimT8]
# ComfyUI supports ComfyNode classes in NODE_CLASS_MAPPINGS. Initialize their
# real schemas just as its V3 loader does; the legacy face node shares this map.
NODE_CLASS_MAPPINGS = {cls.GET_SCHEMA().node_id: cls for cls in _V3}
NODE_CLASS_MAPPINGS['KoOH3InjectVideoLatent'] = H3InjectVideoLatent
NODE_DISPLAY_NAME_MAPPINGS = {cls.GET_SCHEMA().node_id: cls.GET_SCHEMA().display_name for cls in _V3}
NODE_DISPLAY_NAME_MAPPINGS['KoOH3InjectVideoLatent'] = 'KoO | H3 Inject Video Latent (local compatibility)'
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
