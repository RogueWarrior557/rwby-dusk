# Project state and handoff log

Read this first when resuming work in a new session. It records what
exists, what was decided, what is pending, and what to do next. Update it
at every milestone.

## Current phase
**Pre-production, art-first stage.** The concept is approved, narrative
direction is in review, and the **master art directive** is now active. No
game code exists yet.

### START HERE (next session)
1. Read `docs/directives/01_master_art_directive.md` (the active
   instructions, verbatim) and `docs/directives/00_original_brief_summary.md`.
2. The user moved off the cloud session to work **on their own Windows
   computer**, in `C:\Users\rogue\Projects\new-project`. If this repo
   isn't there yet, clone it:
   `git clone --branch ccr-42ec6447-8f17rv https://github.com/RogueWarrior557/rwby-dusk new-project`.
   The project files sit at the repo root on that branch.
3. Do the directive's **"YOUR IMMEDIATE TASK"** list, starting with a real
   investigation of the local machine: OS, CPU, GPU/VRAM, RAM, disk,
   installed engines and editors, Python. **None of the directive's tasks
   have been done yet.** The cloud session was cut off right after
   unblocking the art plugins.
4. Art plugins are installed on the user's account: **SpriteCook** (pixel-art
   generation, MCP `https://mcp.spritecook.ai/mcp/claude`) and **Kling AI**
   (image generation, MCP `https://kling.ai/mcp/plugin`). Both need the
   user's sign-in. On a local machine there is no cloud proxy to block them.
   Check their credits and commercial-use terms before spending.
5. Official art must be grounded in **real references** (King God Castle and
   similar games, plus real-world material). The cloud container could not
   fetch any image host; a local machine can. Keep copyrighted reference
   images **out of git** (local `references/` folder, gitignored) and commit
   only a reference index with links, attribution and lessons.
6. **Get the user's approval** of a visual direction before establishing the
   official style.

### Art history (for context)
* The earlier cloud attempts at official art (SVG Maren draft) were made
  **without references**, and the user rejected that approach. Treat
  `art/official/maren_vey/` as a discarded exploration, not a candidate.
* Art was briefly put on hold while the user was on their phone. The master
  art directive lifts that hold.

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
| Power system (Lumen Arts) | `docs/design/04_power_system.md` | Five power sources, seven Arts plus lost Naming, rare gifts, legendary artifacts, faction control, every hero's power, and Maren rebuilt as a Wick-born frontline Captain with the First Lantern |
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
| Maren is hero #1 of 24: a **deployable frontline Captain**, the strongest unit (Wick-born, First Lantern, Naming in Act III); the base object is renamed **the Beacon** | Adopted after user feedback that she felt like a blank canvas | `04_power_system.md` §9 |
| Engine: Godot 4.7.x + GDScript | **Pending user approval** | See proposal §8.3 |
| Title | **Under review.** User proposed *Faith in Light* and *Nothing in Faith*. *Nothing in Faith* is intentional: "the Nothing" (the Hush) is what burned memories become, so the faith is literally full of Nothing. Recommended: adopt it, call the Hush "the Nothing" in common speech, make "Faith in Light" the Church's creed and "There is Nothing in faith" the Quiet's reply, and add a store tagline. **Awaiting the user's confirmation.** | Trademark check needed before launch |
| Cloud Default environment network | Allowed `mcp.spritecook.ai` and `kling.ai` (approved by user) | Only relevant to cloud sessions |

## Pending user decisions
* Story review questions in `docs/design/03_story_review.md` §6: Tobin's
  unrestored path, Ansel's redemption, keeping the endings, the defined
  protagonist, the tone level, Maren's power level, and the Offering
  ending.
* Still open from the proposal (§9): business model; engine (Godot) and
  permission to download and run its binary; trademark check on the title.
* Title: confirm *Nothing in Faith* and the lore integration (see Decisions).
* Visual direction: three directions are to be proposed per the art
  directive, and need approval.

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
