# KoO Motion Control v1.0 — Release audit

Prepared 2026-11-16 from the specified experimental JSON and the actual installed
Python/JavaScript source. The release contains runnable implementations and a
documented external dependency installation. Public publication still needs the
owner's licensing decision; an optional model download needs access review.

## Inventory and package contents

Inspected **123 original nodes, 60 class identifiers, 243 links**, including all
unselected branches. All original node modes are 0: lazy switches, rather than
mode 2/4, govern inactive branches. The release has **124 nodes** after adding one
unconnected native MarkdownNote. The original graph layout and all 243 links remain.

Original KoO class IDs included unchanged:

- `KoOUltimateControls` — generation/refinement/output selection.
- `KoOUltimateTiming` — duration, native 24 FPS and 17n+5 frame planning.
- `KoOUltimateLoRA` — conditional model-only LoRA loading.
- `KoOUltimateExport` — lazy, conditional video export with existing audio/metadata behavior.
- `KoOUltimateSparse` — disabled-by-default delegation to registered SolAttnMiniMax.
- `KoOUltimateT8Stitch` — delegation to registered MiniMaxH3FaceRefineStitchAuditT8Advanced.

Locally differing third-party variants also preserved:

- `H3InjectVideoLatent` from MIT-licensed FaceRefine includes an extra spatial
  validation before VAE encode. It is registered as `KoOH3InjectVideoLatent` in the
  release only, used by node 1302.
- `MiniMaxH3OutputTrimT8`, `trim_av_output`, and `validate_audio` from GPL-licensed
  T8 retain the installed interface/PCM slicing behavior. The release registers
  `KoOMiniMaxH3OutputTrimT8`, used by nodes 807 and 922.

The provenance of the local differences is not established by available history;
they are not claimed as original KoO inventions. Their original Python class
names and function bodies remain intact. Two namespaced registration IDs avoid
load-order-dependent overwrites by upstream repositories; no other graph class
identifiers were renamed. The corresponding JSON changes are documented in
WORKFLOW_CHANGES.json.

Bundled files:

| File | Purpose |
|---|---|
| `ComfyUI-KoO-Motion-Control/__init__.py` | Actual ComfyUI registration of all eight classes |
| `koo_nodes.py` | Six exact original KoO class implementations |
| `face_latent.py` | Exact installed FaceRefine latent-injection class |
| `trim.py` | Exact installed T8 trim class and its complete two-function helper closure |
| `model_paths.py` | Standard detector search-path registration required in a minimal installation; no file/model creation |
| `requirements.txt`, `README.md` | Environment/dependency/install guidance |
| `licenses/FaceRefine-MIT.txt`, `T8-NOTICE.txt`, `GPL-3.0.txt` | Checked licenses and complete applicable notices |
| `workflow/KoO_Motion_Control_RELEASE.json` | Separate release graph with three model tables |
| `documentation/` | Installation, dependencies, licenses, model verification, inventory, source manifest and test evidence |

No original KoO JavaScript or private configuration/helper files were found.
Consequently the package needs no KoO web extension. The necessary PointsEditor,
VHS and dependency UI code is installed with the relevant external repositories.
The native MarkdownNote renders the documentation without a new custom frontend.

## Dependencies and exclusions

External dependencies: KJNodes, SeC Nodes, Video Depth Anything, VideoHelperSuite,
H3 FaceRefine, MiniMax H3 Audio T8, and SelfLift. All seven official installation
links and relevant source/helper chains are in DEPENDENCIES.md. T8 additionally
supplies the delegated stitch/audit and optional SolAttnMiniMax classes.

These repositories were **not copied into the ZIP**. Selected source comparisons
show SeC, VDA, SelfLift and PointsEditor files identical to upstream; retained
FaceRefine classes, KJ image-size class and VHS loader classes/functions match by
AST. T8 face-refine node definitions are identical. This is scoped comparison,
not a whole-repository clean-history assertion. Ten bundled original symbols
match the installed source AST, allowing only the declared trim schema-ID rename.

Native ComfyUI supplies loaders, H3 conditioning and sigma shift, samplers,
audio/video latent operations, image/mask operations, switches, primitives,
CreateVideo, ResolutionSelector, ManualSigmas and notes. These are excluded.
Unrelated KoO Fusion, DLSS/NVIDIA, Veda and standalone upscaler repositories and
the unused KoO DLSSPreset class are excluded. fearnworksnodes is excluded: its
`from nodes import *` re-export misleadingly labels unrelated nodes in live
object_info, so actual implementation files were traced separately.

## Preserved behavior and intentional release-only changes

No original file or installed custom-node source was edited. No generation,
sampler, seed, scheduler, sigma list, model filename, refinement control, prompt,
audio connection or node position was changed. Fashion, SelfLift and DLSS were
not enabled or executed. The saved DLSS Boolean remains true but is inert because
the graph has no DLSS stage. The main Pika LCM/sigma pipeline is unchanged.

The actual saved controls are **Role Swap + Adaptive Face Refine**, comparison on,
debug off and sheet off. Existing notes saying refinement is OFF are stale and
are explicitly identified in the new documentation; changing the actual controls
would have violated the preservation requirement.

Apart from the two collision-free registration IDs, the release changes only:
one unconnected documentation node/group and initial canvas-view metadata;
removal of PointsEditor/VHS temporary preview cache references; and removal of
historical local audit/cache extra fields (`KoO_DLSS_repair`, `KoO_H3_Ultimate`,
`anomalous_hashes`). Those fields included a local absolute path and stale claims
about earlier workflows. Input media filenames and point coordinates are retained
for settings preservation, but no referenced media is distributed. Users must
choose their own media and points.

