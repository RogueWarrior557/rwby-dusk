# Pixel-Art Craft, Character Sprite Design and Sprite Animation (for a 2D pixel-art mobile tactical autobattler)

How these notes were gathered (Nov 2026). Full-page fetching was blocked for most hosts in this session: derekyu.com, slynyrd.com, aseprite.org, gamedeveloper.com, saint11.org, lospec.com, medium.com, pixelparmesan.com and all *.github.io sites failed to resolve. The web-search budget, which is shared with other agents, also ran out partway through. So the evidence comes in three levels of strength:
1. **Primary sources read in full**: source code, READMEs and docs fetched directly from raw.githubusercontent.com. This covers Aseprite source, EULA and Lua API docs; Godot docs; the LPC generator; pixel-sprite-generator; Sprator; Pixelorama; LibreSprite; PalettePainter; RampenSau; OKShift; pixelsrc; and the DawnBringer palette data. These are marked **[primary]**.
2. **Web-search result snippets**: these are citable URLs, but I could not read the pages in full, so treat the wording as the source's gist rather than an exact quote. These are marked **[snippet]**.
3. **My own inference or practitioner consensus with no fetched source**: kept in the "Inferences" subsections, never in "Cited Findings".

To strengthen these notes, allow these hosts in the session's network settings and re-fetch: slynyrd.com (Pixelblog series), saint11.org (Pedro Medeiros tutorials), lospec.com, aseprite.org/docs, gamedeveloper.com (Dead Cells, Owlboy and Eastward articles) and derekyu.com.

---

## 1. Fundamentals: line work, clusters, shading, outlines, AA, dithering, hue-shifted ramps, palettes, pixel density, value contrast

### Takeaway
Professional pixel art is mostly *cluster management*. Every group of same-coloured pixels should read as a deliberate shape. Lines use regular step patterns. Shading follows one committed light direction rather than the outline (pillow shading). Outlines and anti-aliasing are used selectively. Ramps hue-shift instead of only darkening. Every asset sits on one shared pixel grid (no mixels). A small curated palette (16–64 colours, as in DB32, Endesga 32, Resurrect 64 and Apollo) enforces most of this automatically.

