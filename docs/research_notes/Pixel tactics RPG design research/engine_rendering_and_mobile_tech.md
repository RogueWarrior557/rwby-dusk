# Engine Selection, Pixel-Art Rendering and Mobile 2D Tech for a Pixel-Art Mobile Tactical Autobattler (Android/iOS, very small team)

> **Source-access note for the report writer (read first).** Research date: 2026-11-23. In this session the network policy blocked direct fetches of docs.godotengine.org, godotengine.org, unity.com, docs.unity.com, docs.unity3d.com, en.wikipedia.org and pcgamer.com, and the shared web-search budget ran out partway through. To compensate I read **primary sources straight from public GitHub repositories with git**:
> - `godotengine/godot-docs` @ master, commit `4b22866` (2026-11-22). This is the source of docs.godotengine.org/en/latest. Citations link the GitHub `.rst` file. The rendered page has the same path under `https://docs.godotengine.org/en/latest/…html`.
> - `godotengine/godot` @ tag `4.7.2-stable` (`doc/classes/ProjectSettings.xml` = the official class reference)
> - `godotengine/godot-website` @ master `d0feac7` (release-page data, blog articles, showcase entries)
> - `Unity-Technologies/Graphics` @ master `0efc28e` (URP source, including PixelPerfectCamera.cs)
> - `game-ci/documentation` @ main `2fa7310`; `bitwes/Gut` @ main; `MikeSchulze/gdUnit4` @ master; `viniciusgerevini/godot-aseprite-wizard` @ godot_4; `defold/defold` @ dev; `phaserjs/phaser` @ master
>
> Items marked **(search summary)** come from a web-search result digest of the cited URL. I could not open the page itself, so verify those before quoting them verbatim. Items marked **(direct observation)** are probes I ran in this session's container. Unity's official docs and pricing pages could not be opened, so every Unity claim comes from search summaries, Unity's GitHub source, or GameCI's docs.

---

## Q1. How do you render pixel art correctly on phones with arbitrary resolutions and aspect ratios?

### Takeaway
Use nearest-neighbor filtering, no mipmaps and lossless (non-VRAM-compressed) textures. Render the game world at a low internal resolution and upscale it by an **integer** factor. Handle the extra aspect ratio of phones and tablets by **expanding** the visible play area at that integer scale, not by fractional stretching. Keep text and dense UI either at integer multiples of the pixel grid or in a separate native-resolution UI layer. Modern phones (2.0–8.5× fractional scale for typical bases) leave only a few pixels of remainder at integer scale, so the main design problem is **how much extra world each device reveals**, not blur.

### Cited Findings
**Filtering / mipmaps / snapping (Godot primary docs, which generalize to any engine)**
- Godot's default 2D texture filter is a project setting (`rendering/textures/canvas_textures/default_texture_filter`, default = Linear). The class reference points pixel-art users to the 2D snap settings — [Godot 4.7.2 ProjectSettings.xml](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/ProjectSettings.xml)
- "Since Godot 4.0, texture filter and repeat modes are set in the CanvasItem properties in 2D (with a project setting acting as a default)". Godot's default 2D import options are "no mipmaps and **Lossless** compression" and "are suited for 2D" — [godot-docs importing_images.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/assets_pipeline/importing_images.rst)
- `rendering/2d/snap/snap_2d_transforms_to_pixel`: "CanvasItem nodes will internally snap to full pixels. Useful for low-resolution pixel art games… This can lead to a crisper appearance at the cost of less smooth movement, especially when Camera2D smoothing is enabled." It is only read at startup (use `RenderingServer.viewport_set_snap_2d_transforms_to_pixel` at runtime). It is "not recommended" together with `snap_2d_vertices_to_pixel`, "as movement may appear even less smooth. Prefer only enabling this setting" — [ProjectSettings.xml 4.7.2](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/ProjectSettings.xml)
- `gui/common/snap_controls_to_pixels` defaults to **true** ("snaps Control node vertices to the nearest pixel to ensure they remain crisp even when the camera moves or zooms") — [ProjectSettings.xml 4.7.2](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/ProjectSettings.xml)
- Unity's URP Pixel Perfect Camera exposes the same ideas as an enum. `GridSnapping.PixelSnapping` = "Prevent subpixel movement and make Sprites appear to move in pixel-by-pixel increments". `UpscaleRenderTexture` = "The scene is rendered to a temporary texture set as close as possible to the Reference Resolution, while maintaining the full screen aspect ratio. This temporary texture is then upscaled to fit the full screen." `assetsPPU` = "Match this value to the Pixels Per Unit values of all Sprites" — [Unity Graphics repo, PixelPerfectCamera.cs](https://github.com/Unity-Technologies/Graphics/blob/master/Packages/com.unity.render-pipelines.universal/Runtime/2D/PixelPerfectCamera.cs)