## Models and link verification

The three tables contain **17 unique model entries**: the requested 16 plus the
person segmentation fallback detector actually selected in the Adaptive node.
All seven main model endpoints were verified. Filenames match the saved loader
values; installation folders were checked in actual loader code. No alternative
generation model was added.

**16/17 direct endpoints returned HTTP 200.** Better Human Motion's exact filename
and URL were returned by the creator's Civitai API, but the direct endpoint
returned HTTP 401. It is flagged MANUAL REVIEW; no URL was invented. No credentials
were supplied or distributed. Video Depth Anything and InsightFace buffalo_l
automatic-download locations are documented. T8's selected YuNet alias is
`facedetection/`, which differs from T8's recommended `face_detection/`; the table
uses the saved alias. No weights were downloaded or redistributed, and local
weight binaries were not rehashed to claim identity with remote files.

## Validation performed

Test environment: Windows, ComfyUI 0.45.0, frontend 1.58.5, Python 3.13.12,
PyTorch 2.11.0+cu130, NVIDIA GeForce RTX 5090. No package installation or upgrade
was performed in the production environment.

| Check | Result and scope |
|---|---|
| Real ComfyUI custom-node loader import | PASS; all eight package classes registered without mocks |
| Actual backend node-info schemas | PASS; all eight schemas serialize, including lazy video input |
| Original class/helper AST equivalence | PASS; ten original symbols and source hashes match |
| Controls, timing and lazy export | PASS; saved Adaptive flags preserved; disabled export does not request video; 7 seconds plans 175 frames |
| Local spatial guard | PASS; real NestedTensor mismatch rejected before any VAE access |
| CPU trim and PCM preservation | PASS; exact 12-frame slice and exact 500-sample PCM slice from small test tensors |
| Minimal GPU smoke test | PASS; same real trim operation on CUDA tensors; no H3 denoising or VAE generation was run |
| JSON IDs, slots and bidirectional links | PASS; 243 original links unchanged, no dangling/stale links |
| Execution-setting preservation | PASS; all 123 original node records match after accounting only for declared ID/preview metadata changes |
| Documentation isolation/overlap | PASS; no sockets/links/output behavior; rectangle does not overlap original nodes; positioned above the graph |
| Minimal dependency registration | PASS; seven external packs loaded, all 124 graph nodes resolved (notes are native frontend classes) |
| Standard detector paths | PASS; saved fallback detector is in the final node's available options |
| External frontend asset serving | PASS; all 115 listed extension scripts returned HTTP 200 |
| Actual ComfyUI frontend loading | PASS for graph loading: release opened, 124 nodes present, all three Markdown tables and download anchors rendered |
| ZIP integrity and extracted install | PASS; CRC checked, all 24 members present, extracted package imported through the real ComfyUI loader with all eight classes and CPU/GPU trim checks passing |
| Content/privacy scan | PASS; no absolute filesystem paths, detected credential patterns, model weights, input/generated media or caches in the ZIP payload |
| Original desktop JSON | Unchanged; SHA256 listed below |

The isolated frontend initially reported missing image media, as expected for a
release without personal inputs, and a missing detector dropdown registration.
The latter was fixed by model_paths.py and verified against the backend options.
No generation was queued. Source video/reference identity quality, model loading,
full H3/Pika inference, detector inference, face-refinement quality, export codecs
and optional branch execution were **not tested**. This report makes no claim
that a full video generation succeeded.

The first attempt to start an ordinary second ComfyUI instance stalled while
loading unrelated native extras and was stopped. The successful UI validation
used the real PromptServer with only the graph's required native modules and
seven actual external dependencies, plus the release package. It did not use
simulated node classes. Test-harness import/encoding/scan issues were corrected
before the final passing checks; no failed package test is concealed as a pass.

## Remaining issues and publication prerequisites

1. The pre-existing KoO source directory contains no public license. The owner
   must confirm rights and choose compatible terms before public publication.
   The third-party MIT/GPL excerpts have complete notices/corresponding source;
   their terms cannot be removed or replaced by an all-MIT claim.
2. Better Human Motion requires manual Civitai download/access verification.
3. The inherited T8 node 925 stores the legacy task label `Ref2VA — 参考生音视频`
   while the current dependency advertises `Ref2VA`. It is retained to avoid a
   silent settings change. Review it before enabling T8 refinement; T8 execution
   is not certified by this release. The saved active refiner is Adaptive.
4. Personal media is deliberately absent. Retained media selectors/points must
   be set by each user. Cross-platform execution, particularly the retained
   Windows relative detector selector, was not tested.
5. No clean environment dependency reinstall or H3 model/inference smoke test was
   performed. GPU smoke coverage is explicitly limited to the small real trim.
   External repos can change; use the documented tested versions/source evidence
   when investigating drift. Loading an arbitrary future upstream commit is not
   certified.

The package is installable with the documented dependencies and contains real
implementations; it is not represented as legally cleared or fully generation-
qualified for immediate public publication.

Original workflow SHA256:
`5aaec374dbb3141c32b99c030ccab986eb66c29dacec7392e883b9eecaa8a205`

See MODEL_VERIFICATION.json, NODE_INVENTORY.json, SOURCE_MANIFEST.json,
UPSTREAM_COMPARISON.json, WORKFLOW_CHANGES.json and VALIDATION_RESULTS.json for
machine-readable evidence. A visual preview is provided alongside the standalone
deliverables as RELEASE_PREVIEW.jpg.
