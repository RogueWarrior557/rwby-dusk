# Project state and handoff log

Read this first when resuming work in a new session. It records what
exists, what was decided, what is pending, and what to do next. Update it
at every milestone.

## Current phase
**Pre-production: research complete, concept proposal awaiting approval.**
No game code exists yet, by design: the brief requires approval of the
concept, narrative premise and combat direction before implementation.

## Repository
* A standalone git repo with its own history (no shared ancestry with the
  Minecraft modpack in the parent repo).
* Pushed to `RogueWarrior557/rwby-dusk`, branch `ccr-42ec6447-8f17rv`, with
  `git push origin main:ccr-42ec6447-8f17rv`.
* The cloud session cannot create new GitHub repositories. To move this
  project into its own GitHub repo, create an empty repo, then:
  `git remote add game <url> && git push game main`. History is already
  clean.

## Completed (2026-11-23)
| Work | Location | Notes |
|---|---|---|
| 7 research workstreams | `docs/research_notes/Pixel tactics RPG design research/` | Pixel art; engine/tech; KGC combat and heroes; KGC modes/economy/visuals; autobattler and mobile games; roguelike/tactics/narrative games; mobile UX/narrative/economy/feel. Mostly search-snippet sourced (see limitations). |
| Synthesized research report | `docs/reports/Pixel tactics RPG design research.md` | Comparison matrix, transferable principles, limitations |
| Environment constraints (verified) | `docs/research/environment_constraints.md` | Tooling and network facts |
| Sprite tooling | `tools/pixelforge/pixelforge.py`, `tools/pixelforge/ramps.py` | Text-grid sprite compiler; OKLCH hue-shifted ramp builder |
| Art feasibility spike | `docs/research/art_spike/` | 32×32 knight, portrait readability mock, lighting test, 8-hero silhouette test |
| Concept proposal | `docs/design/00_concept_proposal.md` | Three concepts, scoring, recommendation (**Hushlight**), world, narrative premise, combat foundation, tech stack, roadmap |

## Decisions made so far
| Decision | Status | Rationale |
|---|---|---|
| Standalone repo, pushed to the session branch | Done | The user asked for a new repo; this session can't create GitHub repos |
| Sprites authored as text grids, compiled by pixelforge | Adopted for spikes | No artist or image model available; tested feasible at 32 px |
| 32×32 unit canvas, 270 px portrait logical width, integer scaling | Proposed | Research recommendation plus our own readability test |
| Concept: Hushlight | **Pending user approval** | See proposal §4 |
| Engine: Godot 4.7.x + GDScript | **Pending user approval** | See proposal §8.3 |

## Pending user decisions
See `docs/design/00_concept_proposal.md` §9.

## Next steps after approval (M1, technical foundation)
1. Download and verify the Godot 4.7.x Linux binary headless (needs the
   user's permission). Fallback: TypeScript web stack.
2. Create the Godot project skeleton (`game/`) with pixel-perfect settings,
   the folder structure, and an architecture doc.
3. Data schemas (heroes, abilities, enemies, waves) plus a Python
   validator.
4. pixelforge → Godot SpriteFrames importer.
5. Deterministic combat core skeleton with unit tests (headless).
6. Web export plus a Playwright screenshot check at 3×, 4× and 5×.

## Known limitations and open risks
* The research is largely snippet-sourced. King God Castle's grid size,
  formulas, sprite sizes and UI are unverified.
* Godot has not yet been executed in this container.
* The Android SDK host is blocked; iOS needs macOS.
* Music production capability is limited. A composer is recommended
  before commercial release.

## Bug log
None yet (no game code). Spike bugs found and fixed are recorded in
`docs/research/art_spike/README.md`.