### Cited Findings
**Line work and jaggies**
- The simplest line slopes read as "perfect lines": 0:1, 1:2, 1:1, 2:1 and 1:0, because the eye can follow them easily. — [OpenGameArt pixel-art tutorial chapter](https://opengameart.org/node/5490) [snippet]
- Practitioner advice: build lines from equal-sized segments (slopes of 1/2, 1/3, 1/4, 1/5). Jaggies, the irregular "staircase" steps, are only a problem where a smooth curve is expected. Deliberately uneven steps can make organic, textured shapes. — [PixelJoint forum thread](https://pixeljoint.com/Forum/forum_posts.asp?TID=20478) [snippet]; [Pixel Grimoire #7](https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-7-e504bfa4ddf2) [snippet]
- Editors' "pixel-perfect" freehand modes remove unintended L-corners from 1-px strokes. Cleanup is still multi-step: draw, fix corners, then fix jaggies. — [Pixel Grimoire #5](https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-4-ff4bfcd2d085) [snippet]. Aseprite ships a "Pixel Perfect freehand mode", "Shading ink", outlines and "Wide Pixels". — [Aseprite README](https://github.com/aseprite/aseprite/blob/main/README.md) [primary]

**Clusters, orphan pixels, banding**
- One-pixel clusters ("orphan pixels") are a main source of visual noise. Delete them, or replace them with small shapes when the detail matters. They are acceptable as deliberate accents, such as eyes or texture. The same author recommends "cluster sketching": block large colour areas first, then refine. — [Pixel Grimoire #2](https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-2-bcd705cb04d7) [snippet]
- In pixel art, "banding" means lines that appear where clusters align. A TU Delft research project on automated pixel-art correction ("Pixel Fixer") defines it formally: two differently coloured segments, each at least 2 px long, adjacent along their long edge, with aligned endpoints. The same work notes that dithering helps little against banding. — [TU Delft repository, Pixel Fixer](https://repository.tudelft.nl/record/uuid:b3c91b18-d9e8-48e0-91ce-8afafd2439d8) [snippet]
- Anti-aliasing turns into banding when the AA pixels hug an outline, so AA requires attention to cluster shape. — [PixelJoint thread](https://pixeljoint.com/forum/printer_friendly_posts.asp?TID=11303) [snippet]

**Pillow shading and light direction**
- Pillow shading means concentric bands of darker colour that follow the outline. It "pays no attention to the light source" and follows the area's shape rather than the form it represents. It is a pronounced form of banding. — [OpenGameArt "Chapter 4: Shadow and Light"](https://opengameart.org/content/chapter-4-shadow-and-light) [snippet]; [Pixnote shading guide](https://pixnote.net/en/learn/shading) [snippet]
- A practical test: after shading, ask "where is the light coming from?" If you can't answer, it is probably pillow shading. Light "from the camera" easily tricks artists into it. In an RPG where the light source is ambiguous, still commit to one consistent direction. With limited colours, push the bands toward the edges and use mainly two-tone shading. — [Pixnote](https://pixnote.net/en/learn/shading) [snippet]; [PixelJoint critique thread](https://pixeljoint.com/forum/printer_friendly_posts.asp?TID=26842) [snippet]

**Outlines and selective outlining (selout)**
- Selout replaces a uniform black outline with outline colours that vary with the lighting. Where the sprite is darkest the outline is dark; where it is lightest the outline is lighter. A common recipe is to use the adjacent fill colour one ramp-step darker. — [itch.io "Pixel Tutorial – Selective Outlines"](https://itch.io/t/2422252/pixel-tutorial-selective-outlines) [snippet]; [Lospec "Pixel Art Outlines Part 2: Using Color"](https://lospec.com/articles/pixel-art-outlines-part-2-using-color) [snippet]
- Black outlines can vanish over dark ground and leave saw-toothed edges. Selout keeps the border readable on varied backgrounds. Interior lines use the colour of the nearer part, or a darker shade for emphasis. Keep selout colours close in value, because a stray light or dark pixel creates jaggies. — [Solarus forum selout tutorials](https://forum.solarus-games.org/en/index.php?msg=5486) [snippet]; [Lospec outlines article](https://lospec.com/articles/pixel-art-outlines) [snippet]; [PixelJoint selout study](https://pixeljoint.com/pixelart/9562.htm) [snippet]
- Selout can be automated. The `pixelsrc` crate exposes an `apply_selout` transform that varies outline colour by the adjacent fill pixels. — [docs.rs pixelsrc apply_selout](https://docs.rs/pixelsrc/latest/pixelsrc/transforms/fn.apply_selout.html) [snippet]

**Anti-aliasing**
- "Alias" in pixel art usually means jaggies, the staircase effect. Manual AA places intermediate colours at the steps. Pixel artists disagree strongly about AA and banding. — [itch.io "Pixel Tutorial – Anti-aliasing"](https://itch.io/t/3524316/pixel-tutorial-anti-aliasing) [snippet]; [Pixel Grimoire #5](https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-4-ff4bfcd2d085) [snippet]; dedicated article: [Pixel Parmesan "Anti-Aliasing Fundamentals for Pixel Artists"](https://pixelparmesan.com/anti-aliasing-fundamentals-for-pixel-artists) (not readable in this session)

**Dithering**
- Dither sparingly and on purpose. Heavy dithering looks noisy and muddy, and veteran opinion is split ("dirty" vs essential). Test at 1:1 or display size: if a dithered area reads as TV static, it is over-dithered. Prefer ordered patterns (Bayer or checkerboard) over random or Floyd–Steinberg error diffusion for crisp pixel art. — [Divoom "Pixel Art Dithering: When to Use It and When to Stop"](https://divoom.com/blogs/setup-ideas/pixel-art-dithering-when-to-use-and-stop) [snippet]; [bitmapped dithering guide](https://martink-rsa.github.io/bitmapped/guides/dithering) [snippet]; [Pixel Parmesan "Dithering for Pixel Artists"](https://pixelparmesan.com/dithering-for-pixel-artists) [snippet]
- Keep dither "in reserve" and make dithered transitions smooth by choosing colours with neighbouring hues and values. — [PixelJoint thread](https://pixeljoint.com/forum/printer_friendly_posts.asp?TID=14450) [snippet]

**Hue shifting and ramps**
- Raymond Schlitter (Slynyrd) says a good ramp should hue-shift across its length. Beginners make "straight ramps" that change only brightness and saturation. He likes strong shifts because they "create harmony between ramps", but says "20 is about as high as I go" (degrees across a ramp). In his example palette of 8 ramps, the ramps' hues are offset by 45° to cover the wheel. "Because of the hue shift every color is surrounded by colors that can work together." — [Slynyrd Pixelblog 1 – Color Palettes](https://www.slynyrd.com/blog/2018/1/10/pixelblog-1-color-palettes) [snippet]
- Rationale from the community: hue shifting adds contrast, avoids dull ramps, and mimics how real light shifts hue between highlight and shadow. — [PixelJoint resources thread](https://pixeljoint.com/forum/forum_posts.asp?TID=15138) [snippet]
- Tools encode the Slynyrd method:
  - Chickensoft **PalettePainter**, a .NET CLI, generates palettes "based on the principles described in Slynyrd's seminal blog". Parameters: `--hue`, `--num-ramps`, `--num-colors-per-ramp`, `--hue-shift`, `--hue-spectrum`, `--desaturate`, `--scale`. — [PalettePainter README](https://github.com/chickensoft-games/PalettePainter) [primary]
  - **RampenSau** is a JS library that generates ramps via hue cycling plus easing functions. — [RampenSau README](https://github.com/meodai/rampensau) [primary]
  - **OKShift** is an Aseprite extension for "OKLab perceptual brightness-preserving hueshift". It contrasts with Aseprite's native HSV hue shift, which changes perceived brightness. — [OKShift README](https://github.com/WangleLine/OKShift) [primary]

**Well-known limited palettes**
- **DawnBringer 32 (DB32)**, by Richard "DawnBringer" Fhager, is bundled with Aseprite. DawnBringer described it as "as multi-purpose as possible, but with a clear slant towards archetypical game graphics & pixelart". Users credit its muted colours, such as the two "dirty yellows", for its versatility. Because so many assets use it, art converted to DB32 combines well with other assets. — [Aseprite bundled dawnbringer-palettes manifest](https://github.com/aseprite/aseprite/blob/main/data/extensions/dawnbringer-palettes/package.json) [primary]; [PixelJoint DB32 thread](https://pixeljoint.com/forum/printer_friendly_posts.asp?TID=16247) [snippet]; [OpenGameArt "Some insights about pixel art color ramps"](https://opengameart.org/node/20643) [snippet]
- **Endesga 32**: Lospec describes it as "high contrast, high saturation", originally made for the game NYKRA, with about 182k downloads at snapshot time. — [Lospec Endesga tag](https://lospec.com/palette-list/tag/endesga) [snippet]
- **Resurrect 64** by Kerrie Lake: about 322k Lospec downloads. Users call it a go-to palette with long ramps (turquoise, pink, warm orange). Some add a deeper black (#18141a) or swap the browns per project. — [Lospec Resurrect 64](https://lospec.com/palette-list/resurrect-64) [snippet]; [itch.io user post](https://itch.io/post/9762454) [snippet]
- **Apollo**: a 46-colour Lospec palette with about 165k downloads. The search did **not** confirm the author (commonly attributed to AdamCYounis; unverified). — [Lospec linear tag listing](https://lospec.com/palette-list/tag/%20linear) [snippet]
- **PICO-8**: a fixed 16-colour palette on a 128×128 display. There are 16 further "secret" colours (indices 128–143), but only 16 can be shown per frame, swapped in via the screen palette. — [PICO-8 manual](https://www.lexaloffle.com/dl/docs/pico-8_manual.html) [snippet]; [NerdyTeachers PICO-8 colour guide](https://nerdyteachers.com/PICO-8/Guide/Colors) [snippet]
- **Constraint palettes can be bent deliberately.** Yacht Club broke the NES palette "purely out of preference". Their reasons were materials no NES colour fitted (Polar Knight's sheepskin) and darker skin tones the NES palette could not render. Sources disagree on how many colours were added: 4 per Engadget, 5 ("darker and desaturated colors") per the artist in PC Gamer. — [Yacht Club "Breaking the NES"](https://www.yachtclubgames.com/blog/breaking-the-nes/) [snippet]; [Engadget](https://www.engadget.com/2014/06/27/why-shovel-knight-couldnt-run-on-a-real-nes/) [snippet]; [PC Gamer](https://www.pcgamer.com/games/action/shovel-knight-artist-says-throwback-games-need-retro-authenticity-but-cant-coast-on-nostalgia-alone-part-of-the-appeal-of-the-nes-era-of-game-making-was-that-everything-was-a-new-idea) [snippet]
- My own OKLab analysis of the DB32 values in Aseprite's `db32.gpl` (data [primary]: [db32.gpl](https://github.com/aseprite/aseprite/blob/main/data/extensions/dawnbringer-palettes/db32.gpl)):
  - Apart from pure black and white, the 30 remaining colours spread fairly evenly from OKLab L≈0.26 to 0.94.
  - 9 of 32 colours are near-neutral (chroma < 0.05).
  - Darks are hue-shifted toward purple and blue: #222034 h≈288°, #45283c h≈339°, #3f3f74 h≈282°.
  - Lights shift toward yellow, cream and cyan: #fbf236, #eec39a, #cbdbfc.
  - Example warm ramp: #45283c (L .32, h 339°) → #663931 (.40, 31°) → #8f563b (.51, 46°) → #d9a066 (.75, 66°) → #eec39a (.84, 65°). That is a hue rotation of about 90° across the ramp as it lightens.
  - This is a computed observation, not the author's stated intent.

**Pixel density consistency (mixels)**
- "Mixels" means mixed pixel sizes in one image or game, for example art drawn at 3× next to art at 2×, or sprites scaled by non-integer factors. The community treats it as a common mistake that makes assets "stick out like a sore thumb". Common causes are a big brush on a big canvas, combining art at odd scales, and improper scaling. The fix is to pick one resolution up front and keep every asset on the same grid; use 9-slicing instead of scaling UI. — [Flowlab "Stop using mixels"](https://community.flowlab.io/t/mini-rant-stop-using-mixels/38287) [snippet]; [itch.io devlog "confronting the elephant pixels"](https://itch.io/blog/1026541/day-16-confronting-the-elephant-pixels-in-the-room) [snippet]; [itch.io post](https://itch.io/post/8448610) [snippet]
- Some accept mixels for small emotes and VFX (hearts, anger marks, sweat drops) or for background layers, though others say even this breaks the look. — [itch.io post](https://itch.io/post/15078117) [snippet]; [yari-pixels "My fascination with mixels"](https://yari-pixels.github.io/Articles/mixels.html) [snippet]
- The Octopath Traveler II developers say they could not raise only the background resolution, because "the characters would look strange". This is a professional statement of the density-matching rule. — [Unreal Engine developer interview, Octopath Traveler II](https://www.unrealengine.com/developer-interviews/octopath-traveler-ii-builds-a-bigger-bolder-world-in-its-stunning-hd-2d-style) [snippet]

### Inferences
- For an autobattler with 10–20 units, the rules that matter most are:
  1. Silhouette and cluster clarity first, internal detail last.
  2. One global light direction (top-left is the common convention) applied to every unit, so units read as one set.
  3. Selout or coloured outlines rather than pure black, so units stay readable over varied arenas.
  4. Minimal dithering on units. Reserve dither for large background gradients and certain VFX.
- **Value contrast between characters and backgrounds.** I found no fetched source in this session. The usual practitioner rule, my own inference, is to give the playfield background a narrower value range and lower saturation than the units. Arenas sit in the mid-values and are desaturated. Units own the darkest darks (outlines) and the brightest highlights and saturated accents. Test by desaturating a battle screenshot: every unit should still separate from the floor.
- A shared master palette of about 32–64 colours, built as hue-shifted ramps and perhaps based on an existing Lospec palette, is the cheapest way to make work from several artists, or from code, look coherent. Licence check: Lospec palettes are colour lists. I found no licence restrictions in this session, but verify each palette's page.

### Gaps
- I could not read Derek Yu's tutorial, the Slynyrd Pixelblog beyond snippets, Michael Azzi's *Pixel Logic*, or videos by Brandon James Greer, AdamCYounis or MortMort; their hosts were blocked or the search budget ran out. Their specific rules, for example Pixel Logic's chapters on clusters and readability, are not cited here.
- There is no verified author attribution for Apollo, and no current download ranking for Lospec palettes; only snapshot numbers from snippets.
- No sourced guidance on character-versus-background value separation. This was inferred only.

---

## 2. Character sprites by size, proportions, and how notable games communicate class, personality and abilities

### Takeaway
Hard evidence on exact sprite sizes is thin. The verified data points:
- Final Fantasy I–VI field sprites are 16×24.
- LPC's open character standard uses 64×64 frames.
- Celeste renders at 320×180.
- Hyper Light Drifter renders at 480×270.

The consistent professional message is to design characters as **shape + colour first**, so they are identifiable from silhouette and dominant hue (Owlboy, Into the Breach). Gameplay state can be communicated through one bold, animated feature, such as Celeste's hair colour for dash charge, rather than fine detail.

### Cited Findings
- **Final Fantasy Pixel Remaster**: Square Enix kept the original **16×24 px** base character size across FF I–VI. — [Siliconera interview on FF Pixel Remaster sprites](https://www.siliconera.com/interview-discussing-final-fantasy-pixel-remaster-sprites-and-designs/) [snippet]
- **Celeste**, pixel art by Pedro Medeiros (Miniboss):
  - The game renders to a **320×180** texture that is then scaled up.
  - Madeline's sprite is drawn **without hair**. The hair is added in real time as a chain of about 5–6 points drawn with a small circle texture, so it stays on the game's pixel grid.
  - Hair colour communicates game state: red means dash ready, blue means dash used.
  - Sources: [Reddit r/gamedev comment attributed to the lead developer (via mirror)](https://axebps-redlib.hf.space/r/gamedev/comments/9a0cfr/how_is_the_hair_in_celeste_made/e4sgcdc/?context=3) [snippet]; [Wikipedia: Madeline (Celeste)](https://en.wikipedia.org/wiki/Madeline_(Celeste)) [snippet]; [blakecrosley.com on pixel characters](https://blakecrosley.com/blog/pixel-art-characters-on-iphone) [snippet]
- **Hyper Light Drifter**: Alx Preston said "Our game is 480p… very intentionally so". Community sources give the internal resolution as **480×270**, which integer-scales to 1080p (×4). — [GamingBolt interview](https://gamingbolt.com/our-game-is-480p-yeah-its-low-resolution-and-very-intentionally-so) [snippet]; [Nintendo Life](https://www.nintendolife.com/news/2014/11/resolution_doesnt_matter_with_2d_games_says_hyper_light_drifter_developer) [snippet]
- **Owlboy**: Simon Stafsnes Andersen based character design on **shapes and colours so players can identify characters easily**. He wanted to showcase pixel art "with as few 'cheats' as possible". — [Game Developer: "Using graphics to express character and theme in Owlboy"](https://gamedeveloper.com/art/using-graphics-to-express-character-and-theme-in-i-owlboy-i-) [snippet]; [GOG interview](https://www.gog.com/en/news/read_about_the_future_of_pixel_art_according_to_the_creators_of_owlboy) [snippet]
- **Into the Breach** (Subset Games): Justin Ma said they would "sacrifice cool ideas for the sake of clarity every time". The game shows the player exactly what every enemy will do next. Pixel artist Polina Hristova assisted Ma on art. — [Game Developer: ITB dev on UI design](https://gamedeveloper.com/design/-i-into-the-breach-i-dev-on-ui-design-sacrifice-cool-ideas-for-the-sake-of-clarity-every-time-) [snippet]; [Wikipedia: Into the Breach](https://en.wikipedia.org/wiki/Into_the_Breach) [snippet]
- **Octopath Traveler (HD-2D)**: SNES-style 2D character sprites sit in polygonal 3D environments with HD lighting and effects. Character and background pixel density were deliberately kept matched (see Q1). — [Unreal Engine spotlight](https://www.unrealengine.com/en-US/spotlights/octopath-traveler-s-hd-2d-art-style-and-story-make-for-a-jrpg-dream-come-true) [snippet]; [Unreal Engine OT2 interview](https://www.unrealengine.com/developer-interviews/octopath-traveler-ii-builds-a-bigger-bolder-world-in-its-stunning-hd-2d-style) [snippet]
- **Sea of Stars** (Sabotage): its sprites are animated more smoothly and lit dynamically beyond what '90s hardware allowed. Creative director Thierry Boulanger notes players read **enemy attack animations** to time blocks, so animation is a gameplay telegraph. — [Nintendo Life hands-on](https://www.nintendolife.com/news/2020/03/hands_on_first_impressions_of_sea_of_stars_the_next_project_from_the_messenger_dev_sabotage) [snippet]
- **Shovel Knight**: built within NES-style constraints, with deliberate palette exceptions (see Q1). — [Yacht Club blog](https://www.yachtclubgames.com/blog/breaking-the-nes/) [snippet]
- **Liberated Pixel Cup / Universal LPC**, an open standard for a reusable layered RPG character:
  - Default frame **64×64**.
  - Weapon and tool animations use oversize frames of **128 px** (slash_128, thrust_128, tool_axe…) or **192 px** (slash_oversize, tool_whip).
  - The original LPC animation set was spellcast, slash, thrust, walk, shoot and hurt. "LPC Revised" introduced "smaller heads" and a new colour palette.
  - Source: [ULPC generator README](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator/blob/master/README.md) [primary]
- **Final Fantasy Tactics**: a hobbyist describes FFT characters with "huge eyes and no mouths and tall heads". — [PixelJoint thread](https://pixeljoint.com/forum/printer_friendly_posts.asp?TID=16229) [snippet]. A search summary also claimed FFT units are 3D models. That contradicts the common understanding that FFT uses 2D sprites on 3D maps, and I could not verify either claim. Treat both as unverified.
- **King God Castle** (AWESOMEPIECE): listed in the Strategy category, about 5.2M installs per a third-party tracker, and described as having "pixel heroes". No source describes its sprite sizes, proportions or pipeline. — [App Store listing](https://apps.apple.com/app/id1526791430) [snippet]; [AppGoblin](https://appgoblin.info/apps/com.awesomepiece.castle) [snippet]

### Inferences
These capability tiers are practitioner consensus plus my own judgement, not sourced:
- **16×16**: a silhouette, 1–2 dominant colours, a weapon readable only as a 1–2 px line, no facial expression beyond eye dots. Class must come from silhouette (hat shape, cape, shield blob) and hue. Good for mobs and icons.
- **24×24 / 16×24**: the classic SNES RPG field size (verified FF 16×24). Room for a hairstyle, a readable weapon, 2–3 tone shading and a 2-head chibi body. A large, varied roster is still cheap to produce and animate.
- **32×32**: room for distinct headgear, weapon type (sword vs axe vs staff head), shield emblem, 3–4 tone ramps with selout, and a readable idle "breathing" bob and weapon swing. The best balance for 10–20 simultaneous units on a phone.
- **48×48**: personality in posture and face (eyebrows, mouth hints), layered equipment, larger weapon arcs. Animation cost rises roughly with area, about 2.25× the pixels of 32×32.
- **64×64 and up** (LPC standard, bosses, portraits): near-realistic proportions are possible, but each frame costs much more and units start to crowd a phone screen.
- **Chibi proportions**: about 2–2.5 heads tall. They maximise readable face and headgear area at small sizes; the head can take about 40–50% of sprite height. This is why SNES/GBA RPGs and most mobile pixel RPGs use them. Taller proportions (3–4+ heads) suit 48 px and above. I found no fetched source giving exact head-to-body ratios for named games. LPC Revised's move to "smaller heads" (verified above) shows the trade-off runs both ways.
- **Communicating class and abilities in tiny sprites**:
  - Reserve one exaggerated "class signifier" per unit (oversized weapon, hat silhouette, cape colour).
  - Assign each class or faction a hue family.
  - Express abilities with VFX and one-frame poses rather than costume detail.
  - Use gameplay-linked colour, as Celeste does, for status, for example a glowing weapon when ultimate is charged.

### Gaps
- No verified sprite dimensions for: Madeline (Celeste), Octopath characters, Hyper Light Drifter's Drifter, Into the Breach mechs, Dead Cells' Beheaded, Eastward, Blasphemous, Sea of Stars, Moonlighter, Wargroove, Chained Echoes, Soul Knight, Guardian Tales, Kingdom Two Crowns, King God Castle.
- I found no primary artist commentary on Wargroove, Chained Echoes, Soul Knight, Guardian Tales or Kingdom Two Crowns before the search budget ran out. A possible lead is the 80.lv article "Moonlighter: building pixel art & preparing for Switch" (https://80.lv/articles/moonlighter-building-pixel-art-preparing-for-switch/), which was found but not read.
- No sourced head-to-body ratios for specific titles.

---

## 3. Animation: frame counts, timing, principles, hit reactions, status effects, layering and palette swaps

### Takeaway
Pixel-game animation uses few frames with **variable per-frame durations**. Typical budgets:
- Idle: 2–6 frames, slow.
- Walk: 4–8 frames at about 80–120 ms each.
- Attack: 3–8 frames, with long anticipation and impact holds and a very short strike.
- Hit flash: 1–2 frames.

Professional pipelines key the pose-to-pose "golden" frames first and add in-betweens only where needed (Dead Cells). Equipment is layered as anchored paper-doll parts. Colour variants are palette swaps driven by indexed colour or lookup tables.

### Cited Findings
**Frame budgets and timing (community rules of thumb)**
- **Idle**: 2–4 frames in one guide, 2–6 frames at 4–8 fps in another. **Walk**: 4–8 frames, "4 for small sprites, 6–8 for 32×32+", and "8 or 6 frames" is economical for most pixel games. **Attack**: 3–6 frames (wind-up, strike, recovery) or 4–8. — [dev.to "How many frames does a sprite animation need?"](https://dev.to/nitin_808a59e08de0d0385ab/how-many-frames-does-a-sprite-animation-need-24k9) [snippet]; [sprite-ai blog](https://www.sprite-ai.art/blog/sprite-animation-frames) [snippet]; [pixelsrc book "The Animator"](https://scbrown.github.io/pixelsrc/book/personas/animator.html) [snippet]
- **Per-frame timing**:
  - Attacks and impacts: about 50–80 ms per frame.
  - Walk: about 80–120 ms; run: about 60–80 ms.
  - Idle: about 150–250 ms. One example uses 750 ms per frame for idle.
  - A widely used sprite-sheet reference uses **75 ms per frame** for cast, walk, thrust, slash and hurt.
  - Sources: [pixelsrc book](https://scbrown.github.io/pixelsrc/book/personas/animator.html) [snippet]; [skills.sh pixel-art-animator](https://skills.sh/willibrandon/pixel-plugin/pixel-art-animator) [snippet]; [sprite-ai blog](https://www.sprite-ai.art/blog/sprite-animation-frames) [snippet]
- **Weight comes from holds**: hold the wind-up and impact frames longer and keep the action frame brief. — [sprite-ai blog](https://www.sprite-ai.art/blog/sprite-animation-frames) [snippet]
- **Smear and impact frames**: smear frames are elongated in-betweens that "work well at low resolution". Hit flashes should be 1–2 frames of high-contrast flash. — [GamineAI "Pixel art combat FX: hitstop, smear frames, impact timing" (Apr 2026)](https://gamineai.com/blog/pixel-art-combat-fx-hitstop-smear-frames-impact-timing-2026) [snippet]. Slynyrd's "Pixelblog 53 – Punches and Kicks" breaks strikes into frames and keeps smear-frame colours simple for legibility. — [Slynyrd blog index](https://slynyrd.com/blog) [snippet]. In general animation, impact frames are stylised, often monochrome, frames inserted at dynamic moments. — [80.lv on impact frames](https://80.lv/articles/learn-how-to-add-accents-to-your-animations-with-impact-frames) [snippet]

**Pose-to-pose and in-betweening (Dead Cells)**
- Thomas Vasseur (Motion Twin) designed Dead Cells' animations "like 2D animations, on key frames. Once, and only once, the animation is convincing and correctly timed with the least amount of frames possible, I add interpolation frames before or after the key frames." The motive was bandwidth: "we had to find a pipeline that could give us great looking pixel art". — [Vasseur's article, mirrored on JIKGuard](https://www.jikguard.com/news/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-dead-cells) [snippet]; original: [Game Developer](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-) (blocked)
- Characters and monsters were modelled and animated in **3ds Max** and rendered to 2D sprites with an in-house tool. Adding equipment such as armour to an existing 3D model was far easier than redrawing 2D frames. — [80.lv Motion Twin interview](https://80.lv/articles/interview-with-the-developers-of-dead-cells) [snippet]; [80.lv Dead Cells character art pipeline case study](https://80.lv/articles/case-study-dead-cells-character-art-pipeline) [snippet]
- **Blasphemous** (The Game Kitchen) uses the hand-made alternative:
  - Start from a standing pose and pixel it.
  - The art director makes quick black-pencil animation drafts.
  - Once timing and expression work, animators finish "pixel by pixel, handcrafted".
  - Fully animated pixel cutscenes were rare because they are "really crazy" to produce.
  - Sources: [Blasphemous BackerKit update](https://blasphemous.backerkit.com/hosted_preorders/project_updates?page=7) [snippet]; [Hollywood Reporter](https://www.hollywoodreporter.com/heat-vision/blasphemous-designer-purist-approach-games-pixel-art-style-1238370) [snippet]

**Variable per-frame durations (tool support)**
- Aseprite stores a duration per frame. The Lua API exposes `frame.duration` in seconds ("0.3333 means… 1/3 of a second"). The JSON sprite-sheet export writes a per-frame `"duration"` (milliseconds) and a `frameTags` array with `name`, `from`, `to`, `direction`, `color` and `repeat`. Tags support FORWARD, REVERSE, PING_PONG and PING_PONG_REVERSE. — [Aseprite API: Frame](https://github.com/aseprite/api/blob/main/api/frame.md) [primary]; [Aseprite API: Tag](https://github.com/aseprite/api/blob/main/api/tag.md) [primary]; [Aseprite doc_exporter.cpp](https://github.com/aseprite/aseprite/blob/main/src/app/doc_exporter.cpp) [primary]

**Layered / paper-doll composition**
- A composable-sprite design (Sigil of Kings devblog):
  - Parent–child layer hierarchy: head with eyes, mouth, hair and helmet; body with cape and hands; feet.
  - Equipment attaches through 2D pixel anchor coordinates that are **animated per frame**.
  - A special magenta marker colour lets one hair sprite be recoloured many ways.
  - Source: [Sigil of Kings "Composable sprites part 2"](https://byte-arcane.github.io/sigil-of-kings-website/2022/02/03/composable-sprites-part-2) [snippet]
- The ULPC generator stacks asset categories as layers with a **z-position per layer**, and generated z-position CSVs are part of the build. Users report z-order bugs, for example a tabard drawn behind armour, which shows z-order must be specified per animation and direction. — [ULPC README](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator/blob/master/README.md) [primary]; [OpenGameArt LPC generator thread](https://lpc.opengameart.org/comment/80532) [snippet]
- Dead Cells' 3D route makes equipment variants cheap to add (see above).

**Palette swaps for variants, teams and rarity**
- The classic method is an indexed-colour sprite plus a palette. Modern RGBA PNGs need a shader:
  - Map reference colours to replacement colours through a swap texture (one per palette). A transparent entry leaves the colour unchanged.
  - Or store palette *indices* in the texture so the palette texture can change at run time.
  - Sources: [Envato Tuts+ palette-swap shader tutorial](https://code.tutsplus.com/how-to-use-a-shader-to-dynamically-swap-a-sprites-colors--cms-25129t) [snippet]; [pvigier "Palette swapping with shaders"](https://pvigier.github.io/2019/10/06/palette-swapping-with-shaders.html) [snippet]; Godot asset ["Palette swap shader with animation support"](https://godotengine.org/asset-library/asset/1122) [snippet]
- A GameMaker palette tool reports that indexed sprites plus palettes used about one-sixth of the storage of separate per-palette sprites. — [Lorikeet (itch.io)](https://dragonite.itch.io/lorikeet) [snippet]
- ULPC's recolour system keeps **one source image plus a palette JSON** per item. It recolours on the GPU through a WebGL fragment shader with the palette encoded as a texture, at about 90–120 ms versus 190–230 ms on CPU per preview sheet. Matching tolerance is ±1 per RGB channel, and palettes hold 1–32 colours per variant. — [ULPC README](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator/blob/master/README.md) [primary]; [ULPC PALETTE_RECOLOR_GUIDE.md](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator/blob/master/PALETTE_RECOLOR_GUIDE.md) [primary]

### Inferences
These are practitioner conventions plus my own synthesis. The fetched sources cover only parts of them.

**Starting frame budget for an autobattler unit at 32×32** (sum of frames per unit, one facing plus horizontal flip):

| Animation | Frames | Timing |
|---|---|---|
| Idle | 4 | 150–200 ms each; or 2 frames ping-pong |
| Move | 4–6 | 80–100 ms |
| Attack | 5–7 | anticipation 2 frames held 120–200 ms total → strike/smear 1 frame at 50–60 ms → impact hold 1 frame at 100–150 ms → recovery 1–2 frames at 80 ms |
| Cast | 6–8 | including a 2–3 frame loop held while VFX play |
| Hit | 2 | 1 white or red flash frame, 1 recoil frame |
| Death | 5–8 | ending on a held corpse or dissolve frame |
| Victory | 4–6 | loopable |

That totals roughly 30–45 frames per unit. Using one facing direction plus horizontal flip, as side-view autobattlers commonly do, halves the cost compared with 4-direction sprites.

**Timing at 60 Hz**
- "12 fps" means about 83 ms per frame (5 game ticks).
- "On twos" at 24 fps is the same 12 fps.
- Pixel games usually author durations per frame in ms rather than at a global fps. Snap durations to multiples of 16.67 ms (one 60 Hz tick) so timing is identical on every device.

**Readable principles at small sizes**
- Squash and stretch: 1–2 px of vertical change on the body during idle breathing or landing.
- Anticipation: a 1–3 px pull-back.
- Secondary motion: hair, cape or plume lag by one frame.
- Smear: a single frame where the weapon becomes a solid arc in a light ramp colour.
- Hit-stop: freeze both attacker and target for 2–6 ticks on impact. This is a common game-feel technique, sourced here only via the GamineAI snippet.

**Status effects**
Avoid redrawing frames. Use:
- run-time tints or palette swaps (poison green, burn orange, freeze blue cast);
- small looping overlay sprites above the head (stun stars, sleep "z");
- under-foot rings or auras;
- frame-rate changes (slow = longer durations, haste = shorter).
Each effect needs a unique silhouette or icon as well as a colour, for colour-blind readability.

**Variants, teams and rarity via palette swap**
- Author units in indexed colour against a master palette.
- Reserve specific ramps as "swap slots", such as primary cloth, secondary cloth, metal trim and glow.
- Teams: a swap of the primary cloth ramp, or better an outline or under-foot ring colour, so team reads even when cloth colours collide.
- Rarity: a metal-trim swap (iron → silver → gold) plus a glow or aura ramp, rather than separate art.

### Gaps
- I could not access Pedro Medeiros' (saint11) animation tutorials or GDC talks on pixel animation, so there is no first-hand professional frame-count data from named commercial titles.
- I could not verify Dead Cells' render settings (render resolution, AA off, normal maps) from a primary source.
- No source in this session for status-effect visualization conventions in tactics or autobattler games.

---

## 4. Pixel-art VFX: slashes, impacts, projectiles, magic; readability and density consistency

### Takeaway
Very little VFX-specific material was retrievable. The sourced points are:
- Keep VFX on the same pixel grid as the sprites (no mixels; the small-emote exception is contested).
- Use short, high-contrast impact flashes (1–2 frames).
- Keep smear and slash colours simple for legibility.
- Draw VFX from the same palette.

Most of the actionable VFX guidance below is inference.

### Cited Findings
- Hit flashes should be 1–2 frames of high-contrast flash, and smears are elongated in-betweens suited to low resolution. — [GamineAI combat FX guide](https://gamineai.com/blog/pixel-art-combat-fx-hitstop-smear-frames-impact-timing-2026) [snippet]
- Smear frames keep colours simple for legibility (Punches and Kicks breakdown). — [Slynyrd blog index](https://slynyrd.com/blog) [snippet]
- Mixels for VFX and emotes are the one commonly tolerated exception, though some argue even this breaks the pixel-art feel. — [itch.io post](https://itch.io/post/15078117) [snippet]
- Eastward pairs 2D pixel art with complex real-time lighting, which gives a "glowing" look; Pixpil built it on an in-house engine plus the open-source MOAI framework. Sea of Stars likewise adds dynamic lighting to sprites. — [80.lv Eastward](https://80.lv/articles/eastward-charming-chinese-pixel-art-adventure) [snippet]; [Red Bull Eastward interview](https://www.redbull.com/my-en/eastward-interview) [snippet]; [Nintendo Life Sea of Stars](https://www.nintendolife.com/news/2020/03/hands_on_first_impressions_of_sea_of_stars_the_next_project_from_the_messenger_dev_sabotage) [snippet]
- Godot's pixel-art guidance: the `viewport` stretch mode renders at low resolution then upscales, so effects and rotations snap to the pixel grid. The `canvas_items` mode allows "sub-pixel" movement and rotation, which breaks strict pixel density. — [Godot docs: Multiple resolutions](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst) [primary]

### Inferences
These are my synthesis of standard practice, not sourced here.
- **Palette-limited VFX ramps.** Give each element one 3–5 colour ramp from the master palette that ends in white or near-white: fire (dark red → orange → yellow → white), ice (navy → cyan → white), arcane (purple → magenta → pink-white), holy (gold → cream → white), poison (dark green → lime). The brightest pixels should be the VFX core, brighter than anything on unit bodies, so effects always win the value contrast.
- **Slash arcs.** One smear or arc frame at full brightness, then 2–3 dissipating frames where the arc thins and breaks into dashes and drops one ramp step per frame. Total about 4 frames at 40–60 ms. Arc thickness about 2–4 px at a 32 px unit scale.
- **Impacts.** Frame 1 is a solid bright starburst or a white silhouette flash of the target. Frames 2–3 are an expanding ring or spark lines. Frame 4 is sparse 1-px debris that fades out by palette step, not by alpha. Add 1–3 px of screen shake or target knockback for weight.
- **Projectiles.** A 3–6 px bright core with a 1-px darker rim, plus a 2–4 frame trail made of the previous positions in dimmer ramp steps. Snap to integer positions.
- **Readability with 10–20 units.**
  - Cap VFX screen coverage: big AoE effects get one frame of full coverage, then thin out.
  - Telegraph enemy AoE with a ground decal that animates in before the hit, following Into the Breach's "show what will happen" philosophy.
  - Use additive glow sparingly, because additive blending creates off-palette colours. If used, apply it through a palette-quantising post-shader or not at all.
  - Avoid alpha fades on pixel effects. Use dithered dissolves (ordered dither masks) or ramp stepping, which keeps the palette discipline intact.
- **Particles.** Particle systems are fine if each particle is a pre-drawn 1×1 to 3×3 sprite in palette colours, positions snap to the virtual pixel grid, and size changes happen by swapping sprite frames, not by scaling.

### Gaps
- No artist-authored pixel VFX tutorial (for example by Pedro Medeiros, Slynyrd or a GDC talk) could be read in this session. Frame counts for VFX above are unsourced conventions.

---

## 5. Tools: Aseprite, LibreSprite, Pixelorama, Krita, Pyxel Edit, GraphicsGale, Photoshop

### Takeaway
**Aseprite** remains the de facto professional choice for sprite animation. It costs $19.99 on Steam; v1.3.18 appears in a June 2026 blog post. Its strengths are layers and frames, tags, slices, onion skin, indexed mode, tilemaps, a Lua API and a full CLI that exports packed sheets plus JSON. Its licence is proprietary but source-available.

**Pixelorama**, free and open source on Godot, is now a credible free alternative. It is actively developed (v1.2.4, 2026-11-03), with tilemaps, layer FX, indexed mode, CLI export and `.aseprite` export.

**LibreSprite** is the GPLv2 fork of 2016-era Aseprite. **Pyxel Edit** (about $9) is tile-focused. **GraphicsGale** is free but Windows-only and legacy. **Krita and Photoshop** can do pixel work but lack sprite-pipeline features; no fetched sources here.

### Cited Findings
**Aseprite**
- Features listed in the README:
  - layers and frames as separate concepts;
  - RGBA, Indexed (palettes up to 256 colours) and Grayscale modes;
  - onion skinning and real-time preview;
  - export to sprite sheets, GIF and PNG sequences;
  - layer groups and reference layers;
  - Pixel Perfect freehand, Shading ink, custom brushes, outlines, wide pixels, symmetry and gradients;
  - tiled mode;
  - Lua scripting and a CLI.
  - Source: [Aseprite README](https://github.com/aseprite/aseprite/blob/main/README.md) [primary]
- Licence: source code and official binaries are under the Aseprite EULA (Igara Studio S.A.). You "may only compile and modify the source code… for your own personal purpose or to propose a contribution", and may not redistribute. Some modules are MIT. An educational licence exists, and Steam copies fall under the Steam Subscriber Agreement. — [Aseprite README](https://github.com/aseprite/aseprite/blob/main/README.md) [primary]; [Aseprite EULA.txt](https://github.com/aseprite/aseprite/blob/main/EULA.txt) [primary]
- Price and version: Steam lists $19.99, with a sale low of $13.99 in March 2026 and an all-time low of $9.99 in Feb 2024. The Aseprite blog lists **v1.3.18**, with a post dated 2026-06-30. The official release-notes page last showed v1.3.17-beta2 (Dec 2025), so it may lag. — [Steambase price tracker](https://steambase.io/games/aseprite/price) [snippet]; [SteamDB](https://steamdb.info/app/431730) [snippet]; [Aseprite blog](https://blog.aseprite.org/2026/06/30/new-website-account/) [snippet]. The Lua API changelog's latest section is v1.3.17, which sets `app.apiVersion` to 39. — [aseprite/api Changes.md](https://github.com/aseprite/api/blob/main/Changes.md) [primary]
- **Scripting**: Lua scripting has existed since v1.2.10. You can transform the active sprite, create sprites, open files, `Sprite:saveCopyAs()`, build dialogs, and add menu commands through plugins. Constants include `SpriteSheetType` (HORIZONTAL, VERTICAL, ROWS, COLUMNS, PACKED) and `SpriteSheetDataFormat`. There is also a `json` module. — [aseprite/api README](https://github.com/aseprite/api/blob/main/README.md) [primary]; [SpriteSheetType](https://github.com/aseprite/api/blob/main/api/spritesheettype.md) [primary]
- **CLI options** (from source):

  | Area | Options |
  |---|---|
  | Running | `--batch`/`-b` (no UI), `--shell`, `--preview`, `--verbose`, `--debug`, `--version` |
  | Saving and conversion | `--save-as <filename>`, `--palette <filename>`, `--scale <factor>`, `--dithering-algorithm`, `--dithering-matrix`, `--color-mode <mode>`, `--shrink-to w,h` |
  | Sheet and data output | `--data <file.json>`, `--format` (json-hash, json-array), `--sheet <file.png>`, `--sheet-type` / `--sheet-pack`, `--sheet-width`, `--sheet-height`, `--power-of-two-size`, `--sheet-columns`, `--sheet-rows` |
  | Splitting | `--split-layers`, `--split-tags`, `--split-slices`, `--split-grid` |
  | Selecting content | `--layer`, `--all-layers`, `--ignore-layer`, `--tag <name>`, `--play-subtags`, `--frame-range from,to`, `--ignore-empty`, `--merge-duplicates` |
  | Padding and trimming | `--border-padding`, `--shape-padding`, `--inner-padding`, `--trim`, `--trim-sprite`, `--trim-by-grid`, `--extrude`, `--crop x,y,w,h`, `--slice <name>` |
  | Naming | `--filename-format <fmt>`, `--tagname-format <fmt>` |
  | Scripts | `--script <file>`, `--script-param name=value` |
  | Listing / JSON content | `--list-layers`, `--list-layer-hierarchy`, `--list-tags`, `--list-slices` |
  | Other | `--oneframe`, `--export-tileset` |

  Source: [app_options.cpp](https://github.com/aseprite/aseprite/blob/main/src/app/cli/app_options.cpp) [primary]
- Filename-format placeholders include `{title}`, `{name}`, `{path}`, `{extension}`, `{layer}`, `{group}`, `{tag}`, `{innertag}`, `{outertag}`, `{frame}`, `{frame1}`, `{tagframe}`, `{slice}` and `{duration}`. — [filename_formatter.cpp](https://github.com/aseprite/aseprite/blob/main/src/app/filename_formatter.cpp) [primary]
- **JSON sheet format**, as written by the exporter (`json-hash` keys frames by filename; `json-array` lists them):
  - Each frame has `filename`, `frame {x,y,w,h}`, `rotated` (always false), `trimmed`, `spriteSourceSize`, `sourceSize` and `duration` (ms).
  - `meta` has `app`, `version`, `image`, `format` ("RGBA8888" or "I8"), `size`, `scale`, and optional `frameTags` (name, from, to, direction, color, repeat, data).
  - Optional `layers` carry name, group, opacity, blendMode, color and per-cel data.
  - Optional `slices` carry name, color, data and `keys` with frame, bounds, 9-slice `center` and `pivot`.
  - Source: [doc_exporter.cpp](https://github.com/aseprite/aseprite/blob/main/src/app/doc_exporter.cpp) [primary]
- Aseprite bundles palettes, including DB16/DB32 and hardware palettes (NES, Game Boy, C64, CGA, MSX, ZX Spectrum and others), as extensions. — [hardware-palettes manifest](https://github.com/aseprite/aseprite/blob/main/data/extensions/hardware-palettes/package.json) [primary]
- Ecosystem extensions include OKShift (OKLab hue shift), "Hue Shifted Color Ramp" and AsepriteOkHsl. — [OKShift README](https://github.com/WangleLine/OKShift) [primary]

**LibreSprite**
- LibreSprite is free and open source under **GPLv2**. It was forked from the last GPL commit of Aseprite after Aseprite went proprietary on 2016-08-26, and is now developed independently. It has real-time preview, onion skin, layers and frames, palettes, tiled mode and shading mode. Builds exist for Linux, macOS, Windows and **Android**. — [LibreSprite README](https://github.com/LibreSprite/LibreSprite/blob/master/README.md) [primary]

**Pixelorama**
- Pixelorama is open source and built on Godot (the current build requires Godot 4.7.1). Features listed in the README:
  - timeline with layers and frames, onion skin, frame tags and audio sync;
  - pixel-perfect lines and indexed mode;
  - pixel-art rotation and scaling algorithms (cleanEdge, OmniScale, rotxel);
  - rectangular, isometric and hexagonal tilemap layers;
  - clipping masks and non-destructive layer effects (outline, gradient map, drop shadow);
  - palettes and auto-backups;
  - export to PNG, APNG, sprite sheets, GIF and video.
  - Distribution: Steam, itch.io, web build, Flathub and WinGet.
  - Source: [Pixelorama README](https://github.com/Orama-Interactive/Pixelorama/blob/master/README.md) [primary]
- Recent releases: v1.2 (2026-07-29) through **v1.2.4 (2026-11-03)**. They added autotiling for tilemap layers, export as Aseprite files (v1.2.2), animatable layer-effect properties with keyframes, and CLI export fixes (`-o/--output`, plus GIF/APNG export from the CLI). — [Pixelorama CHANGELOG](https://github.com/Orama-Interactive/Pixelorama/blob/master/CHANGELOG.md) [primary]

**Pyxel Edit, GraphicsGale and others**
- **Pyxel Edit**: about $9 for the release build, with an older beta free. It is best known for tileset creation; it handles animation but "leans toward tiles". — [PC Gamer "best pixel art tools"](https://www.pcgamer.com/best-pixel-art-maker-tools/) [snippet]; [Elegant Themes](https://www.elegantthemes.com/blog/design/best-pixel-art-makers-for-designers-and-artists) [snippet]
- **GraphicsGale**: free and Windows-only. — [PC Gamer](https://www.pcgamer.com/best-pixel-art-maker-tools/) [snippet]; [Concept Art Empire](https://conceptartempire.com/pixel-art-software/) [snippet]
- AlternativeTo lists Pixelorama and PixiEditor as free open-source alternatives to Pyxel Edit. — [AlternativeTo](https://alternativeto.net/software/pyxel-edit) [snippet]

### Inferences
- **Recommendation for a small team**:
  - Aseprite as the authoring standard. It is cheap per seat, and its CLI and Lua API make it the backbone of an automated export pipeline. Its JSON format (per-frame duration, tags, slices with pivots) maps directly onto engine animation clips and hit or anchor points.
  - Pixelorama as the zero-cost seat for contributors, since it can now export `.aseprite` files.
  - Aseprite's EULA forbids redistributing self-compiled builds. Every seat that uses CI or the CLI needs a licence. Check whether a headless CI runner needs its own licence; this was not verified.
- **Krita** (free, GPL) and **Photoshop** (subscription) work for concept paint-overs and pixel-art illustration if nearest-neighbour resampling, a pencil or aliased brush, and a pixel grid are configured. They lack tags, sprite-sheet JSON export and indexed-palette workflows comparable to Aseprite's. This is an inference; their docs were not fetched.

### Gaps
- Not verified this session: Krita and Photoshop pixel-art feature docs; Pyxel Edit's current price and status; GraphicsGale's maintenance status; the LibreSprite release cadence and scripting (its README does not mention scripting); Pixelorama's exact CLI flag list and licence text (the README shows a licence badge; it is commonly MIT, but I did not verify it).

---

## 6. Programmatic generation: code-authored sprites at professional quality

### Takeaway
Purely random generators (Bollinger masks, cellular automata) produce *coherent-looking noise*. They work for spaceships, icons and filler monsters, but not for a hero roster. Professional-quality programmatic art comes from **constraint + authorship**:
- hand-designed part templates, stored as palette-indexed character grids or semantic regions;
- a fixed hue-shifted master palette;
- deterministic layering with per-frame anchors;
- automatic post-passes: outline or selout, orphan-pixel and banding checks;
- palette swaps for variety.

Code assembles and varies hand-made parts; it should not invent shapes from noise.

### Cited Findings
**Dave Bollinger's mask algorithm (pixel robots and spaceships), as ported by zfedoran's pixel-sprite-generator**
- A 2D mask template has cell values:
  - `-1` = always border (black);
  - `0` = empty;
  - `1` = random empty/body;
  - `2` = random border/body.
- The randomised template is mirrored on X and/or Y. Edges are then generated around the body cells, and the result is coloured.
- Options: `colored`, `edgeBrightness` (default 0.3), `colorVariations` (0.2), `brightnessNoise` (0.3), `saturation` (0.5).
- Source code: [pixel-sprite-generator.js](https://github.com/zfedoran/pixel-sprite-generator/blob/master/pixel-sprite-generator.js) [primary]. Description and ports (Rust, C#, Unity, Python and others): [pixel-sprite-generator README](https://github.com/zfedoran/pixel-sprite-generator/blob/master/README.md) [primary]; Bollinger's original pages survive only on archive.org (linked from the README).

**Sprator (cellular automaton)**
1. Generate 4×8 white noise.
2. Apply rules: a live cell with 2–3 neighbours survives; a dead cell with ≤1 live neighbours becomes live; all others die or stay dead.
3. Repeat several steps.
4. Mirror and add an outline.

Source: [Sprator README](https://github.com/yurkth/sprator/blob/master/README.md) [primary]

**Layered and part-based generation**
- A 2016 GenJam procedural-sprite project split sprites into eight part groups (torso, head, helmet, hair, weapon…). It coloured them from a palette of material ramps (metal, leather, hair). — [Game Developer "Gen Jam 2016: procedurally generating sprites"](https://www.gamedeveloper.com/programming/gen-jam-2016-procedurally-generating-sprites) [snippet]
- Paper-doll systems: see the parent-child anchors and magenta recolour marker in Q3. — [Sigil of Kings devblog](https://byte-arcane.github.io/sigil-of-kings-website/2022/02/03/composable-sprites-part-2) [snippet]. Also ULPC: z-positioned layers, per-item palette JSON and a GPU recolour, with licence obligations (CC0, CC-BY, CC-BY-SA, OGA-BY, GPL; a credits CSV is generated). — [ULPC README](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator/blob/master/README.md) [primary]

**Text and semantic formats for code- or AI-authored sprites**
- `pixelsrc` is "a semantic, human-readable text format for defining pixel art", in JSON5:
  - A named palette maps tokens to colours.
  - A sprite has a size and regions defined by shapes (`stroke`, `rect`, `circle`, `fill: "inside(outline)"`, explicit `points`).
  - A "lenient by default" compiler offers a strict mode for CI.
  - It is distributed as a Rust crate, CLI `pxl` and WASM, under the MIT licence.
  - Source: [pixelsrc README](https://github.com/scbrown/pixelsrc/blob/main/README.md) [primary]. It also offers an `apply_selout` transform: [docs.rs](https://docs.rs/pixelsrc/latest/pixelsrc/transforms/fn.apply_selout.html) [snippet]

**Palette construction in code**
- PalettePainter (Slynyrd principles: hue-shift, hue-spectrum, desaturate and ramp-count parameters), RampenSau (hue cycling plus easing in LCH and other spaces), and OKShift (OKLab brightness-preserving hue shift). — [PalettePainter](https://github.com/chickensoft-games/PalettePainter) [primary]; [RampenSau](https://github.com/meodai/rampensau) [primary]; [OKShift](https://github.com/WangleLine/OKShift) [primary]
- Automated quality checks are a research topic. TU Delft's "Pixel Fixer" formalises banding detection, which shows that rules like "no banding" can be machine-checked. — [TU Delft repository](https://repository.tudelft.nl/record/uuid:b3c91b18-d9e8-48e0-91ce-8afafd2439d8) [snippet]

### Inferences
This is my synthesis: a recommended architecture for code-generated PNGs in this project.

1. **Master palette as data.** Define about 8–12 ramps of 4–6 colours each, hue-shifted (about 15–20° across a ramp per Slynyrd; darks toward blue or purple, lights toward yellow). Build them with OKLab or OKLCH so that equal steps are perceptually equal. Store them as JSON, for example `{ramp: "skin", colors: [...]}`. Every generated pixel must be a palette index; a CI check rejects off-palette colours.
2. **Hand-authored parts as character grids.** Each body, head, hair, armour, weapon and accessory part is a small ASCII grid. One character equals one semantic slot, for example `.`=transparent, `o`=outline, `1`–`4`=primary ramp steps dark→light, `a`/`b`=accent ramp, `s`=skin ramp, `m`=metal ramp. Slots resolve to ramp indices at render time, which makes palette swaps, team colours and rarity trim free. Grids are designed by an artist or art director, pixel by pixel, with real cluster and selout decisions. Code must not invent them.
3. **Skeleton and anchors per frame.** Each animation frame of the base body defines anchor points (head, hand_main, hand_off, back, feet) and a z-order list. Parts are pasted at anchors with integer offsets and no rotation. Rotation destroys pixel clusters, so rotated weapons need hand-drawn variants at 0°, 45° and 90°, or a pixel-art rotation algorithm such as cleanEdge or rotxel (in Pixelorama) followed by manual cleanup.
4. **Post-passes, run in this order**:
   1. Composite.
   2. Remove interior outline pixels where parts overlap.
   3. External outline pass: 4-neighbour dilation of the alpha mask, coloured per adjacent fill ramp's darkest step. That gives selout; pure black stays as an option.
   4. Optional light-direction pass: on the top-left boundary of each part's interior, shift one ramp step lighter; on the bottom-right, one step darker. It only changes indices along the existing ramp.
   5. Orphan-pixel lint: flag any isolated pixel whose 8 neighbours all differ, unless a whitelist tags it as deliberate (for example eyes).
   6. Banding lint: flag parallel same-length runs using the TU Delft definition.
   7. Silhouette check: render the alpha mask as solid black at 1× and compare against the other classes using an overlap or IoU metric, so classes stay distinguishable.
5. **Variety budget.** Get variety from combinatorics of hand-made parts × palette swaps, not from random pixels. Use Bollinger or cellular-automaton methods only where noise is acceptable: procedural icons, rubble, star fields, background props, "corrupted" enemy variants. Seed them deterministically and always run them through the same palette and outline passes.
6. **What separates intentional programmatic art from noise**:
   - Every pixel belongs to a cluster that represents a form.
   - The palette is curated and ramped.
   - Light direction is consistent.
   - Outlines are deliberate.
   - Symmetry is broken on purpose. Fully mirrored sprites look robotic; real characters face 3/4 and carry asymmetric equipment.
   - All output sits on one grid, at one scale.
   - Animation is authored pose-to-pose.
   Random generators fail on cluster intent and asymmetry.
7. **Known limitations.**
   - Grids are slow to author for large sprites; consider authoring in Aseprite and exporting to grids or indices with a Lua script.
   - Anchored parts can't express overlapping deformation, such as a cape wrapping around the body. Those need per-frame hand-drawn parts.
   - Automated shading passes can't replace an artist's form shading at 32 px and above. Use them only to *nudge* hand-shaded parts.

### Gaps
- I could not read Bollinger's original write-up (archive.org was blocked), the GenJam article body, or any academic paper on procedural pixel *characters*. No sourced evaluation of output quality for any generator.

---

## 7. Production pipeline: from concept to engine, naming, atlases, QA

### Takeaway
A robust small-team pipeline runs:
1. Locked palette and scale spec.
2. Silhouette pass at 1×.
3. Base sprite with flats, light and selout.
4. Key poses, then timing, then in-betweens.
5. Tags and slices in Aseprite.
6. CLI batch export to packed sheets plus JSON.
7. Engine import that reads per-frame durations and pivots.
8. Automated lint plus a human 1×/target-scale review.

Most of this is inference, assembled from verified tool capabilities.

### Cited Findings
- Dead Cells' rule: get the animation "convincing and correctly timed with the least amount of frames possible" before adding in-betweens. — [Vasseur article mirror](https://www.jikguard.com/news/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-dead-cells) [snippet]
- Blasphemous' order: standing pose → pixelisation → rough pencil animation drafts → pixel-by-pixel finals. — [BackerKit update](https://blasphemous.backerkit.com/hosted_preorders/project_updates?page=7) [snippet]
- Cluster-sketching workflow: block large colour areas first, then refine. — [Pixel Grimoire #2](https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-2-bcd705cb04d7) [snippet]
- Aseprite's CLI supports what export automation needs: packed sheets, JSON with per-frame durations, tags, layers and slices with pivots, splitting by layer or tag, filename templates, trimming, padding, extrusion and script execution with parameters. — [app_options.cpp](https://github.com/aseprite/aseprite/blob/main/src/app/cli/app_options.cpp) [primary]; [doc_exporter.cpp](https://github.com/aseprite/aseprite/blob/main/src/app/doc_exporter.cpp) [primary]
- ULPC's build validates sources, regenerates a z-position CSV and a credits CSV, and enforces unit-test coverage on changed lines. This is an example of treating sprite assembly as tested code. — [ULPC README](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator/blob/master/README.md) [primary]

### Inferences
**Pipeline stages and deliverables** (my recommendation):
1. **Style bible.**
   - Virtual resolution and integer scale (see Q8).
   - Unit canvas (for example 32×32) with a ground-line or pivot row (for example y=29) and a maximum character height.
   - Light direction (top-left).
   - Outline rule: selout, with external outline 1 px, never 2 px.
   - Master palette (`.gpl`, `.ase` and JSON).
   - Ramp-slot conventions for swaps.
   - Forbidden list: no mixels, no non-integer scaling, no alpha gradients on units, no AA on outer silhouettes.
2. **Concept.** Rough or paint-over at any resolution. Then a **silhouette sheet**: all roster units as solid black shapes at 1× on one page, to confirm class distinctness.
3. **Base sprite.** Flats → light pass → selout → detail. Review at 1× and at target scale on an actual phone.
4. **Animation.** Key poses (anticipation, contact or impact, recovery) → timing using per-frame ms in Aseprite → in-betweens and smears → secondary motion.
5. **Tagging.** One `.aseprite` file per unit. Tags `idle`, `move`, `attack`, `cast`, `hit`, `death`, `victory`. Slices for `pivot` (feet), `hit_point` (where VFX and projectiles spawn), `head` (status icon anchor) and `weapon_tip`.
6. **Export.** For example, built only from verified option names:

   ```
   aseprite -b unit_knight.aseprite --sheet out/unit_knight.png --data out/unit_knight.json --format json-array --sheet-pack --list-tags --list-slices --trim --shape-padding 1 --filename-format "{title}_{tag}_{tagframe}"
   ```

   Then pack all units into atlases per screen or per battle.
7. **Naming.** Use lowercase snake case: `unit_<faction>_<class>_<variant>`, `vfx_<element>_<type>`, `ui_icon_<name>_16`. Tags use fixed verbs, and frames are numbered within tags.
8. **Automated QA**, as a CI script over exported PNGs:
   - all colours in the master palette (or in declared swap slots);
   - no semi-transparent pixels on units (alpha 0 or 255 only);
   - sprite fits the canvas and the pivot row;
   - no orphan pixels outside a whitelist;
   - outline continuity (every opaque edge pixel is an outline colour);
   - frame counts and durations per tag within spec (durations multiples of about 16–17 ms);
   - consistent canvas size per unit family;
   - an atlas texture-size budget.
9. **Human QA checklist**:
   - reads at 1× on a phone at arm's length;
   - silhouette is distinct from the other 19 units in a crowded battle screenshot;
   - team colour is readable;
   - light direction is consistent;
   - no pillow shading;
   - no jaggy curves on the main silhouette;
   - the attack's anticipation is legible enough to telegraph (Sea of Stars and Into the Breach principle);
   - effects don't hide unit identity.

### Gaps
- No sourced industry-standard naming or atlas convention was found. The conventions above are recommendations.

---

## 8. Recommended sprite dimensions for a portrait or landscape mobile autobattler (10–20 units, ~1080×2400 phone)

### Takeaway
I recommend:
- a **virtual canvas about 270 px wide in portrait** (1080 ÷ 4), with height expanding to about 600 px on 1080×2400, rendered with **integer scaling (×4 on 1080-wide phones)**;
- **32×32 unit cells**, with characters about 22–28 px tall in 2–2.5-head chibi proportions;
- **48×48 or 64×64** for bosses and large units;
- **16×16** for status and UI icons.

For a landscape layout, use the same 32×32 units on a canvas about 480–600 px wide (2400 ÷ 5 = 480, 2400 ÷ 4 = 600). Use 24×24 only if more than 20 units must fit, or the team is very small.

### Cited Findings
- Godot's guidance for pixel art:
  - "Most pixel art games use viewport sizes between 256×224 and 640×480".
  - 640×360 is a good baseline because it integer-scales to 720p, 1080p, 1440p and 4K without black bars.
  - Use `viewport` stretch mode, `keep` or `expand` aspect, and **integer stretch scale mode**, which has been available since Godot 4.2.
  - Integer mode rounds 2.5× down to 2×, "to prevent distortion when displaying pixel art".
  - With fractional scaling, "line widths… vary wildly" and checkerboards look uneven.
  - Example: a 640×360 base in a 1366×768 window shows at 1280×720 (×2) with black bars in integer mode.
  - Source: [Godot docs: Multiple resolutions](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst) [primary]
- Godot's mobile guidance:
  - Use `expand` aspect "to support multiple aspect ratios and make better use of tall smartphone displays (such as 18:9 or 19:9)".
  - For apps that support both portrait and landscape, use a **square** base resolution (for example 720×720) so the automatically chosen scale is similar in both orientations.
  - Consider a 4:3 base for tablets and foldables.
  - Source: [Godot docs](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst) [primary]
- Reference internal resolutions of acclaimed pixel games: Celeste **320×180** ([Reddit comment via mirror](https://axebps-redlib.hf.space/r/gamedev/comments/9a0cfr/how_is_the_hair_in_celeste_made/e4sgcdc/?context=3) [snippet]) and Hyper Light Drifter **480×270** ([GamingBolt](https://gamingbolt.com/our-game-is-480p-yeah-its-low-resolution-and-very-intentionally-so) [snippet]). Both are exact integer divisors of 1920×1080 (×6 and ×4).
- Classic RPG character size: FF I–VI used **16×24**. — [Siliconera](https://www.siliconera.com/interview-discussing-final-fantasy-pixel-remaster-sprites-and-designs/) [snippet]. The open LPC standard is **64×64** frames with 128/192 px oversize attack frames. — [ULPC README](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator/blob/master/README.md) [primary]
- Pixel density must match across characters and environment, or the characters "would look strange". — [Unreal Engine OT2 interview](https://www.unrealengine.com/developer-interviews/octopath-traveler-ii-builds-a-bigger-bolder-world-in-its-stunning-hd-2d-style) [snippet]
- Mixels, including non-integer scaling and different scales for different assets, are a widely recognised flaw. — [Flowlab](https://community.flowlab.io/t/mini-rant-stop-using-mixels/38287) [snippet]

### Inferences
This is my reasoning and arithmetic, not sourced.

**1. Integer divisors of common phone widths (portrait)**

| Phone width | Divisors |
|---|---|
| 1080 | ÷3 = 360, ÷4 = 270, ÷5 = 216, ÷6 = 180 |
| 1170 / 1179 (recent iPhones) | ÷4 ≈ 292–294 |
| 1440 (QHD Android) | ÷5 = 288, ÷6 = 240 |
| 720 (budget) | ÷2 = 360, ÷3 = 240 |

A design that guarantees a **safe width of about 240–270 virtual px**, and lets the canvas *expand* to whatever `floor(screen_width / scale)` gives (about 270–300), keeps every device at a whole-number scale with no black bars. Pick the largest integer scale that keeps virtual width ≥ about 240 and pad the extra width with arena border art. Height expands the same way: 2400 ÷ 4 = 600 virtual px of vertical room for the battlefield, bench or shop, and UI.

**2. Unit size from layout**
- A portrait autobattler board of 6–8 columns across about 240–270 px gives about 30–45 px per column.
- A **32×32** unit canvas fits with 2–8 px gutters, and 10–20 units fit comfortably in about 4–5 rows of the about 600 px height.
- At ×4, one 32 px unit is 128 physical px. On a typical 6.1–6.7" 1080-wide phone (about 65–70 mm wide, about 16 px/mm), that is roughly 8 mm. That is large enough to read class from silhouette and to tap. A 24 px unit (about 6 mm) is still readable. 16 px (about 4 mm) is too small for class identity on a crowded board.

**3. Why not larger (48–64 px units)?**
- At 48 px in a 270-wide canvas, only about 5 units fit per row.
- Area per frame is 2.25–4× that of 32 px, so with 30–45 frames per unit across a roster of perhaps 40–80 units, animation cost explodes.
- 64 px chibis at ×4 = 256 physical px, about 16 mm each, which is too big for 20 on screen.

**4. Why not smaller (16–24 px)?**
- 16 px removes the class or equipment read that a tactical game relies on.
- 24 px works and is cheaper. FF-style 16×24 sprites prove the readability ceiling. Choose 24 px if the design needs about 20+ units in a narrower board, or if the team is one artist.

**5. Landscape option**
- Virtual about 480×216 (2400 ÷ 5 by 1080 ÷ 5) or about 600×270 (÷4).
- Same 32 px units: a horizontal lane battlefield of about 12–16 cells × 4–6 rows fits 20 units easily.
- If you support both orientations, follow Godot's square-base tip, for example 270×270 core plus expand.

**6. Asset classes at one shared scale**
- Units: 32×32 canvas (character about 22–28 px).
- Elites and bosses: 48×48 or 64×64.
- Projectiles: 8–16 px.
- VFX: up to 64–96 px for AoE.
- Status icons: 8×8 or 16×16 above heads.
- UI icons: 16×16 or 24×24.
- Collection or gacha portraits: 64–96 px.

All of these render at the **same ×4 (or device) integer scale**. Do not show a portrait drawn at 1× next to units at a different scale. If larger "HD" portraits are wanted, make them a deliberate separate illustration style, not up-scaled pixel art.

**7. Rendering details**
- Nearest-neighbour filtering.
- Snap sprite positions to the virtual pixel grid. Godot's `viewport` stretch mode does this; Unity's Pixel Perfect Camera is the equivalent, though its docs were not fetched here.
- No sprite rotation or scaling at run time except by integer factors.
- Render UI text either as pixel fonts at the same scale or as a separate high-resolution UI layer, a deliberate stylistic split that many mobile pixel games accept. That second option is a design choice; I found no source here.

### Gaps
- King God Castle's actual unit size, virtual resolution and orientation could not be verified (no sources found), so I can't calibrate against the genre reference.
- I did not fetch Unity Pixel Perfect Camera docs (the raw path 404'd) or mobile safe-area guidance (notches, gesture bars). Physical-size estimates use assumed phone widths, not cited device specs.
- No playtest data on minimum readable sprite size for mobile tactics. The values above should be validated by mocking a 20-unit battle screen at the candidate sizes on real devices.
