# Licenses and redistribution notices

The package includes a minimal extraction of two third-party components; it does not claim ownership of them.

- `face_latent.py`: MIT, copyright (c) 2026 Carasibana, from https://github.com/Carasibana/ComfyUI-H3-FaceRefine. Complete notice in `licenses/FaceRefine-MIT.txt`. Retains the installed pre-VAE spatial check; author of that local difference is not established.
- `trim.py`: GPL-3.0-or-later, copyright (C) 2026 MiniMax H3 Audio T8 contributors, from https://github.com/T8mars/comfyui-minimax-h3-audio-T8. Contains the local versions of MiniMaxH3OutputTrimT8, trim_av_output and validate_audio. Complete GPLv3 text in `licenses/GPL-3.0.txt`, upstream notice in `licenses/T8-NOTICE.txt`. Only the schema registration identifier is changed. This package distributes complete corresponding source for these excerpts. Preserve notices and GPL obligations when redistributing this combined package; it cannot be presented as an entirely MIT-licensed distribution.
- `koo_nodes.py`: original local KoO source. No license file or explicit public software license was present in its source directory. Inclusion was requested by the workflow owner. No new public license grant is inferred: **before public publication the owner must confirm authorship/rights and select compatible licensing terms for the KoO code and combined distribution.** This is an unresolved publication prerequisite, not a missing runtime implementation.
- Integration glue and documentation were prepared for this release; no license is inferred for the owner's pre-existing workflow or prompts.

External dependency repositories are installed separately from their official links. Their software and model licenses continue to apply. No model weights are redistributed. InsightFace pretrained buffalo_l has non-commercial research terms by default; consult its official model license for the intended use. Model access does not grant broader use rights.

No licensing terms were accepted and no ownership declarations were fabricated during this audit.
