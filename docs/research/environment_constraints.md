# Development environment constraints (verified 2026-11-23)

This file records what was **actually tested** in the cloud development
container used for this project, because these facts constrain engine choice,
asset production, and what can be honestly verified.

## Hardware / OS
| Item | Result |
|---|---|
| OS | Linux (container), 4 vCPU, 15 GiB RAM, no GPU |
| Display | none (headless) |
| Python | 3.13 with Pillow 12.3 and NumPy 2.5 available |
| Node.js | v22 available |
| Java | OpenJDK 21 available (needed for Android/Gradle builds) |
| ffmpeg | available (`/usr/bin/ffmpeg`), useful for audio conversion and preview video |
| Browser | Chromium + Playwright pre-installed (headless screenshots possible) |
| Godot / Aseprite / Unity | **not installed** |

## Network policy (probed with curl through the session proxy)
| Host | Result | Consequence |
|---|---|---|
| `registry.npmjs.org` | 200, allowed | npm packages installable |
| `pypi.org` | 200, allowed | pip packages installable |
| `api.github.com`, `github.com/.../releases` | 403, blocked by policy | Godot binaries (hosted on GitHub releases) cannot be downloaded without an environment change |
| `godotengine.org`, `downloads.godotengine.org` | no connection, blocked | same |
| `dl.google.com` (Android SDK repository) | no connection, blocked | Android SDK command-line tools cannot be fetched without an environment change |
| `maven.google.com`, `services.gradle.org`, `repo.maven.apache.org` | 200, allowed | Gradle/Android build dependencies resolvable once an SDK exists |

## What this means
* **Asset production:** sprites are authored as text grids and compiled with
  `tools/pixelforge` (Python and Pillow). This works today, and a first
  feasibility spike is in `docs/research/art_spike/`.
* **Godot:** usable here only if the user approves allowing the Godot
  download host(s) for this environment, or provides the binary another way.
  Once present, Godot runs headless for tests, imports and web exports.
* **Unity:** not practical in this container (large editor download from
  blocked hosts, licence activation, no GPU).
* **Web stack (TypeScript + a 2D WebGL renderer + Capacitor):** fully
  buildable and testable here today through npm and Playwright.
* **iOS builds** need macOS and Xcode under any engine. They cannot be
  produced from this container.
* **Android builds** need the Android SDK. Its repository host
  (`dl.google.com`) is blocked, but Gradle and Maven hosts are allowed. A
  signed APK from this container needs one environment change, or a local or
  CI machine.

These constraints are an input to the engine decision in the proposal, not
the whole decision.
