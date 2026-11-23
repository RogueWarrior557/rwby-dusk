# Project state and handoff log

Read this first when resuming work in a new session. It records what
exists, what was decided, what is pending, and what to do next. Update it
at every milestone.

## Current phase
**Pre-production: concept approved (Hushlight); narrative direction in
review.** No game code exists yet.
* **Art is ON HOLD** at the user's request (2026-11-23: "you can't make any
  images or art for the game for the time being"). Do not produce artwork
  until the user lifts this.
* The user wants official art to be **based on real references** (King
  God Castle and similar games). Image hosts are blocked in this
  environment, and a proposed network change was declined. Next time art
  resumes, get references first (the user supplies images, or approves
  network access) before drawing anything.

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
| Narrative bible v2 | `docs/design/01_narrative_bible.md` | World truth layers, rules of light, timeline, 12-chapter plot, choices map, burn-a-memory, foreshadowing ladder, endings, 24 hero design facts, symmetric bond map (28 pairs) |
| Story review packet | `docs/design/03_story_review.md` | One-page story, chapter summaries, all 24 heroes' personal stories, antagonists' stories, open questions for the user |
| Art tools (paused) | `tools/artrender/` (render.js, composite.py, inkkit.py), `art/official/maren_vey/` | SVG→PNG renderer with layer isolation; compositing (rim light, bloom, shafts, motes, grading, grain); tapered strokes and auto cel-shading. Maren draft v3 is **not** final and was made without references. |

## Decisions made so far
| Decision | Status | Rationale |
|---|---|---|
| Standalone repo, pushed to the session branch | Done | The user asked for a new repo; this session can't create GitHub repos |
| Sprites authored as text grids, compiled by pixelforge | Adopted for spikes | No artist or image model available; tested feasible at 32 px |
| 32×32 unit canvas, 270 px portrait logical width, integer scaling | Proposed | Research recommendation plus our own readability test |
| Concept: Hushlight | **Approved** by the user ("Exactly") | See proposal §4 |
| Official art style: mostly cartoon, semi-realistic undertones, mood carried by faces | Direction given by the user; production on hold | Must be grounded in references |
| Maren is hero #1 of 24 (Hearth commander) | Adopted | Narrative bible §14 |
| Engine: Godot 4.7.x + GDScript | **Pending user approval** | See proposal §8.3 |

## Pending user decisions
* Story review questions in `docs/design/03_story_review.md` §6: Tobin's
  unrestored path, Ansel's redemption, keeping all four endings, the defined
  protagonist, and the tone level.
* Still open from the proposal (§9): business model; engine (Godot) and
  permission to download and run its binary; trademark check on the title.

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
