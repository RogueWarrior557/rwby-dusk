# Art feasibility spike (pre-production)

**Question:** can a team with no human pixel artist and no image-generation
model produce pixel art that meets a professional bar, by placing pixels
deliberately in text grids and compiling them with `tools/pixelforge`?

**This is not final art.** The knight is a concept-neutral test subject. Its
palette (`palettes/spike.json`) is provisional.

## Files
| File | What it is |
|---|---|
| `palettes/spike.json`, `spike.pal`, `spike_swatch.png` | 29-colour provisional palette: 7 hue-shifted OKLCH ramps plus outline and specular |
| `compose_knight_v1.py` | Authoring helper: hand-placed row segments, layered shield → body → sword |
| `knight_v1.pxs` | Compiled 32×32 text-grid sprite (the canonical source format) |
| `knight_v1_preview_x10.png` | 10× nearest-neighbour preview |
| `readability_mock_portrait_270w_x4.png` | 14 units on a 7×10 board of 32 px tiles in a 270×480 portrait view, scaled 4× to 1080×1920. Enemies are a palette swap plus mirror. |

## Findings (observed by inspecting the rendered output)
1. **Feasible at 32×32.** After one correction pass (an off-centre shield
   boss, a misaligned sword grip), the sprite has a clear silhouette, a
   consistent pixel scale, deliberate value shading on the steel, and a
   readable character detail (the glowing visor slit).
2. **Correction passes are mandatory.** Both defects were visible only in
   the rendered preview, not in the text grid. Rendered-preview review must
   be part of every sprite's QA.
3. **Palette swaps create readable factions cheaply.** Remapping two ramps
   (crimson → arcane, steel one step darker) gives an immediately distinct
   team. This supports a palette-swap plan for rarity tiers, factions and
   enemy variants.
4. **Board fit.** A 7-column board of 32 px tiles uses 224 of 270 virtual
   pixels. That leaves margins for safe areas, and in portrait leaves
   substantial vertical room for prep and bench UI. At 4× on a 1080 px-wide
   phone, a unit is roughly 100 physical px wide, small but legible. This
   matches the research recommendation of 32×32 canvases with 22–28 px
   characters.
5. **Weaknesses seen:** the plume is thin, the near arm reads as a
   horizontal bar, and the knight alone is not a distinctive design.
   Distinctive silhouettes (unusual headgear, weapons and body shapes) must
   be a design requirement for every hero.

## Lighting test (`light_test/`)
**Question:** can a light/dark board read clearly in pixel art without
alpha gradients or runtime blending, so that light can carry gameplay
meaning?

| File | What it is |
|---|---|
| `floor.pxs`, `lantern.pxs` | Hand-authored 16×16 flagstone tile and 16×32 lantern post with a 2-frame flicker (palette `palettes/env.json`) |
| `light_mock.py` | Mock renderer, not engine code. Each colour has 4 precomputed light variants (dark, dim, lit, bright), computed in OKLCH: dark is low value, compressed contrast and cold; bright is warm. Band edges use 4×4 ordered (Bayer) dithering. Enemies whose feet are in darkness render as silhouettes showing only their eye glint. |
| `light_mock_x4.png`, `light_mock_detail_x4.png`, `light_mock_1x.png` | Output at 4× and at native 270×480 |

**Findings (from inspecting the output):**
1. **"Warm light, cold dark" reads instantly.** Lit, dim and dark states
   stay distinct at phone scale, and heroes in bright light pick up warm
   highlights.
2. **Silhouettes with eye glints make concealment legible.** That gives a
   clear visual rule for a gameplay state (veiled or untargetable) with no
   extra UI.
3. **Light can stay inside a strict palette.** Precomputed variants keep the
   colour count bounded (base colours × 4) and keep every pixel crisp.
4. **Bug found and fixed during inspection:** the light accumulator started
   at 0, so every unlit pixel dithered on the lit/dim threshold. Only the
   rendered image revealed this, which again shows rendered review is
   required.
5. **Still open:** the flagstone is repetitive across the board, so a real
   tileset needs 3–4 variants plus decals. The dark level may need tuning per
   environment. Units standing in dim light should get a subtle readability
   rim so they never sink into the floor.