**Integer vs. fractional scaling, letterbox vs. expand**
- Godot docs: with fractional scaling at 2.133×, "each pixel in the viewport corresponds to 2.133×2.133 pixels… since displays can only display 'whole' pixels, this will lead to uneven pixel scaling which results in incorrect appearance of pixel art". With `integer`, the image is shown at 2× "with black bars" on all four sides — [godot-docs multiple_resolutions.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst)
- **Correction to the brief:** Godot's integer scale mode dates from **Godot 4.2**, not 4.3: "Since Godot 4.2, the **Stretch Scale Mode** setting allows you to constrain the… scale factor… to integer values" — [multiple_resolutions.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst)
- `display/window/stretch/scale_mode = "integer"`: "The scale factor will be floored to an integer value… This provides a crisp pixel art appearance." Note: "resizing the window to be smaller than the base viewport size will clip the contents" — [ProjectSettings.xml 4.7.2](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/ProjectSettings.xml)
- Godot's official pixel-art recipe: "Most pixel art games use viewport sizes between 256×224 and 640×480. 640×360 is a good baseline, as it scales to 1280×720, 1920×1080, 2560×1440, and 3840×2160 without any black bars when using integer scaling." Set stretch mode `viewport`. Set stretch aspect `keep` (black bars) **or** `expand` "to support multiple aspect ratios", and if using expand, anchor Controls to the correct corners. Set scale mode `integer` — [multiple_resolutions.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst)
- The same page's generic *mobile* recipes (portrait 720×1280 or 1080×1920, `canvas_items`, `expand`) are for **non-pixel-art** games. For tablets and foldables it suggests a 3:4 base (e.g. 960×1280) — [multiple_resolutions.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst)
- Unity's Pixel Perfect Camera `CropFrame` options: none; pillarbox; letterbox; windowbox ("Black borders added to all sides of viewport to match Reference Resolution"); and StretchFill ("Expands the viewport to fit the screen resolution while maintaining the viewport's aspect ratio") — [PixelPerfectCamera.cs](https://github.com/Unity-Technologies/Graphics/blob/master/Packages/com.unity.render-pipelines.universal/Runtime/2D/PixelPerfectCamera.cs)
- Unity's final-blit filter modes: RetroAA = "point filter to upscale to closest multiple of Reference Resolution, followed by bilinear filter to the target resolution". Point = "point filter to upscale to target resolution" — [PixelPerfectCamera.cs](https://github.com/Unity-Technologies/Graphics/blob/master/Packages/com.unity.render-pipelines.universal/Runtime/2D/PixelPerfectCamera.cs). Per Unity's docs, the filter mode only applies with Stretch Fill. Retro AA reduces shimmer but can look blurry, and Point is sharper with more shimmer **(search summary)** — [Unity Manual: Pixel Perfect Camera reference](https://docs.unity3d.com/Manual/urp/2d-pixelperfect-ref.html)
- Practitioner reports (anecdotal): integer scaling "create[s] black borders until the window is big enough", and some users switch to fractional to avoid bars. Several threads report sprite misalignment with integer scaling, with suggested fixes of rounding `global_position` and aligning sprite offsets to whole pixels **(search summary)** — [Godot Forum: PixelArt resolution artefacts with Integer scaling](https://forum.godotengine.org/t/pixelart-resolution-artefacts-with-integer-scaling/109353). A community Godot 4.4 guide recommends 640×360 base, `canvas_items`, integer, Nearest **(search summary)** — [itch.io: Godot 4.4 settings for pixel art](https://itch.io/blog/806788/godot-44-settings-for-pixel-art)

**Low-res viewport vs. high-res canvas; subpixel motion**
- Godot: "The `viewport` stretch mode provides low-resolution rendering that is then stretched to the final window size. If you are OK with sprites being able to move or rotate in 'sub-pixel' positions or wish to have a high resolution 3D viewport, you should use the `canvas_items` stretch mode instead" — [multiple_resolutions.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst)
- Unity docs say Upscale Render Texture keeps rotated pixels upright and square instead of producing high-resolution diagonal edges. The legacy standalone package says Pixel Snapping is only available when Upscale Render Texture is disabled, and that the standalone 2D Pixel Perfect package supports only the Built-in pipeline, so URP users should not install it **(search summary)** — [Unity Manual: Pixel Perfect Camera ref](https://docs.unity3d.com/Manual/urp/2d-pixelperfect-ref.html); [com.unity.2d.pixel-perfect 5.1 docs](https://docs.unity3d.com/Packages/com.unity.2d.pixel-perfect@5.1/manual/index.html)
- Godot physics interpolation (`physics/common/physics_interpolation`, default off) "will interpolate the transforms of objects… so that smooth motion is seen even when physics ticks do not coincide with rendered frames" — [ProjectSettings.xml 4.7.2](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/ProjectSettings.xml). The jitter doc warns it "will increase input lag" — [godot-docs jitter_stutter.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/jitter_stutter.rst)
- Godot 4.7 added nearest-neighbor filtering for **3D** resolution scaling, but "this does not affect 2D rendering", so it is irrelevant to a pure 2D game — [godot-website release_4_7 features.yml](https://github.com/godotengine/godot-website/blob/master/_data/release_4_7/features.yml)

**UI, fonts, hiDPI, safe areas**
- Pixel fonts: "Fonts that have a pixel art appearance should have bilinear filtering disabled" (Default Texture Filter → Nearest). "The font size must also be an integer multiple of the design size… and the Control node using the font must be scaled by an integer multiple as well. Otherwise, the font may look blurry." Godot supports BMFont `.fnt` and image-based bitmap fonts — [godot-docs gui_using_fonts.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/ui/gui_using_fonts.rst)
- Godot font oversampling is enabled by default (it re-rasterizes dynamic fonts when the viewport scale changes), so native-resolution UI text stays crisp under `canvas_items` — [multiple_resolutions.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst)
- Safe areas: on Android you can enable **Edge to Edge** in the export preset and use `DisplayServer.get_display_safe_area` and `DisplayServer.get_display_cutouts` "to query the area in which your application can safely draw" — [godot-docs creating_applications.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/ui/creating_applications.rst)

**Texture compression (ETC2/ASTC) and memory**
- Godot: **Lossless** "is the default and most common compression mode for 2D assets… without any kind of artifacting… It will use considerably more amount of video memory than VRAM Compression… This is also the recommended setting for pixel art." **VRAM Compressed** (S3TC/BPTC/ETC2 by platform; ASTC on mobile when enabled) reduces VRAM "usually by a factor between 4 and 6" but "should be avoided for 2D as it exhibits noticeable artifacts, especially for lower-resolution textures". "Even in 3D, 'pixel art' textures should have VRAM compression disabled as it will negatively affect their appearance, without improving performance significantly due to their low resolution." Lossy (WebP) shrinks disk size only, "Video memory usage isn't decreased" — [importing_images.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/assets_pipeline/importing_images.rst)
- `import_etc2_astc`: ETC2 for lower-quality textures and ASTC (4×4 blocks) for high-quality textures — [ProjectSettings.xml 4.7.2](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/ProjectSettings.xml)
- Godot's memory table for one RGBA8 texture *with mipmaps*: 512² = 1.33 MiB; 1024² = 5.33 MiB; 2048² = 21.33 MiB; 4096² = 85.33 MiB (VRAM-compressed = ¼ of that) — [importing_images.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/assets_pipeline/importing_images.rst)

### Inferences
- **Device scale table (my arithmetic: integer scale = floor(min(W/bw, H/bh)); "fill viewport" = floor(screen/scale) game pixels when expanding).**

  | Device (portrait) | Base 180×320 | Base 270×480 | Base 360×640 |
  |---|---|---|---|
  | Low-end 720×1600 | 4× → 180×400 | 2× → 360×800 | 2× → 360×800 |
  | 1080×2400 (20:9) | 6× → 180×400 | 4× → 270×600 | 3× → 360×800 |
  | 1080×1920 (16:9) | 6× → 180×320 | 4× → 270×480 | 3× → 360×640 |
  | iPhone 13/14 1170×2532 | 6× → 195×422 | 4× → 292×633 | 3× → 390×844 |
  | iPhone Pro Max 1290×2796 | 7× → 184×399 | 4× → 322×699 | 3× → 430×932 |
  | iPad 10.2" 1620×2160 | 6× → 270×360 | 4× → 405×540 | 3× → 540×720 |
  | iPad Pro 12.9" 2048×2732 | 8× → 256×341 | 5× → 409×546 | 4× → 512×683 |

  The remainder at integer scale is ≤4 screen pixels on every device above, so black bars are negligible **if the viewport expands**. But the visible world changes a lot, e.g. 180 px wide on phones vs 270 px wide on an iPad at the 180×320 base. Design a fixed **"safe core" board** (the tactical grid plus essential HUD) that fits the base resolution. Treat everything beyond it as decorative bleed or extra HUD space. For a portrait autobattler, a ~180–270 px wide logical canvas yields 4–6× scale on phones (chunky, very readable). A 360-wide canvas gives only 2–3×, which needs more art per screen.
- **Recommended pattern (Godot):** stretch mode `viewport` + aspect `expand` + scale mode `integer` + Nearest + `snap_2d_transforms_to_pixel`. **Or** keep the root in `canvas_items` for native-resolution UI/text and render the board in a `SubViewport` scaled by an integer factor. The second option avoids pixel fonts for localized text (CJK glyph sets are impractical as hand-made pixel fonts). Whether Godot's built-in `expand` + `integer` fills to within <1 scale step on all devices, or leaves larger bars, needs a device test (see Gaps). A ~20-line script that computes `floor(screen/scale)` and sets the viewport size is a reliable fallback.
- **Memory budget example (arithmetic, uncompressed RGBA8, no mipmaps):** a 48×48 hero with 8 animations × 8 frames ≈ 64 frames × 9.2 KB ≈ 0.59 MB. 40 heroes ≈ 24 MB of sprite data. Packed into 2048² atlases (16 MiB each without mipmaps), that is about 2 atlases. A 270×600 RGBA8 render target is about 0.65 MB. Pixel-art games can afford lossless textures on any phone that meets Godot's or Unity's minimums. Disk size is controlled by PNG/WebP-lossless storage, not VRAM compression.
- Because ASTC and ETC2 encode 4×4 blocks with interpolated endpoint colors, palette-exact pixel art gets color bleeding across hard edges. This matches Godot's "noticeable artifacts, especially for lower-resolution textures" statement. This is my explanation; the docs give no mechanism.

### Gaps
- I could not open Unity's Sprite import documentation to cite the standard Unity pixel-art import settings: Filter Mode = Point, Compression = None, Generate Mip Maps off, consistent PPU. This is widely known practice but unverified this session.
- No device test confirmed how Godot 4.7's `viewport` + `expand` + `integer` distributes remainder pixels on 19.5:9 phones. Godot docs show only the `keep` case with bars.
- I found no authoritative 2026 device-resolution market-share data (Godot docs link to Google stats, but that page was not accessible).

---

## Q2. Godot 4.x: version status, pixel-art settings, mobile export maturity and tooling

### Takeaway
As of 2026-11-23 the latest stable release is **Godot 4.7.2** (Aug 2026), and **4.8 is in beta 4** (Nov 18, 2026). The engine is MIT-licensed. Godot has first-class pixel-art settings (integer scaling since 4.2, 2D snapping, nearest filtering). 2D batching has run on every renderer since 4.4. The **Compatibility (OpenGL ES 3.0/WebGL2)** renderer is the right default for a 2D mobile game: it covers the widest range of devices, launches faster and is the only renderer that also exports to web. **GDScript, not C#**, is the safe choice, because C# on Android/iOS is still "experimental" and C# cannot export to web at all.

### Cited Findings
**Versions (verify at release time)**
- Git tags on `godotengine/godot` include 4.6, 4.6.1–4.6.3 and **4.7, 4.7.1, 4.7.2-stable** (the latest stable tag) — [godotengine/godot tags](https://github.com/godotengine/godot/tags) (direct `git ls-remote`, 2026-11-23)
- "Maintenance release: Godot 4.7.2" is dated 2026-08-18 — [godot-website article source](https://github.com/godotengine/godot-website/blob/master/collections/_article/maintenance-release-godot-4-7-2.md). "Dev snapshot: Godot 4.8 beta 4" is dated 2026-11-18 — [godot-website article source](https://github.com/godotengine/godot-website/blob/master/collections/_article/dev-snapshot-godot-4-8-beta-4.md). One outlet calls it a likely final beta **(search summary)** — [linuxcompatible.org](https://www.linuxcompatible.org/story/godot-48-beta-4-released-as-likely-final-beta-before-stable-launch/)
- 4.7 was released 18 June 2026 (HDR output, AreaLight3D, Asset Store overhaul, stable Android build environment "GABE") **(search summary)** — [Phoronix](https://phoronix.com/news/godot-4.7-released). 4.6.3 shipped May 20, 2026 **(search summary)** — [gamedev.net](https://gamedev.net/news/3473-maintenance-release-godot-463/). The 4.4 stable page is dated 3 March 2025 **(search summary)** — [Godot 4.4 release page](https://godotengine.org/releases/4.4)
- Feature status by version: 4.2 = integer scale mode; 4.3 = **TileMapLayer** node (release-page highlight "new-tilemaplayer-node") and single-threaded web export; 4.4 = 2D batching on Forward+/Mobile, automatic fallback from Vulkan/D3D12/Metal to OpenGL, ubershaders; 4.5 = `optimize=size_extra` build option; 4.6 = Vulkan Mobile crash fixes for Mali/Adreno, CSV translation context/plurals; 4.7 = per-platform export template downloader, Perfetto tracing on Android, GABE stable — sources: [multiple_resolutions.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst), [4.3 release page source](https://github.com/godotengine/godot-website/blob/master/pages/releases/4.3.html), [exporting_for_web.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/export/exporting_for_web.rst), [4.4 dev 3 article](https://github.com/godotengine/godot-website/blob/master/collections/_article/dev-snapshot-godot-4-4-dev-3.md), [renderers.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/renderers.rst), [optimizing_for_size.rst](https://github.com/godotengine/godot-docs/blob/master/engine_details/development/compiling/optimizing_for_size.rst), [release_4_6 features.yml](https://github.com/godotengine/godot-website/blob/master/_data/release_4_6/features.yml), [release_4_7 features.yml](https://github.com/godotengine/godot-website/blob/master/_data/release_4_7/features.yml)

**Renderer choice and device support**
- Renderers: Forward+ and Mobile run on RenderingDevice (Vulkan / D3D12 / Metal). **Compatibility** uses OpenGL and is "suited for low-end desktop and mobile platforms. Used by default on the web platform". Choose Compatibility if "developing for older mobile devices", "for web… Compatibility is the only choice", "developing a 2D game", or if "You want the best performance possible on all devices". In the docs' feature table, 2D games are "Yes" for Compatibility, and for Mobile/Forward+ "Yes, but Compatibility is usually good enough for 2D" — [renderers.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/renderers.rst)
- "Since Godot 4.4, when using Forward+ or Mobile, if Vulkan is not supported" the engine tries D3D12/Metal, then "will then fall back to Compatibility" (controlled by `Fallback to OpenGL 3`) — [renderers.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/renderers.rst)
- "The Compatibility renderer has lower hardware requirements and generally launches faster" — [creating_applications.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/ui/creating_applications.rst)
- Minimum OS for **exported** games: Android 7.0 (Compatibility), Android 9.0 (Forward+/Mobile), iOS 15.0 (Vulkan via MoltenVK) or iOS 16.0 (Metal). Mobile GPU minimum: "full OpenGL ES 3.0 support" for Compatibility and "full Vulkan 1.0 support" for Mobile/Forward+ — [godot-docs system_requirements.rst](https://github.com/godotengine/godot-docs/blob/master/about/system_requirements.rst)
- Godot 4.6 "Mobile mended": "we tracked down and fixed a series of crashes affecting devices with certain Mali and Adreno mobile GPUs. If you've been seeing unexplained crashes on Android with the Mobile renderer, this release should bring relief" (credited to crash logs shared by the developers of *Rift Riff* and *Kamaeru*) — [release_4_6 features.yml](https://github.com/godotengine/godot-website/blob/master/_data/release_4_6/features.yml)
- Since 4.4, Forward+/Mobile avoid shader-compilation stutter with ubershaders, but "when using the Compatibility renderer, it is not possible to use this ubershader approach due to technical limitations in OpenGL" — [jitter_stutter.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/jitter_stutter.rst)

**Pixel-art project settings (summary of Q1, Godot-specific)**
- Stretch mode `viewport`, aspect `keep`/`expand`, scale mode `integer`, base 640×360 (desktop guidance) — [multiple_resolutions.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst). `snap_2d_transforms_to_pixel` preferred over vertex snapping; Controls snap by default — [ProjectSettings.xml 4.7.2](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/ProjectSettings.xml). The editor's "Use Pixel Snap" only affects editing. For runtime, use Rendering > 2D > Snapping and GUI > Snap Controls to Pixels — [introduction_to_2d.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/2d/introduction_to_2d.rst)

**Animation / Aseprite / tiles**
- Godot Aseprite Wizard (Godot 4 branch, updated Nov 2026) imports `.aseprite` files as **SpriteFrames** (for AnimatedSprite2D), static textures, tileset textures (from Aseprite tilemap layers), or AnimationPlayer tracks. It splits tags into animations and supports slices and per-layer export. "Aseprite Wizard is only required during development… animations previously imported should keep working" — [godot-aseprite-wizard README](https://github.com/viniciusgerevini/godot-aseprite-wizard)
- It shells out to the **Aseprite executable**, and an option "Generate Bake Files" "creates a resource file (bake)… that can be used as fallback when the machine doesn't have Aseprite installed". This matters for CI containers without Aseprite — [Aseprite Wizard docs: introduction](https://github.com/viniciusgerevini/godot-aseprite-wizard/blob/godot_4/docs/en/1-introduction/index.md)
- Godot's built-in SpriteFrames editor can slice frames from a spritesheet grid ("Add frames from sprite sheet") — [godot-docs 2d_sprite_animation.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/2d/2d_sprite_animation.rst)

**UI**
- Control-node anchoring via the Layout menu is the recommended way to adapt to `expand`. Since 4.7 Controls have "offset transform" properties (visual-only transforms for juicy UI) — [multiple_resolutions.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst); [release_4_7 features.yml](https://github.com/godotengine/godot-website/blob/master/_data/release_4_7/features.yml)

**GDScript vs C#**
- "Since Godot 4.2, projects written in C# support all desktop platforms… as well as Android and iOS. **Android support is currently experimental. iOS support is currently experimental** and has a few limitations… Exporting to iOS can only be done from a macOS device. Currently, projects written in C# **cannot be exported to the web platform**" (docs master, Nov 2026) — [godot-docs c_sharp/index.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/scripting/c_sharp/index.rst); [c_sharp_basics.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/scripting/c_sharp/c_sharp_basics.rst)
- GDScript memory: "Godot implements reference counting… instead of a garbage collector". RefCounted/Resource instances free automatically, while Nodes/Objects need `free()`/`queue_free()` — [gdscript_basics.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/scripting/gdscript/gdscript_basics.rst)

**Web export**
- Godot 4 web export targets **WebGL 2.0 via Compatibility only**. "Since Godot 4.3, Godot supports exporting your game on a single thread", which avoids SharedArrayBuffer/cross-origin-isolation requirements and "works very well on macOS and iOS too" — [exporting_for_web.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/export/exporting_for_web.rst)

**Licensing**
- Godot's `LICENSE.txt` at tag 4.7.2-stable is the MIT ("Permission is hereby granted…") license, "Copyright (c) 2014-present Godot Engine contributors". There are no royalties, seats or activation — [godot LICENSE.txt @ 4.7.2-stable](https://github.com/godotengine/godot/blob/4.7.2-stable/LICENSE.txt)

**Build size**
- Custom export templates: `optimize=size` (default on WebAssembly), `optimize=size_extra` (since 4.5), and `disable_3d=yes`, which reduces binary size "by about 15%" — [optimizing_for_size.rst](https://github.com/godotengine/godot-docs/blob/master/engine_details/development/compiling/optimizing_for_size.rst)

### Inferences
- For this project the Compatibility renderer's drawbacks (no ubershader, fewer 3D features) barely matter: a 2D sprite game uses few shader variants, and those can be warmed at load. Its benefits matter a lot: Android 7.0+ reach, fastest launch, and pixel-identical behavior between the native build and the **web build** used for browser-based visual QA.
- Use GDScript. C# would cost the web export (which the container-based QA loop depends on) and adds "experimental" mobile risk for a small team.
- Pin a single minor version (4.7.x now). Move to 4.8 only after its first maintenance release, because Godot minor releases carry breaking changes (4.6 notes recommend reading the migration guide — search summary, [Godot 4.6 release](https://godotengine.org/releases/4.6/)).

### Gaps
- No measured Godot 4.7 Android APK size or cold-start time was found (Godot docs give relative figures only). Measure on a low-end device early.
- I could not confirm whether 4.8 contains 2D/mobile changes relevant here (only titles from news snippets).
- Third-party license obligations (e.g. FreeType, mbedTLS notices that must ship with an exported game) were not reviewed.
- Godot's mobile monetization plugin ecosystem (IAP, ads, Play Games) was not researched this session. It is commonly reported as thinner than Unity's, which is a real risk for a commercial mobile release.

---

## Q3. Unity 6 (2D): features, 2026 licensing and suitability under the project's constraints

### Takeaway
Unity 6 has a mature 2D stack (URP 2D Renderer, Pixel Perfect Camera, Sprite Atlas, 2D Animation, Aseprite Importer) and the deepest mobile ecosystem. The runtime fee was cancelled in Sept 2024, and Personal is free under $200K revenue with an optional splash screen. Its weak point for *this* project is automation: **Personal licenses cannot be activated manually in headless Docker** (activation runs through Unity Hub), Unity downloads are unreachable from this container, and the editor is heavy. That makes Unity a poor fit for a "develop and test in a headless Linux container" workflow.

### Cited Findings
**Versions**
- Unity 6.3 LTS is supported until December 2027, and Unity 6.0 LTS is supported through October 2026 **(search summary)** — [Unity blog: Unity 6.3 LTS is now available](https://unity.com/blog/unity-6-3-lts-is-now-available); [Unity Manual: New in Unity 6.3 LTS](https://docs.unity.com/en-us/engine/current/manual/whats-new/unity63). Unity's manual header shows "Version: Unity 6.6 (6000.6)", and docs exist for 6000.7 and 7000.0 paths **(search-result listings)** — [docs.unity3d.com Manual](https://docs.unity3d.com/Manual/WhatsNewUnity63.html). I could not verify which of 6.4–6.7 or "7000.0" are final or preview releases.
- 6.3 LTS 2D additions: URP 2D can render 3D Mesh/Skinned Mesh renderers alongside sprites with 2D lights, Sprite Masks and Sorting Groups; low-level 2D physics APIs integrating **Box2D v3**; a Sprite Atlas Analyser (secondary source) **(search summary)** — [Unity Manual: New in 6.3](https://docs.unity.com/en-us/engine/current/manual/whats-new/unity63); [AlternativeTo news](https://alternativeto.net/news/2025/12/unity-6-3-lts-arrives-with-hybrid-2d-3d-scenes-box2d-v3-and-cross-platform-toolkit)

**Pixel Perfect Camera (URP)**
- Built into URP (`UnityEngine.Rendering.Universal.PixelPerfectCamera`): assetsPPU, refResolutionX/Y, CropFrame {None, Pillarbox, Letterbox, Windowbox, StretchFill}, GridSnapping {None, PixelSnapping, UpscaleRenderTexture}, FilterMode {RetroAA, Point}. A Cinemachine extension `CinemachineUniversalPixelPerfect` exists in the same package — [PixelPerfectCamera.cs](https://github.com/Unity-Technologies/Graphics/blob/master/Packages/com.unity.render-pipelines.universal/Runtime/2D/PixelPerfectCamera.cs); [Graphics repo Runtime/2D folder](https://github.com/Unity-Technologies/Graphics/tree/master/Packages/com.unity.render-pipelines.universal/Runtime/2D)

**Pricing / license (2026)**
- Runtime Fee cancelled for games, announced **September 12, 2024**, with a return to seat-based subscriptions. The "Made with Unity" splash screen becomes **optional for Unity Personal games built with Unity 6**. The Personal ceiling doubled from $100K to **$200K** **(search summary)** — [Unity blog: Unity is canceling the Runtime Fee](https://unity.com/blog/unity-is-canceling-the-runtime-fee); [Game World Observer](https://gameworldobserver.com/2024/09/12/unity-cancels-runtime-fee-new-pricing-changes); [Windows Central](https://www.windowscentral.com/gaming/unity-backtracks-on-controversial-runtime-fee-takes-major-step-in-restoring-eroded-trust)
- Current terms: **Personal** free for individuals and small businesses with < $200K revenue or funds raised in the prior 12 months. A 2026 changes page says the Personal seat cap is being removed. **Pro** is required above $200K and listed at **$2,310/yr per seat** (Chinese page: $210/seat/month). **Enterprise** above $25M. Unity Pro/Enterprise prices rose **5% starting January 12, 2026** **(search summary)** — [Unity: Changes to subscription plans and pricing](https://unity.com/products/pricing-updates); [Unity Plans & Pricing](https://unity.com/products). In 2024 coverage, Pro rose 8% to $2,200/seat/yr effective Jan 2025, consistent with the later $2,310 after +5% — [Game World Observer](https://gameworldobserver.com/2024/09/12/unity-cancels-runtime-fee-new-pricing-changes); [Game Developer](https://gamedeveloper.com/business/unity-is-killing-its-controversial-runtime-fee)

**Headless / CI / licensing in containers**
- GameCI (the de-facto open-source Unity CI) says "All Unity actions require activation". For a **Personal** license you must "Use Unity Hub to create a `.ulf` license file", then store the `.ulf` plus Unity email and password as CI secrets — [GameCI docs: Activation](https://github.com/game-ci/documentation/blob/main/docs/03-github/02-activation.mdx)
- GameCI troubleshooting: "**Unity no longer supports manual activation of Personal licenses**". The documented workaround is editing the activation web page's HTML to unhide the Personal option — [GameCI docs: common issues](https://github.com/game-ci/documentation/blob/main/docs/09-troubleshooting/common-issues.mdx); [Unity Discussions thread](https://discussions.unity.com/t/unity-no-longer-supports-manual-activation-of-personal-licenses/926760)
- Reported headless failures: "License is not active (com.unity.editor.headless)" on Linux with GameCI images v3 — [game-ci/unity-orb#74](https://github.com/game-ci/unity-orb/issues/74). Docker masking `/etc/machine-id` breaks license file generation — [Unity Issue Tracker](https://issuetracker.unity3d.com/issues/cannot-activate-license-within-a-docker-container)
- Unity's own Docker docs: the "Headless Editor is available only for Linux x86_64", and container licensing is described via floating license servers (a Pro/Enterprise setup) **(search summary)** — [Unity Manual 6000.7: Docker](https://docs.unity.com/en-us/engine/6000.7/manual/building-and-publishing/docker)
- GameCI `unity-builder` supports Linux and Windows editor containers plus macOS hosts. Android output via `androidExportType` = `androidPackage` (APK) or `androidAppBundle` (AAB) — [GameCI docs: Builder](https://github.com/game-ci/documentation/blob/main/docs/03-github/04-builder.mdx). Tests: `testMode` = All/PlayMode/EditMode/Standalone — [GameCI docs: Test runner](https://github.com/game-ci/documentation/blob/main/docs/03-github/03-test-runner.mdx)
- iOS: "Unity will produce an Xcode project that needs to be built using Xcode on a Mac". GameCI's example runs the build on `ubuntu-latest` and the Xcode/fastlane step on `macos-latest` — [GameCI docs: iOS deployment](https://github.com/game-ci/documentation/blob/main/docs/03-github/06-deployment/ios.mdx)
- **(direct observation)** From this container, `public-cdn.cloud.unity3d.com` (Unity Hub AppImage) and `download.unity3d.com` did not resolve or connect under the current network policy.

### Inferences
- Unity remains a strong engine for a human team working on desktop machines with a GPU. It has better mobile SDK and monetization coverage (ads, IAP, analytics) and a larger hiring pool. For an agent- and container-driven workflow, though, every Unity build and test needs a Hub-activated `.ulf` secret (fragile for Personal), allow-listed Unity download hosts, and multi-GB editor and module images.
- Pricing risk is now moderate and predictable: free under $200K, then about $2.3K/seat/yr. The 2023 episode remains a trust factor: Mega Crit left mid-production over it (Q9).

### Gaps
- Could not open Unity docs to verify: Sprite Atlas v2 behavior, 2D Animation/PSD Importer, **Aseprite Importer** package status, UI Toolkit vs uGUI runtime maturity for mobile, editor and module install size, `Application.persistentDataPath`, ScriptableObject workflows, and the Unity Test Framework CLI flags (`-batchmode -nographics -runTests`). These are standard Unity knowledge but unverified this session.
- Could not confirm whether Unity Personal now offers any officially supported headless or serial-based activation for CI in 2026.
- The exact status of Unity 6.4–6.7 and the "7000.0" docs track is unverified.

---

## Q4. Credible alternatives: Defold, GameMaker, Phaser (web + Capacitor), LÖVE

### Takeaway
Only Defold and Phaser were checked against primary sources this session. Defold is a free, source-available engine with first-class iOS/Android/HTML5 targets. Phaser 4 is an MIT web framework whose native mobile builds depend on third-party wrappers. Neither beats Godot on the project's combination of integer-scaled pixel art, native mobile export and a headless Linux toolchain. GameMaker and LÖVE could not be verified (see Gaps).

### Cited Findings
- **Defold:** licensed under the "Defold License, Version 1.0, May 2020" (its own license, not OSI MIT). The repo has platform-specific build docs for iOS, Android and HTML5/Emscripten and was actively committed on 2026-11-23 — [defold/defold README and LICENSE.txt](https://github.com/defold/defold)
- **Phaser:** "fast, free, and fun open source HTML5 game framework… WebGL and Canvas rendering across desktop and mobile web browsers", MIT license (© 2026 Phaser Studio Inc.). Games "can be built for the web… or compiled to iOS, Android, Steam and native apps **using 3rd party tools**". JS or TypeScript. The minified build is "345 KB" gzipped. **Phaser 4** replaces the v3 pipeline with a new node-based WebGL renderer: "Multi-texture batching is smarter, avoiding unnecessary batch breaks on mobile", plus a "Blocky" filter "for pixel-art-friendly pixelation" — [phaserjs/phaser README](https://github.com/phaserjs/phaser)

### Inferences
- **Phaser + Capacitor** is the most Playwright-friendly stack: everything is a browser page, so headless Chromium tests are native to it. But mobile performance runs inside a WebView, platform features (IAP, notifications, safe areas) come through Capacitor plugins, and integer-scaling discipline must be hand-built (canvas `image-rendering: pixelated`, `roundPixels`, manual viewport math). It is a reasonable plan B if the team is web-native.
- **Defold** is lightweight, with small builds and a strong mobile focus, and is scriptable in Lua. Its smaller community and fewer pixel-art and UI conveniences make it a niche choice. Its headless build tool (bob.jar) is plausible for CI but was not verified here.

### Gaps
- **GameMaker:** current 2026 licensing (free non-commercial tier vs paid commercial/console tiers), Linux CLI build support, and mobile export cost were not verified. Search budget ran out and gamemaker.io was not tried.
- **LÖVE:** mobile ports (love-android, iOS via Xcode) are community-maintained. Status in 2026 not verified.
- **Defold** headless CLI (bob.jar) and pixel-perfect rendering specifics not verified.

---

## Q5. The headless Linux container constraint: install, test, export, screenshot

### Takeaway
Godot fits this constraint best. It is a single ~78 MB binary downloadable from GitHub (reachable from this container). It officially supports `--headless` for CI, CLI export (`--export-release Android game.apk`), and headless unit tests (GUT, gdUnit4 with JUnit XML). Its Compatibility-renderer **web export** can be served locally and screenshotted with the available Chrome/Playwright. Android APK export additionally needs the Android SDK + JDK (SDK host currently blocked), and **iOS needs macOS + Xcode for any engine**.

### Cited Findings
- "Using the `--headless` command line argument is **required** on platforms that do not have GPU access (such as continuous integration)". `--headless` = `--display-driver headless --audio-driver Dummy`. Examples: `godot --headless --export-release Android /var/builds/project.apk`. Other flags: `--import` (import resources, then quit), `--export-debug`, `--export-pack` (PCK/ZIP only), `--install-android-build-template`, `--quit-after <n>`, `--write-movie <file>` ("usually with .avi or .png extension"), `--rendering-driver` — [godot-docs command_line_tutorial.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/editor/command_line_tutorial.rst)
- Android export from a desktop host requires **OpenJDK 17** ("Higher versions of the JDK are also supported, but we recommend using JDK 17") and the Android SDK, installed via the Android CLI (`platform-tools build-tools/36.1.0 platforms/android-36 cmdline-tools/latest ndk/29.0.14206865 cmake/3.22.1`). The docs warn: "do not use an Android SDK provided by your distribution's repositories". AAB for Google Play requires a Gradle build, and Play uploads need a non-debug keystore (`keytool -genkey …`). The 4.8 editor adds automatic Android/Java SDK setup — [godot-docs exporting_for_android.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/export/exporting_for_android.rst)
- iOS: "You must export for iOS from a computer running macOS with Xcode installed" — [godot-docs exporting_for_ios.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/export/exporting_for_ios.rst). Unity has the same constraint (Xcode project built on a Mac) — [GameCI iOS docs](https://github.com/game-ci/documentation/blob/main/docs/03-github/06-deployment/ios.mdx)
- 4.7 added a per-platform export template downloader, because previously "you had to download export templates for all platforms even if you only you wanted to export your project for a single platform" — [release_4_7 features.yml](https://github.com/godotengine/godot-website/blob/master/_data/release_4_7/features.yml)
- **Testing:** GUT plugin version **9.6.1** (GUT ≥ 9.0 supports Godot 4) ships a command-line runner `gut_cmdln.gd` — [bitwes/Gut](https://github.com/bitwes/Gut). **gdUnit4** supports GDScript and C# tests, scene and input simulation (mouse, signals), mocking, a "Command Line Tool — Run tests outside the Godot editor for CI/CD pipelines", "JUnit XML" export and a GitHub Action. Compatibility: v6.2.x → Godot 4.5–4.7.1; master v7.0.0 → 4.7, 4.7.1, 4.8.dev7 — [gdUnit4 README](https://github.com/MikeSchulze/gdUnit4)
- **(direct observation, 2026-11-23)** In this container: GitHub release assets resolve (the Godot 4.7.2 Linux editor zip is 77,860,424 bytes, and the all-platform export templates `.tpz` are 1,281,349,702 bytes). `dl.google.com` (Android SDK repository) did **not** resolve. Installed tools: `Xvfb`/`xvfb-run`, Mesa `swrast_dri.so`/`kms_swrast_dri.so` (software OpenGL, llvmpipe) and `zink_dri.so`, **Google Chrome for Testing 153**, **OpenJDK 21**, 4 CPU cores and 15 GB RAM. An attempt to download and execute the Godot binary was blocked by this session's permission policy, so **no engine run was performed**.
- Web export of the same project is WebGL2/Compatibility, and single-threaded export needs no cross-origin isolation headers — [exporting_for_web.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/export/exporting_for_web.rst)

### Inferences
- **Realistic Godot pipeline in this container:** (1) download the pinned editor binary and only the Web (and later Android) templates. (2) `godot --headless --import`. (3) Run unit and simulation tests with `godot --headless -s addons/gut/gut_cmdln.gd …` or the gdUnit4 CLI, producing JUnit XML. (4) `godot --headless --export-release Web build/web/index.html`, serve it locally, and drive it with Playwright/Chrome (SwiftShader WebGL2) for screenshots and visual diffs. (5) Optionally run the native Linux build under `xvfb-run` with `--rendering-driver opengl3` (Mesa llvmpipe) and `--write-movie frame.png --quit-after N` for deterministic frame captures. Step (5) is plausible but untested. Pure `--headless` uses a dummy renderer and cannot produce images.
- Android APK via CLI is feasible once the environment allows `dl.google.com` (or the SDK is pre-baked into the image). JDK 21 is present but JDK 17 is the recommended version. A debug keystore can be generated with `keytool`. Real-device testing (GPU drivers, thermal, touch) cannot happen in the container. Plan a device lab or cloud device farm.
- iOS must be delegated to a macOS runner (e.g. a hosted macOS CI) for export, signing and TestFlight. That is equally true for Unity.
- For Unity, the equivalent loop would need Unity-host network access, a Hub-generated Personal `.ulf` stored as a secret (manual activation unsupported), and multi-GB editor/Android-module images. Feasible on GitHub Actions with GameCI but fragile for an unattended container.

### Gaps
- No hands-on proof that Godot 4.7.2's Compatibility renderer runs correctly under Xvfb + llvmpipe in this exact container (blocked by permission policy). This is the top item to verify first.
- No measurement of web-export screenshot determinism (font hinting and SwiftShader differences) for pixel-diff testing.

---

## Q6. Mobile 2D performance practice (batching, atlases, overdraw, pooling, GC, particles, frame pacing, battery, profiling)

### Takeaway
A tactical autobattler with dozens of sprites is far below mobile limits if you follow the basics. Share textures through atlases so batching works (Godot batches on all renderers since 4.4). Avoid large overlapping translucent layers (tile-based mobile GPUs pay for overdraw). Pool frequently spawned effects. Prefer CPUParticles2D on low-end devices. Cap the frame rate, e.g. 30 fps for menus and 60 fps for combat, to save battery and limit thermal throttling. Profile on real devices (Godot 4.7 adds Perfetto tracing on Android).

### Cited Findings
- 2D batching: "Multiple similar items are grouped together and rendered in a batch, via a single draw call… state changes, material and texture changes can be kept to a minimum" — [godot-docs gpu_optimization.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/performance/gpu_optimization.rst)
- "Batching has been implemented in the Compatibility renderer since the release of 4.0. This release [4.4 dev 3] brings the same performance benefits… when using the Forward+ and Mobile backends (GH-92797). Now 2D performance is comparable between all backends." The benefit is largest for "lots of text rendering or repeated sprites that share a texture (e.g. when using tilemaps…)" — [dev-snapshot-godot-4-4-dev-3.md](https://github.com/godotengine/godot-website/blob/master/collections/_article/dev-snapshot-godot-4-4-dev-3.md) (rendered: [godotengine.org article](https://godotengine.org/article/dev-snapshot-godot-4-4-dev-3/)). Before that, users saw one draw call per sprite on Forward+/Mobile vs one total on Compatibility — [Godot Forum thread](https://forum.godotengine.org/t/vulkan-fails-to-batch-2d-sprites-into-a-single-draw-call/44547). A 4.4-dev regression affected 2D performance generally (383→200 fps in a test scene) — [godot#99420](https://github.com/godotengine/godot/issues/99420). Resolution status not verified.
- Batching knobs: `rendering/2d/batching/item_buffer_size` (default 16384: "Maximum number of canvas item commands that can be batched into a single draw call") and `uniform_set_cache_size` (4096; raising it "can improve performance if the project renders many unique sprite textures every frame") — [ProjectSettings.xml 4.7.2](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/ProjectSettings.xml)
- Batching breaks on texture changes, and painter's order can force extra draws (e.g. wood/grass/wood → 3 draw calls). Mobile GPUs are tile-based, so use the simplest shaders you can afford **(search summary of Godot 4.2–4.5 GPU optimization docs)** — [Godot docs 4.5 GPU optimization](https://docs.godotengine.org/en/4.5/tutorials/performance/gpu_optimization.html)
- Particles: "CPUParticles2D is a CPU-driven option with near-feature parity with GPUParticles2D, but lower performance when using large amounts of particles. On the other hand, CPUParticles2D may perform better on low-end systems or in GPU-bottlenecked situations." There are "no plans to add new features to CPUParticles2D" — [godot-docs particle_systems_2d.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/2d/particle_systems_2d.rst)
- Frame cap and power: `application/run/max_fps` / `Engine.max_fps` — [godot-docs project_settings.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/editor/project_settings.rst). `low_processor_mode` "only redraws the screen if necessary. This may lower power consumption, and is intended for editors or mobile applications. For most games… it is recommended to keep this setting disabled" — [ProjectSettings.xml 4.7.2](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/ProjectSettings.xml)
- Profiling: Godot 4.7 makes **Perfetto** "the default tracing tool for Android editor and template builds… to easily analyze the performance of their games" — [release_4_7 features.yml](https://github.com/godotengine/godot-website/blob/master/_data/release_4_7/features.yml). `--debug-canvas-item-redraw` visualizes redraws for low-processor troubleshooting — [command_line_tutorial.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/editor/command_line_tutorial.rst)
- Memory model: GDScript uses reference counting (no tracing GC pauses). Nodes must be freed explicitly — [gdscript_basics.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/scripting/gdscript/gdscript_basics.rst)
- Unity 6.3 adds a Sprite Atlas Analyser for spotting inefficient packing (secondary source) **(search summary)** — [AlternativeTo](https://alternativeto.net/news/2025/12/unity-6-3-lts-arrives-with-hybrid-2d-3d-scenes-box2d-v3-and-cross-platform-toolkit)

### Inferences
- Budget guidance for this genre (my estimates): under 100 draw calls per frame is trivially achievable with 2–4 atlases (board tiles, units, VFX, UI). Overdraw is the more likely mobile bottleneck: full-screen translucent overlays, stacked UI panels and large additive VFX. Keep full-screen alpha layers to 1–2.
- GDScript avoids C#-style GC spikes, but allocating many Nodes per frame (damage numbers, projectiles) still costs CPU. Pool them, and keep combat logic in plain RefCounted/Object data separate from presentation Nodes. That separation also enables headless simulation (Q8).
- Battery and thermal: set `max_fps` to 60 in combat and 30 in menus/idle. Avoid `low_processor_mode` during animated scenes, but it suits static meta screens. Pixel art at a low internal resolution keeps fill-rate cost tiny, which itself reduces throttling.
- Unity's equivalents (SRP Batcher/2D batching, Sprite Atlas, Profiler, Memory Profiler, Android GPU Inspector) exist but were not verified this session.

### Gaps
- No public 2026 benchmark found comparing Godot Compatibility vs Mobile renderer 2D throughput on low-end Android.
- Godot Android frame pacing (e.g. Swappy integration) was not mentioned in current docs; status unknown.
- Unity mobile 2D performance specifics (incremental GC, SRP Batcher with sprites) unverified.

---

## Q7. Save systems on mobile (location, atomicity, versioning, corruption safety)

### Takeaway
In Godot, save to `user://` (app-private storage; IndexedDB on web) as versioned JSON (or ConfigFile for settings). Write a temp file, then rename it over the target, and keep the previous file as a backup. Include a `save_version` field with migration functions. Unity's equivalent location is `Application.persistentDataPath` (not verified this session).

### Cited Findings
- "To store persistent data files, like the player's save or settings, you want to use `user://` instead of `res://`". The `user://` folder is created per app. "On HTML5 exports, `user://` will refer to a virtual filesystem stored on the device via IndexedDB" — [godot-docs data_paths.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/io/data_paths.rst)
- Godot's official saving tutorial uses the `JSON` helper (`JSON.stringify`, `JSON.parse`) and notes types like `Vector2` are "not supported by JSON" (store x/y separately). It recommends `ConfigFile` for settings-like data — [godot-docs saving_games.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/io/saving_games.rst)
- Godot 4.6 release notes list a "JSON's here!" item, a JSON-related improvement whose details I did not read — [release_4_6 features.yml](https://github.com/godotengine/godot-website/blob/master/_data/release_4_6/features.yml)

### Inferences
- **Atomic write pattern (engine-agnostic):** serialize to `save.json.tmp`, flush and close, rename the current `save.json` to `save.json.bak`, rename tmp to `save.json`. On load, try main, then .bak, then defaults. Add a checksum (e.g. SHA-256 of the payload) to detect truncation. In Godot this uses `FileAccess` plus `DirAccess.rename()`. Rename atomicity on Android/iOS app-private storage is generally reliable on the same filesystem, but test it.
- **Versioning:** a top-level `{"save_version": N, …}` and a chain of pure `migrate_vN_to_vN+1(dict)` functions, unit-tested with golden fixtures under GUT/gdUnit4 in the container.
- **Avoid saving with Godot `Resource` (.tres/.res) files:** loading resources from writable locations can instantiate embedded scripts. Plain JSON is safer and diff-able. This is widely discussed in the Godot community but I could not find the warning in current docs (see Gaps).
- Write on meaningful events (end of battle, purchase), not every frame. Mobile OSes can kill backgrounded apps, so also save on the app-pause notification (`NOTIFICATION_APPLICATION_PAUSED` in Godot; not verified this session).
- Cloud save (Google Play Games / iCloud) needs platform plugins. That is out of scope here and plugin maturity is unverified for Godot.

### Gaps
- No Godot doc found that explicitly documents rename atomicity, or a warning about loading untrusted `.tres` files.
- Unity `Application.persistentDataPath` and `PlayerPrefs` limits not verified (docs domain blocked).

---

## Q8. Data-driven architecture: Godot Resources vs JSON/CSV vs Unity ScriptableObjects, balance spreadsheets and offline simulation

### Takeaway
Keep heroes, abilities and encounters in **spreadsheet-exportable CSV/JSON as the source of truth**, versioned in git and validated by tests. Load or convert them into typed Godot `Resource` classes (or plain dictionaries) at import or startup. Write the combat resolver as **deterministic, presentation-free GDScript** so the same code runs in the game, in `--headless` batch simulations, and in unit tests. Unity's ScriptableObjects give a similar editor-friendly layer but bind data to Unity's asset pipeline.

### Cited Findings
- Godot `Resource` is a RefCounted type (auto-freed when unused) — [gdscript_basics.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/scripting/gdscript/gdscript_basics.rst)
- Godot natively imports CSV for translations, and 4.6 improved "Spreadsheet-based localization… optional `?context` columns… `?plural` columns" and generation of CSV translation templates — [release_4_6 features.yml](https://github.com/godotengine/godot-website/blob/master/_data/release_4_6/features.yml)
- Godot can run arbitrary scripts headless (`--headless` is "Useful for servers and with `--script`") — [command_line_tutorial.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/editor/command_line_tutorial.rst)
- The JSON helper converts between Dictionary and string — [saving_games.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/io/saving_games.rst)

### Inferences
- **Recommended data flow:** Google Sheets/Excel → CSV export (or JSON via a script) → `data/*.csv` in git → a Godot `EditorImportPlugin` or a startup loader builds typed `HeroDef`/`AbilityDef` Resources → the runtime reads only typed defs. Schema validation (required columns, ID references, value ranges) runs as a unit test in CI.
- **Simulation:** a `CombatSim` class with a seeded RNG and no Node dependencies can be invoked by `godot --headless -s tools/sim.gd -- --matchups 10000 --out results.csv`. Python/pandas then analyzes win rates. Alternatively, duplicate the rules in Python, at the risk of drift; using the engine's own code is safer.
- `.tres` text resources are fine for hand-tuned one-off content (VFX configs, UI themes), but spreadsheets are better for bulk balance numbers (diff-friendly, accessible to designers, usable outside the engine).
- Unity equivalent: ScriptableObjects plus a CSV importer. Batch simulation would need Unity batchmode (license activation, Q3) or a separate pure-C# assembly runnable with `dotnet test`. That works, but it is extra architecture to keep engine-independent.

### Gaps
- No primary source compared performance of loading thousands of `.tres` files vs JSON on mobile.
- No Unity ScriptableObject documentation could be retrieved this session.

---

## Q9. Shipped games as evidence of viability

### Takeaway
Godot's commercial track record now includes major hits: *Slay the Spire 2* (moved from Unity to Godot; early access Mar 5, 2026; reported ~575K peak CCU), *Brotato*, *Dome Keeper*, *Cassette Beasts*, *Halls of Torment* and *Buckshot Roulette*. But Godot's own showcase lists these mostly for PC/console. **Mobile-first Godot hits are rarer.** *Brotato* did launch on iOS/Android, but I could not verify which engine its mobile port uses.

### Cited Findings
- *Slay the Spire 2*: Mega Crit had spent over two years in Unity, then switched to Godot after the 2023 runtime-fee policy. Unity reversed the fee, but Mega Crit stayed with Godot. It made *Dancing Duelists*, "an auto-battling deckbuilder", to "explore the Godot engine". Mega Crit is a major Godot sponsor. Early access released March 5 (2026) **(search summary)** — [PC Gamer](https://pcgamer.com/games/card-games/slay-the-spire-2-ditched-unity-for-open-source-engine-godot-after-2-years-of-development); [Game Developer](https://gamedeveloper.com/business/slay-the-spire-devs-followed-through-on-abandoning-unity); [GamingOnLinux](https://www.gamingonlinux.com/2023/10/slay-the-spire-devs-release-dancing-duelists-after-abandoning-unity-for-godot/page=1/); [Wikipedia: Slay the Spire II](https://en.wikipedia.org/wiki/Slay_the_Spire_II). Peak of nearly 575,000 concurrent players **(search summary)** — [gamedev.net](https://gamedev.net/news/2020-slay-the-spire-2-hits-nearly-575000-concurrent-players-almost-beating-silksongs/). Godot showcase entry: Mega Crit, dated 2026-03-05, platforms windows/macos/linux — [godot-website showcase/slay-the-spire-2.md](https://github.com/godotengine/godot-website/blob/master/collections/_showcase/slay-the-spire-2.md)
- Godot showcase entries (official platform tags): *Brotato* (Blobfish) — windows, playstation; *Dome Keeper* (Bippinbits) — windows, macos, linux; *Cassette Beasts* (Bytten Studio) — windows, linux, switch, xbox; *Halls of Torment* (Chasing Carrots) — windows, linux; *Buckshot Roulette* (Mike Klubnika) — windows, linux, switch, playstation, xbox — [godot-website collections/_showcase](https://github.com/godotengine/godot-website/tree/master/collections/_showcase)
- *Brotato* launched on iOS and Android as a $4.99 premium release via Erabit Studios. The article does not name the engine of the mobile build **(search summary)** — [Pocket Gamer](https://www.pocketgamer.co.uk/brotato/release/)
- Android titles *Rift Riff* and *Kamaeru* are cited by Godot as shipping on Google Play with the Mobile renderer (their crash logs drove 4.6 fixes) — [release_4_6 features.yml](https://github.com/godotengine/godot-website/blob/master/_data/release_4_6/features.yml)
- *Xogot* (Godot editor for iPad/iPhone, by Xibbon) is in Godot's showcase, which shows Godot's runtime operating as a native iOS app — [godot-website showcase/xogot.md](https://github.com/godotengine/godot-website/blob/master/collections/_showcase/xogot.md)

### Inferences
- Godot is proven for commercial 2D and pixel art on PC and console, and is credible on mobile (Rift Riff, Kamaeru, Xogot). The mobile evidence is thinner than Unity's, whose dominance on mobile is well known but was not sourced this session.
- *Slay the Spire 2*'s move matters here as a genre-adjacent case: turn- and tactics-adjacent roguelike UI-heavy 2D, made by a small studio. It shows Godot handles UI-dense 2D games at scale.

### Gaps
- Engine of *Brotato*'s mobile port unverified. Whether *Dome Keeper*, *Cassette Beasts* or *Halls of Torment* have mobile versions unverified.
- No sourced list of Unity pixel-art mobile hits was collected this session.

---

## Q10. Recommendation for this project (engine, architecture, risks)

### Takeaway
**Choose Godot 4.7.x (stable) with GDScript and the Compatibility renderer.** Use a low-resolution portrait logical canvas (~180–270 px wide) at integer scale with an expanding play area. Use nearest filtering and lossless textures, with the UI either pixel-scaled at integer multiples or in a native-resolution layer. Make combat a deterministic, data-driven core runnable headless. Godot is the only evaluated engine that meets *all* of: native Android/iOS export, a strong pixel-art feature set, a free MIT license, and a fully scriptable headless Linux workflow (install, test, web build, screenshots) with no license activation. Revisit 4.8 after its first patch release.

### Cited Findings
- Integer scaling, viewport stretch and 2D snap settings exist and are documented for pixel art — [multiple_resolutions.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/multiple_resolutions.rst); [ProjectSettings.xml 4.7.2](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/ProjectSettings.xml)
- Compatibility is recommended for 2D, low-end mobile and web, and launches faster — [renderers.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/rendering/renderers.rst); [creating_applications.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/ui/creating_applications.rst)
- `--headless` CLI export and testing are officially supported for CI — [command_line_tutorial.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/editor/command_line_tutorial.rst); [gdUnit4](https://github.com/MikeSchulze/gdUnit4); [GUT](https://github.com/bitwes/Gut)
- C# on mobile is experimental and has no web export — [c_sharp/index.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/scripting/c_sharp/index.rst)
- Unity Personal cannot be manually activated for headless CI — [GameCI common issues](https://github.com/game-ci/documentation/blob/main/docs/09-troubleshooting/common-issues.mdx)
- iOS requires macOS + Xcode regardless of engine — [exporting_for_ios.rst](https://github.com/godotengine/godot-docs/blob/master/tutorials/export/exporting_for_ios.rst); [GameCI iOS](https://github.com/game-ci/documentation/blob/main/docs/03-github/06-deployment/ios.mdx)

### Inferences
**Concrete starting configuration (Godot 4.7.x):**
1. Renderer: `gl_compatibility` (mobile + web). Window: portrait. Base viewport e.g. 180×320 (chunky, 4–8× scale) or 270×480 (finer detail, 2–5×). Stretch: `viewport`, aspect `expand`, scale mode `integer`. Default texture filter: Nearest. `snap_2d_transforms_to_pixel = true`. Leave `snap_controls_to_pixels` on (default). Textures imported Lossless, no mipmaps, in atlases per domain (units, tiles, VFX, UI).
2. A fixed "safe core" board that fits the base resolution, with expandable decorative margins. HUD anchored to the screen edges inside `DisplayServer.get_display_safe_area()`.
3. Text: pixel bitmap fonts at integer multiples for Latin. For CJK, plan a native-resolution UI layer (canvas_items in a separate CanvasLayer/SubViewport arrangement) with a dynamic font.
4. Combat core: pure GDScript data classes with a seeded RNG, no Nodes, driven by CSV/JSON defs. The presentation layer subscribes to combat events (pooled sprites and effects).
5. Saves: versioned JSON in `user://`, atomic temp-and-rename with a .bak copy, migration tests.
6. Container CI: download the pinned editor and only the Web/Android templates, `--headless --import`, gdUnit4 or GUT with JUnit output, headless balance-sim jobs, web export, Playwright screenshots and golden-image diffs. Android APK via CLI once the Android SDK host is allowed (or pre-baked). iOS on a macOS runner later.
7. Frame policy: 60 fps in combat, 30 fps in idle/meta screens (`Engine.max_fps`). CPUParticles2D for low-end. Profile with Perfetto on a low-end Android device early.

**Key risks and mitigations**
- *Mobile platform services* (IAP, ads, cloud save, push) depend on Godot plugins whose 2026 maturity was not verified. **Mitigation:** spike Google Play Billing and StoreKit integration in month 1. If it blocks, Unity becomes the fallback (accepting the CI cost).
- *Android GPU driver variance:* Compatibility avoids the Vulkan crash class fixed in 4.6, but test on Mali, Adreno and PowerVR low-end devices (cloud device farm).
- *Shader-compile hitches on Compatibility* (no ubershaders): keep custom shaders few and pre-warm them on the loading screen.
- *Integer-scale edge cases* (remainder bars, tablets revealing much more world): prototype the board on 20:9, 19.5:9 and 4:3 in week 1 using web export at device resolutions in Playwright.
- *Version churn:* pin to 4.7.x and upgrade deliberately. gdUnit4 and GUT track Godot minors (gdUnit4 v6.2 → 4.5–4.7.1).
- *iOS:* needs an Apple Developer account plus a macOS build host. The container cannot do it for either engine.
- *Unity fallback cost:* $0 under $200K revenue (splash optional), about $2,310/seat/yr Pro above that. The main cost is CI and licensing friction in containers, not money.

### Gaps
- Top verification tasks before committing: (1) run Godot 4.7.2 headless import, tests and web export in this container, and capture screenshots via Chrome. (2) Allow `dl.google.com` and test a CLI Android debug APK export. (3) Spike IAP/ads plugins for Godot 4.7 on Android and iOS. (4) Measure APK size and cold start on a low-end Android device.
- GameMaker, LÖVE and Defold CLI specifics were not verified (search budget exhausted).
