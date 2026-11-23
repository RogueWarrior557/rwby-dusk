# King God Castle (킹갓캐슬): Combat and Hero Systems

> **How these notes were made, and where they are weak (read first).** Research date: 23 Nov 2026. In this session WebFetch could not reach any host: `store.steampowered.com` and `namu.moe` both failed DNS resolution in the sandbox. Partway through, the shared web-search budget also ran out. As a result, **every finding below comes from search-engine result snippets and summaries of the cited pages, not from reading the full pages.** Each URL is the page the snippet came from. Exact numbers came from those snippets and may be out of date or paraphrased. The most detailed sources are NamuWiki (Korean, plus its machine-translated mirror en.namu.wiki) and the community Fandom wiki (kgc.fandom.com). Both are fan-edited, and many of their pages are 1–3 years old. Store changelogs and Google Play reviews give the 2025–2026 state of the game. Labels used throughout: **[CURRENT]** = confirmed for 2025–2026; **[HISTORICAL]** = removed or changed; **[UNDATED]** = no reliable date, so it may be stale.

---

## 1. Developer, publisher, release dates, platforms, orientation, current version and update status

### Takeaway
AWESOMEPIECE (어썸피스) develops King God Castle. The studio also made *Zombie High School*. The game launched on iOS and Android on 19 Oct 2020. It was still getting regular "Season" updates in November 2026: Season 75, version 175.0.02, dated 7 Nov 2026. Its store title is now "King God Castle: Luminous Fate". **I found no evidence of a Steam release.** The brief's "mobile/Steam" premise looks wrong. The only PC route I found is Google Play Games for PC.

### Cited Findings
- AWESOMEPIECE (어썸피스) is the developer. Its best-known titles are 좀비고등학교 (*Zombie High School*) and 킹갓캐슬 — [NamuWiki mirror: Awesomepiece](https://namu.moe/w/Awesomepiece) (search snippet; the page itself could not be fetched). Google Play also names the developer as AWESOMEPIECE. The package ID is `com.awesomepiece.castle` — [Google Play (US)](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_US).
- The Korean release date was **19 Oct 2020**. NamuWiki calls the game a "defense-type strategy game" (디펜스형 전략 게임) — [NamuWiki 킹갓캐슬](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC). Metacritic lists an iOS release on 19 Oct 2020, with a user score of 6.8 from only 4 ratings — [Metacritic](https://www.metacritic.com/game/king-god-castle/). TapTap lists Android on 10/19/2020 — [TapTap reviews](https://www.taptap.io/app/201530/review).
- **The store title has changed several times.** All of these names belong to the same App Store ID, 1526791430:
  - "King God Castle: Merge Defense" — [App Store TH](https://apps.apple.com/th/app/king-god-castle-merge-defense/id1526791430)
  - "Defense RPG" — [Google Play NZ](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_NZ), [TapTap](https://www.taptap.io/app/201530)
  - "Strategy RPG" — [Google Play CA](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_CA&gl=KR)
  - "Pixel RPG" — [App Store IS](https://apps.apple.com/is/app/king-god-castle-pixel-rpg/id1526791430)
  - "**Luminous Fate**" (the current name) — [Google Play US](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_US), [App Store SA](https://apps.apple.com/sa/app/king-god-castle-luminous-fate/id1526791430)
  - The Korean title is "킹갓캐슬: 빛의 운명" ("Fate of Light") — [program.download](https://program.download/king-god-castle/)
- The current Google Play pitch reads: "Merge pixel art heroes, build your squad RPG strategy, and unleash powerful auto battler combat to claim victory" — [Google Play US](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_US).
- **Latest version [CURRENT]:**
  - **175.0.02, 7 Nov 2026**, labelled "Season 75 – 1 New Skin – Bug fixes – Fix localizing issue". Versions 175.0.00 and 175.0.01 came out on 5–6 Nov — [Aptoide](https://com-awesomepiece-castle.en.aptoide.com/app).
  - Google Play shows Season 75 dated 5 Nov 2026 — [Google Play US](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_US).
  - Earlier 2026 snapshots: 172.0.01 "Season 72", 20 Aug 2026 — [Soft112](https://kinggodcastle.soft112.com/); 172.1.00, 25 Aug 2026 — [AppBrain](https://www.appbrain.com/app/kinggodcastle/com.awesomepiece.castle).
  - Back in 2025, v157.1.00 was dated 2 Jul 2025 — [iPa4Fun version history](https://www.ipa4fun.com/history/448637/).
- **Live-ops signals for 2025–2026 [CURRENT]:**
  - The hero level cap rose from 20 to 30 in an update on 10 Sep 2025 — [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
  - The "late team" system was deleted on 3 Dec 2025 and replaced by a "starting-hero" system. The roster stood at 69 heroes "as of January 10th" (2026, from context) — [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
  - On Google Play, dated 21 Aug 2026, the developer said it would review progression balance and reward accessibility. This followed complaints about hero medals past level 25 and about the "Cube of Power" — [Google Play US](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_US).
  - An App Store listing advertised a "5th Anniversary Event". One listing reportedly offered "Get all heroes for free!" for the 5.5th anniversary, but I could not confirm the date or the terms — [App Store SA](https://apps.apple.com/sa/app/king-god-castle-luminous-fate/id1526791430), [App Store IS](https://apps.apple.com/is/app/king-god-castle-pixel-rpg/id1526791430).
  - A code list includes `KGC5POINT5CELEBRATE`, "valid until April 30th, 2026" — [Clashiverse codes](https://clashiverse.com/king-god-castle-codes/).
- **Producer (PD) changes:**
  - A PD called "Equester" posts developer letters on the official notice site — [kgcastle-notice.awesomepiece.com](https://kgcastle-notice.awesomepiece.com/1e51c2e0-6f0e-809b-9fb9-d04e86f96f71).
  - An earlier PD, "Crocodilemon" ("MrCroco" in the community), wrote a letter during the relic-option controversy — [en.namu Artifact Option Reorganization Controversy](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC%20%EC%9C%A0%EB%AC%BC%20%EC%98%B5%EC%85%98%20%EA%B0%9C%ED%8E%B8%20%EB%85%BC%EB%9E%80).
  - Related community videos: "HUGE NEWS no more MrCroco" — [YouTube](https://www.youtube.com/watch?v=PWXD9FjHv3w); "KING GOD CASTLE'S FUTURE.. IS IT DEAD?" — [YouTube](https://www.youtube.com/watch?v=l4bRtIrYlSA); "...SAVED?!" — [YouTube](https://www.youtube.com/watch?v=SCWvfvM1ztg).
- **There are two version-number schemes.** Store builds run 157 to 175. Community "patch" numbers look different: "Patch 5.3.4" tied to Season 42 — [YouTube rundown](https://www.youtube.com/watch?v=LnDBOCzr3Yk); "update 6.4.8" (hero Ivi) — [TierMaker](https://tiermaker.com/categories/video-games/king-god-castle-saras-new-hero-update--528-713596).
- **Content droughts [HISTORICAL]:** NamuWiki says new content slowed down. Raid (습격), the main mode, got no new chapters after Chapter 10 in 2022, until "Raid Season 2" arrived on 8 Feb 2024 — [NamuWiki 킹갓캐슬](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC), [NamuWiki 비판 및 논란 (criticism)](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%B9%84%ED%8C%90%20%EB%B0%8F%20%EB%85%BC%EB%9E%80).
- **Steam:**
  - A search scoped to Steam found no King God Castle store page. It returned "KING GOD DOMAIN" (app 1383670, a turn-based card game with Mixed reviews, relationship to KGC unknown) and unrelated "King of the Castle" titles — [Steam app 1383670](https://store.steampowered.com/app/1383670).
  - Google Play has a "Play on PC" (Google Play Games) listing — [Google Play PC store](https://play.google.com/pc-store/games/details?id=com.awesomepiece.castle).
  - The NamuWiki Awesomepiece snippet says King God Castle "was to be" the studio's first PC and Nintendo Switch single-player story game. The sentence is in the future tense ("예정이었다"), and I found no evidence that such a release happened — [namu.moe Awesomepiece](https://namu.moe/w/Awesomepiece).
- **Conflicting signal on service status:** NamuWiki's Awesomepiece page reportedly lists 킹갓캐슬 under "games that ended service" — [namu.moe Awesomepiece](https://namu.moe/w/Awesomepiece), [NamuWiki 킹갓캐슬 (category)](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC). Store changelogs contradict this: they show Season 75 shipping in Nov 2026 — [Aptoide](https://com-awesomepiece-castle.en.aptoide.com/app). No shutdown notice turned up in English or Korean searches.

### Inferences
- From the numbering (Season 72 in Aug, 73 in Sep, 75 in early Nov 2026), seasons appear to run about monthly. Store version numbers track season numbers (17**5** ≈ Season **75**).
- The "ended service" category on NamuWiki probably refers to a different edition or a regional or third-party publishing deal, or it is a categorisation error. The global build is clearly still live. The report should not claim the game has shut down.
- Each rename (Merge Defense → Defense RPG / Strategy RPG → Pixel RPG → Luminous Fate) was probably a store-optimisation repositioning, not a new game. The core combat loop appears unchanged across the renames.

### Gaps
- **Publisher:** I found no separate publisher. It is probably self-published by AWESOMEPIECE, but I could not verify this.
- **Orientation (portrait or landscape):** I could not verify it from any source I reached. My unverified recollection is portrait. Check a store screenshot.
- **Steam:** I could not confirm whether a Steam version exists, or ever existed. The Steam store could not be fetched, and searches found none.
- I could not read the contents of the latest Equester letter, the exact date the "Luminous Fate" rename happened, or what the rename changed.

---

## 2. Battlefield layout: grid, deployment zones, the castle, units fielded, waves

### Takeaway
Combat takes place on a tile grid. Heroes deploy into a player-side "camp/formation" (진영) that grows over a run as you spend in-run silver to expand it. One deck guide grows it from 4 slots to 8–10 by round 5. The game uses row and adjacency language (Row 1 / front line, back line, "2 tiles horizontally", 3×3 and 5×5 areas). The castle works as a run-level HP pool called "castle durability". Runs advance round by round, including elite rounds, against enemy waves and bosses. **I could not verify the exact grid dimensions.**

### Cited Findings
- At the start of a run you receive silver. You spend it to summon heroes and to **expand your formation**. You strengthen your camp through smelting, merchant purchases and "devil's suggestions", then clear the enemies on the field to move to the next round — [en.namu King God Castle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC).
- **Camp size grows round by round.** One season-specific deck guide gives camp expansion of 4-4-6-7-10 for rounds 1-2-3-4-5. Another deck uses 4-4-5-6-8. In one deck, "the more heroes there are, the less damage you receive", up to −40% with 10 heroes placed — [en.namu Deck](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1) [UNDATED, older seasons].
- **Rows matter.**
  - The Giant Altar gives every hero in **Row 1** a damage-reflection buff — [Mejoress altar guide](https://www.mejoress.com/en/king-god-castle-best-altars-to-choose-for-your-team/) [UNDATED].
  - NamuWiki describes a hero who changes form depending on placement: a bruiser-tank (딜탱) in the front row (전열), a ranged carry (원딜) in the back row (후열) — [NamuWiki 캐릭터 정보](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
- **Adjacency and area effects:**
  - A Great Rift "front-line rune" (전열 룬) grants Absolute Defense +2/4/6 charges at battle start to the hero and to allies within 2 tiles horizontally (up to 5 heroes). NamuWiki notes that this is why teams are arranged horizontally — [NamuWiki 대균열/룬 (Great Rift runes)](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8C%80%EA%B7%A0%EC%97%B4/%EB%A3%AC).
  - Grouped "Courage"-class heroes give allies in a **5×5 area** a shield at battle start — [en.namu Battlefield/Strategy](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EA%B2%A9%EC%A0%84%EC%9D%98%20%EC%A0%84%EC%9E%A5/%EC%A0%84%EB%9E%B5).
  - Bombie's passives add splash in a **3×3 area** around the target — [kgc.fandom Bombie](https://kgc.fandom.com/wiki/Bombie).
- **Tile-specific buffs:** The Arena relic "Shard of the Blessed Relic" (축복의 성물 파편) blesses **one tile**. A hero on that tile concentrates for 2 s after battle starts, then deals +35/50/65/80% damage — [NamuWiki 유물 (relics) r258](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%9C%A0%EB%AC%BC?uuid=aa8b80e2-577c-45d8-a1c1-4563d5639c55) [UNDATED].
- **Enemy reach is measured in tiles.** One Raid chapter's monsters detect targets up to 8 tiles forward (전방 8칸). Vampire-raid monsters do not attack the back line — [NamuWiki 캐릭터 정보 / 습격 pages](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
- **The castle as HP:** In each stage, a devil's offer gives an item in exchange for a penalty. Penalties include more or higher-level monsters, or **reduced castle durability** — [en.namu Raid/Demon Defense Battle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EB%A7%88%EB%AC%BC%20%EB%B0%A9%EC%96%B4%EC%A0%84).
- **Rounds:** Elite rounds exist, and an altar skill pays silver for them (see §5). The 100 silver granted at the start "cannot be used after the first battle" — [en.namu King God Castle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC), [en.namu Tips](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%ED%8C%81).
- **Great Rift is a separate mode.** Each floor is randomly regenerated with 11 tiles — [kgc.fandom Great Rift](https://kgc.fandom.com/wiki/Great_Rift).

### Inferences
- The battlefield looks like a **two-sided tile board**: player heroes in a bottom or front formation, enemies advancing from the far side. Melee units close the gap, ranged units fire across it, and enemy aggro ranges are counted in tiles. The 8-tile monster detection range and the 5×5 shield area suggest a grid at least 5 tiles wide.
- "Castle durability" probably acts as a meta-HP for the run. Losing rounds, or accepting devil penalties, wears it down, and the run fails at zero. That is why the "castle" in the title matters mechanically. I could not verify exactly what reduces it besides devil offers.
- Expanding the formation competes with summoning for the same silver. This is a classic auto-battler width-versus-depth tension (see §3).

### Gaps
- Exact grid dimensions, the maximum camp size, and whether enemies hit the castle directly when they pass the heroes.
- Waves per stage and stages per chapter.
- Whether the "King" is a combat entity. I found no "king skill" or castle-cast ability in any source (see §4 Gaps).

---

## 3. Unit deployment, merging, star grades, deck composition and positioning rules

### Takeaway
Within a run you summon heroes with silver. As far as the sources show, the summons come at random from your pre-built deck of **6 hero types**. **Identical heroes merge**, raising their star grade up to **7★**, grouped into four power tiers. You choose each hero's tile. The run tension is spreading silver across more bodies (formation slots) versus stacking stars on a few carries. Relics push this to extremes in both directions: "solo carry" relics versus "many copies of one hero" relics. The "late team" (후발대) system was removed on 3 Dec 2025 **[HISTORICAL]**. It controlled what the early summons produced, and it had become the dominant strategy. A "starting-hero" system **[CURRENT]** replaced it.

### Cited Findings
- **Star merging [CURRENT, as of 2025–26 wiki]:** Heroes gain stars by combining duplicates, up to 7. Stars 1–2 are tier 1, 3–4 tier 2, 5–6 tier 3, and 7 is tier 4. Higher stars raise attack speed, ability (spell) power, attack power and health — [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4); also in Korean: "성급이 올라가면 영웅의 공격 속도, 주문력, 공격력, 체력이 올라간다" — [NamuWiki 캐릭터 정보](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4). Players and store copy describe merging identical heroes into stronger units, with grid positioning mattering — [App Store US](https://apps.apple.com/us/app/king-god-castle/id1526791430), [TapTap](https://www.taptap.io/app/201530).
- **Silver value by star:** A fan-wiki summary puts a hero's silver value at 2 silver for 1★, rising to 40 silver for 7★. The snippet said "summoning returns silver", which probably means the sell or refund value. Treat it as ambiguous — [en.namu Tips](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%ED%8C%81).
- **Deck of 6:**
  - One deck archetype pairs 5 late-team heroes with 1 main damage dealer ("후발대 5명과 메인 딜러 1명"). Starting round 1 with only the main hero summoned was commonly called the "one-man deck" (원맨덱) — [NamuWiki 팁](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%ED%8C%81).
  - A NamuWiki snippet says all 6 heroes must be filled before a battle can start ("영웅을 6명 전부 채워야만 전투를 시작할수 있다") — [NamuWiki 덱](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1) / [NamuWiki 캐릭터 정보 r1862](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4?uuid=5a3eae9d-0b18-478c-ab5b-0fc1d7f11468).
- **Late team (후발대) [HISTORICAL; removed 3 Dec 2025]:**
  - Late-team heroes did not appear in the first 8 summons in Raid or Expedition — [NamuWiki 팁](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%ED%8C%81), [DCinside KGC gallery guide](https://m.dcinside.com/board/kinggodcastle/23621).
  - They also did not appear while 3 or fewer heroes had been summoned in round 1. This applied in Raid, Strong-Enemy Raid and Hero Raid. It did **not** apply in 격전 ("Fierce Battle") — [DCinside](https://gall.dcinside.com/mgallery/board/view/?id=kinggodcastle&no=33254), [Arca.live high-chapter late-team guide](https://arca.live/b/kinggod/69747856?p=1).
  - In high chapters, monsters are strong from the start, so a late team was "practically mandatory" to avoid early collapse — [Arca.live](https://arca.live/b/kinggod/69747856?p=1).
  - NamuWiki says the system was originally meant to prevent early losses to heroes that don't attack. It "degenerated into King God Castle's most important strategy and entry barrier" — [en.namu Tips](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%ED%8C%81), [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
  - It was deleted on 3 Dec 2025 and replaced by a new starting-hero system — [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
  - Compensation for the "advance party" came up in a PD letter during the relic-option controversy — [en.namu Artifact Option Reorganization Controversy](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC%20%EC%9C%A0%EB%AC%BC%20%EC%98%B5%EC%85%98%20%EA%B0%9C%ED%8E%B8%20%EB%85%BC%EB%9E%80).
- **Relics that reward headcount extremes:**
  - **Rapid Sword** raises attack speed based on how many identical characters are on the field. One guide says it gives no extra bonus beyond 5 — [LevelsXP beginner guide](https://levelsxp.com/king-god-castle/beginners-guide/) (about 2024), [games.lol guide](https://games.lol/blog/king-god-castle-guide/) (about 2023).
  - Another relic (named 잠식, "Encroachment", in the Korean snippet) grows stronger the fewer heroes you deploy. It peaks at +60% with 1 hero and gives nothing at 6 or more. It is "the core relic for solo play" — [NamuWiki 유물 r258](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%9C%A0%EB%AC%BC?uuid=aa8b80e2-577c-45d8-a1c1-4563d5639c55) [UNDATED].
  - The **Mask** relic supports "solo builds", paired with the Blacksmith Altar — [Mejoress](https://www.mejoress.com/en/king-god-castle-best-altars-to-choose-for-your-team/).
- **Archetype example, "Aramis Gang" [UNDATED, flagged outdated]:**
  - Run at least 5 Aramis (rifle DPS), with Leonhardt as main tank and Lily, Lyca, Bardrey and Alberion as fillers. Pair with Rapid Sword and Penetrating Spear — [kgc.fandom Builds](https://kgc.fandom.com/wiki/Builds).
  - Alternatively, 6 Aramis in the back lane plus 2 Leonhardt as tanks — [TouchTapPlay guide](https://www.touchtapplay.com/king-god-castle-strategy-guide-tips-cheats-and-more/).
- **Positioning:** Tanks such as Leonhardt go in front and DPS such as Evan goes behind — [LevelsXP](https://levelsxp.com/king-god-castle/beginners-guide/), [kgc.fandom Builds](https://kgc.fandom.com/wiki/Builds). Placement matters more as enemies get stronger — [en.namu Tips](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%ED%8C%81).
- **Awakening affects deployment.** In a Kain deck (Seasons 28–30), the support Mara "must be awakened" and "2+ should be deployed" — [NamuWiki 덱](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1).
- Players build enough team variety that a community tool, "kgc-companion", exists for sharing King God Castle teams — [davidward.dev](https://davidward.dev/posts/project-kgc-companion/).

### Inferences
- The loop reads as a **draft-and-merge roguelite inside a tower-defence wrapper**. Random summons from a 6-type deck plus merging to 7★ create the "will I hit my carry?" tension of auto-chess. The fixed, player-built deck reduces chaos compared with a shared pool.
- Relics that pay out at **1 hero** (solo) or at **≥5 copies of one hero** give runs a sharp identity and make the build decision early and binding. But they also squeeze the middle ground of balanced teams.
- The rise and removal of the late team is a useful cautionary tale. A **safety valve** (protecting early rounds) turned into a deterministic summon-manipulation tool. It became mandatory knowledge and gated new players. Any system that lets players predict or force early RNG risks becoming the meta.

### Gaps
- How the current (post Dec 2025) **starting-hero system** works: whether you pick one guaranteed hero, how many, and whether it is free.
- Exact summon cost, whether summons can be rerolled or locked, and whether merging is automatic or manual (drag-to-merge).
- Whether there is a bench, and whether heroes can be repositioned between rounds or mid-round.

---

## 4. Combat flow: targeting, movement, range, attack speed, mana, abilities, damage types, defenses, CC, healing/shields

### Takeaway
Combat runs automatically in real time. Heroes basic-attack, gain **mana from attacking (15 per basic attack) and from being hit**, and auto-cast their skill when mana is full. Skill costs vary by hero. The defensive design rests on **count-based "Absolute Defense" (절대방어) charges** alongside "spell defense" and "Protection" shields. This produces a hit-count versus damage-per-hit interplay: multi-hit attacks and specific bosses bypass it. Targeting is usually front-to-back, with exceptions such as assassins aiming at the farthest enemy. **I found no player-cast "king" or castle skill.**

### Cited Findings
- **Mana:** Heroes recover a set amount of mana when they attack or are hit, and cast their skill once enough is gathered ("피격당하거나 공격하면 마나를 일정량 회복하게 되고, 필요한 양의 마나가 모이면 스킬을 사용한다"). One basic attack yields **15 mana**. Skill costs differ by hero: Jupiter's skill costs 15, so he casts on every basic attack ("스킬 딜러") — [NamuWiki 캐릭터 정보](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
- **Recast-lock change [HISTORICAL → CURRENT]:** The hero Yeon (연) used to be able to recast whenever mana filled. Now Yeon cannot cast again until the current skill finishes, even with full mana — [NamuWiki 캐릭터 정보](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
- **Targeting and range:**
  - Lyca (라이카) always targets the enemy farthest from herself, ignoring front and back rows, so she can hit the rearmost damage dealer — [NamuWiki 캐릭터 정보](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
  - Bambi (밤비) is a long-range dealer with long range on both basic attack and skill — [same source](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
  - Bombie throws bombs at **random** enemies — [kgc.fandom Bombie](https://kgc.fandom.com/wiki/Bombie).
  - Monsters have per-type aggro ranges (8 tiles forward in one chapter; back line ignored by vampire-raid monsters) — see §2.
- **Stats:** Guides rate heroes on health, spell power, attack speed and passive skills — [LevelsXP tier list](https://levelsxp.com/king-god-castle/tier-list/). Stars raise ATK, SP, attack speed and HP (§3).
- **Damage types and formulas (examples) [UNDATED]:**
  - **Aramis – Headshot:** fires a powerful bullet at a single target for "physical normal damage" of (130/150/170/200 + SP×0.02)% of ATK. Another guide says it scales with spell power instead of ATK. The two sources conflict — [kgc.fandom Heroes](https://kgc.fandom.com/wiki/Heroes), [eXputer tier list](https://exputer.com/guides/tier-lists/king-god-castle-tier-list/).
  - **Leonhardt – Smite:** a shield bash for 30/40/50/60 + SP damage that **stuns** for 1.5/2/2.5/3 s. Its reach grows at higher levels — [eXputer](https://exputer.com/guides/tier-lists/king-god-castle-tier-list/).
  - **Bombie – Rain of Bombs:** throws bombs at random enemies with +60/120/180/240% attack speed for (3/4/5/6 + SP/50) s. Passives at hero level 4 and level 8 add 3×3 splash — [kgc.fandom Bombie](https://kgc.fandom.com/wiki/Bombie).
  - **Luniare – Blessing of the Blue Moon:** concentrates for 5 s, then grants 15/60/120/250 + SP **Protection** to a linked target and converts a share of her ATK and SP into that target's stats — [kgc.fandom Heroes](https://kgc.fandom.com/wiki/Heroes).
  - In these examples, skill values come in four steps. That matches the four star tiers (§3).
- **Absolute Defense (절대방어) and spell defense:**
  - The altar grants Absolute Defense twice at battle start to all heroes, or three times at altar level 15. The Altar of Blood gives 2/3/4/5 charges at level 10 and above — [en.namu Raid/Demon Defense Battle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EB%A7%88%EB%AC%BC%20%EB%B0%A9%EC%96%B4%EC%A0%84).
  - Counters to it:
    - A boss skill with no attack power ignores Absolute Defense.
    - One boss "ignores all protection, including absolute and spell defense, and instantly kills if hit" — [en.namu Raid/Demon Defense Battle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EB%A7%88%EB%AC%BC%20%EB%B0%A9%EC%96%B4%EC%A0%84).
    - In the Eternal Memory raid, the hit count is so high that Absolute Defense or spell defense "almost never works" — [en.namu Raid/Eternal Memory](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EC%98%81%EC%9B%90%EC%9D%98%20%EA%B8%B0%EC%96%B5).
    - The support hero Mara "breaks Absolute Defense with 4 basic attacks" — [NamuWiki 덱](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1).
    - One relic gives heroes Absolute Defense and **strips** Absolute Defense, spell defense and current skill-cancel or stacking effects from all enemies in range — [en.namu Relic](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%9C%A0%EB%AC%BC).
- **Shields and protection:** Luniare's Protection (above), and the Courage-class 5×5 shield at battle start — [en.namu Battlefield/Strategy](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EA%B2%A9%EC%A0%84%EC%9D%98%20%EC%A0%84%EC%9E%A5/%EC%A0%84%EB%9E%B5).
- **Damage reduction and reflection:** Row-1 damage reflection from the Giant Altar — [Mejoress](https://www.mejoress.com/en/king-god-castle-best-altars-to-choose-for-your-team/). One relic or deck grants up to −40% damage taken at 10 heroes — [en.namu Deck](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1).
- **CC:**
  - Leonhardt's stun (above).
  - Mara's stun "buys time for Kain to power up". She also lays clones that build "Void" (공허) stacks — [NamuWiki 덱](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1).
  - The "Apostle of Demons" verdict stuns the whole field and deals no damage, so Absolute Defense is useless against it — [en.namu Raid/Demon Defense Battle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EB%A7%88%EB%AC%BC%20%EB%B0%A9%EC%96%B4%EC%A0%84).
- **Summons interact with bosses.** Against the Divine boss, summoned units take 30% damage reduction from the boss, and the boss takes 50% of the damage dealt to the summons (paraphrased; the snippet's wording is garbled) — [kgc.fandom Divine boss strategy](https://kgc.fandom.com/wiki/Divine_boss_strategy).
- **Some stats are conditional.** "Mystic"-class heroes get large ATK and SP boosts that shrink as allies die — [en.namu Battlefield/Strategy](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EA%B2%A9%EC%A0%84%EC%9D%98%20%EC%A0%84%EC%9E%A5/%EC%A0%84%EB%9E%B5).
- **Player agency in combat:** review summaries say battles resolve automatically, so pre-fight setup decides the outcome — [App Store US](https://apps.apple.com/us/app/king-god-castle/id1526791430), [QooApp](https://m-apps.qoo-app.com/en-US/app/15621) (search-summary characterisation).

### Inferences
- **Absolute Defense is the signature defensive rule.** A number of hits are fully negated regardless of size. This makes **hit frequency** a real attribute. Few-big-hit carries (Headshot-style) are walled by charges. Multi-hit, DoT, zero-damage CC and "pierce" effects (Mara, the stripping relic) become counter-picks. The design generates rock-paper-scissors without elemental types.
- Mana from both dealing and taking hits lets tanks reach their skills by absorbing damage. Cheap-cost heroes like Jupiter become "skill-every-swing" engines, and the Yeon change shows the developers had to cap degenerate recast loops.
- Front-to-back default targeting, plus a few "farthest enemy" or random-target exceptions, makes the back line both safe and attackable. That gives formations meaning without full pathfinding complexity.

### Gaps
- **Critical hits:** I found no information.
- **Armour/resist formula, physical versus magic mitigation:** I found only the "spell defense" layer.
- **Movement rules:** whether melee heroes walk across tiles or stay put; any pathfinding.
- **Healing:** heals were not described in the snippets I reached, apart from shields and Protection.
- **Player-cast skills:** I found **no evidence** of a player-controlled "king" or castle active skill. Combat appears fully automatic. Verify in game before assuming either way.

---

## 5. Altar, relics, talents/skill points, awakening, runes, equipment and castle upgrades

### Takeaway
- **Altars** are the in-run build-direction system: 6 types, each levelled up to 15, with breakpoints at levels 5 and 10. You allocate points among them.
- **Relics** are persistent equippable modifiers with rolled options. Some are "corruption" relics that boost a specific altar.
- **Runes** belong to the Great Rift mode.
- **Equipment** has God, King and lower grades.
- **Awakening** exists and changes hero power and kits.
- **Devil's suggestions** are in-run risk/reward offers paid for with castle durability or tougher enemies.
- I found no "talent tree" or "skill points" system under those names.

### Cited Findings
- **Altars:**
  - The 6 altars are Hero, Blacksmith, Blood, Giant, Mage and Greed. Each can be upgraded to level 15 maximum, a cap Altar Relics cannot exceed. Bonuses unlock at levels 5 and 10 — [kgc.fandom Altar](https://kgc.fandom.com/wiki/Altar).
  - Effects mentioned:
    - **Giant** gives Row 1 damage reflection.
    - **Greed** starts combat "at maximum points with an extra +15 silver".
    - **Blacksmith** is typically strongest for solo or Mask-relic builds — [Mejoress](https://www.mejoress.com/en/king-god-castle-best-altars-to-choose-for-your-team/).
    - The altar's second skill pays silver for elite rounds, +1 per altar level up to 15 — [en.namu King God Castle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC).
    - Absolute Defense at battle start: 2, or 3 at Lv15. **Blood** at Lv10+ gives 2/3/4/5 — [en.namu Raid/Demon Defense Battle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EB%A7%88%EB%AC%BC%20%EB%B0%A9%EC%96%B4%EC%A0%84).
  - Typical allocations [UNDATED]:
    - Aramis build: 15 Hero + 8 Greed + 1 Blood + 1 Giant — [kgc.fandom Builds](https://kgc.fandom.com/wiki/Builds).
    - Divine boss: "15 hero and 10 greed (more Luniare)" or "15 hero and 10 smith (more luck, +1 count)" — [kgc.fandom Divine boss strategy](https://kgc.fandom.com/wiki/Divine_boss_strategy).
    - Beginner advice: put points into Blood before level 5, then Hero and Greed — [LevelsXP](https://levelsxp.com/king-god-castle/beginners-guide/).
  - An achievement, "Zealot of Heroes", requires clearing with only the Altar of Heroes — [kgc.fandom Great Rift Achievements](https://kgc.fandom.com/wiki/Great_Rift_Achievements).
- **Relics:**
  - The Hero-altar "corruption" relic "Light of Glory" adds +2/+3/+4/+5 to the Altar of Heroes by relic level — [kgc.fandom Relic](https://kgc.fandom.com/wiki/Relic). NamuWiki's version: the "Encroaching Artifact" strengthens the Altar of Heroes by 2/3/4/5 levels, with a bonus level-up chance when using a "Tome of Power" — [en.namu Relic](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%9C%A0%EB%AC%BC).
  - Named relics: Rapid Sword, Penetrating Spear, Mask, the "Encroachment"/solo relic, Shard of the Blessed Relic, and the Absolute-Defense-stripping relic (see §3–4).
- **Relic options and refining:** A relic-option "reorganisation" moved toward **two-line options**. The PD said the goal was to reduce the frustration of treating anything short of a one-line option as a failure. He admitted the change was drastic and the UI direction wrong, offered refining-based compensation, and promised further upgrades for single-line options. The letter came 52 hours after the update announcement (date given as 25 Mar; year not in snippet) — [en.namu Artifact Option Reorganization Controversy](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC%20%EC%9C%A0%EB%AC%BC%20%EC%98%B5%EC%85%98%20%EA%B0%9C%ED%8E%B8%20%EB%85%BC%EB%9E%80).
- **Runes (Great Rift):** The front-line rune gives Absolute Defense to the hero and to allies within 2 horizontal tiles — [NamuWiki 대균열/룬](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8C%80%EA%B7%A0%EC%97%B4/%EB%A3%AC). Several runes require an Altar Relic level of 15 or higher — [kgc.fandom Runes](https://kgc.fandom.com/wiki/Runes).
- **Equipment:** Items have grades. A hero with one God-grade (counts 3) and one King-grade (counts 2) item has a "total item grade" of 5 — [en.namu Tips](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%ED%8C%81). In-run "smelting" (blacksmith) and merchant purchases strengthen the camp — [en.namu King God Castle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC).
- **Devil's suggestions:** In each stage, a devil offers an item for a penalty: more monsters, higher-level monsters, or reduced castle durability — [en.namu Raid/Demon Defense Battle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EB%A7%88%EB%AC%BC%20%EB%B0%A9%EC%96%B4%EC%A0%84).
- **Awakening:** It is required for some heroes to be viable (Mara in the Kain deck) — [NamuWiki 덱](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1).
- **"Legacies":** A 2026 Google Play reviewer calls them "nearly impossible to grind for" — [Google Play US](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_US).

### Inferences
- The altar is a **run-level commitment axis**, separate from the hero roster. Hero means stats, Greed means economy, Blood means survivability and Absolute Defense, Giant means front-row reflection, Mage presumably means spell scaling, and Blacksmith means items. Hard caps at 15 with breakpoints at 5 and 10 push players to "max one, splash another", which keeps choices legible.
- The equipment tier names (God and King grades) are probably where the title's "King God" wordplay lives. That is cosmetic, not a mechanic.
- Relic option rolling (one-line versus two-line) is a long-tail grind system that **feeds combat power**. Its controversy shows how persistent RNG gear can make players feel any run without perfect relics is pointless.

### Gaps
- The Mage altar's effects, and full effect tables for each altar's level 5 and level 10 bonuses.
- The awakening procedure and what changes on awakening (stats, skill rework or new passive).
- Whether a "talent" or skill-point tree exists at all. None was found.
- What "Legacies" are mechanically.
- The exact role of the "Tome of Power".

---

## 6. Hero systems: acquisition, rarity, classes/roles, progression, notable kits, synergies, build diversity, balance

### Takeaway
Heroes come from random summons, with currencies such as "God's Scrolls". The roster was **69 heroes in January 2026**. Progression runs on a persistent hero level (cap raised from 20 to 30 in Sep 2025; levels past 25 gated by hero medals and a fortnightly "Cube of Power"), awakening, relics and equipment. Classes are **not** Warrior/Archer/Wizard/Priest. Guides use either functional roles (Tank, Fighter, Ranged, Assassin, Supporter) or the game's own affinity-style labels (Courage, Mystic/Mystique, Shadow, Tenacity, Swiftness), and the latter carry group effects. Players report power creep from new heroes and a meta of narrow "one-carry" decks.

### Cited Findings
- **Acquisition:**
  - Summoning is random, and luck decides which heroes you get — [Metacritic user reviews](https://www.metacritic.com/game/king-god-castle/).
  - Codes give "God's Scrolls", for example `2025HalfYearAnniversary` for 4 God's Scrolls — [Pro Game Guides codes](https://progameguides.com/king-god-castle/king-god-castle-codes/).
  - A 2026 reviewer says "only 7 out of the 25 different units are accessible" and unlocking a new one is "extremely unlikely". This conflicts with the 69-hero roster and may describe a new-account or mode-limited pool — [Google Play IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_IN).
  - A TapTap reviewer says the game is "not for f2p" — [TapTap reviews](https://www.taptap.io/app/201530/review).
- **Roster size:** 69 heroes as of 10 January (2026) — [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
- **Classes and roles:**
  - Guides disagree. Some use RPG roles (Assassin, Supporter, Tank, Ranged, Fighter) — [MrGuider tier list (Oct 2026)](https://www.mrguider.org/articles/king-god-castle-tier-list-guide/).
  - Others use the game's own labels: Evan and Ian under **Courage**, Mirsyl under **Mystique**, plus **Shadow**, **Tenacity** and **Swiftness** — [VCGamers](https://www.vcgamers.com/news/en/strongest-characters-in-king-god-castle-tier-names-and-classes/), [MobileMatters (Aug 2026)](https://mobilematters.gg/guides/gaming/king-god-castle-unit-tier-list).
  - NamuWiki's character page shows class headers "Mystery, Shadow, Tenacity" — [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
  - Mirsyl is labelled "supporter" in one guide and "Mystique" in another, which suggests the two systems overlap: a role plus a class.
- **Class effects:** Courage heroes grouped together give a 5×5 shield at battle start. Mystic heroes get large ATK and SP boosts that shrink as allies die — [en.namu Battlefield/Strategy](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EA%B2%A9%EC%A0%84%EC%9D%98%20%EC%A0%84%EC%9E%A5/%EC%A0%84%EB%9E%B5). This page is about a specific mode (격전의 전장, the "Fierce Battlefield"), so these may be mode modifiers rather than global synergies.
- **Progression:**
  - In-run: star grades 1–7 (§3).
  - Persistent hero level: cap raised from 20 to 30 on 10 Sep 2025 — [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
  - Levels past 25 need a "cube" sold only every two weeks — [Google Play IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_IN). The developer responded on 21 Aug 2026 about hero medals past Lv25 and the Cube of Power — [Google Play US](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_US).
  - Bombie's passives unlock at hero levels 4 and 8, so hero level unlocks kit features as well as stats — [kgc.fandom Bombie](https://kgc.fandom.com/wiki/Bombie).
  - Awakening (§5) and equipment grades (§5) also apply.
- **Notable kits (mechanics only) [UNDATED numbers]:**
  - **Leonhardt (tank):** shield-bash stun with growing reach — [eXputer](https://exputer.com/guides/tier-lists/king-god-castle-tier-list/).
  - **Aramis (ranged carry):** single-target "Headshot" scaling off ATK; the core of mass-copy builds with Rapid Sword — [kgc.fandom Heroes](https://kgc.fandom.com/wiki/Heroes), [kgc.fandom Builds](https://kgc.fandom.com/wiki/Builds).
  - **Bombie:** random-target bombardment with a big attack-speed steroid and 3×3 splash passives — [kgc.fandom Bombie](https://kgc.fandom.com/wiki/Bombie).
  - **Luniare (support):** links to one ally, channels for 5 s, then gives Protection and transfers part of her ATK and SP into that ally. A "make one carry stronger" support — [kgc.fandom Heroes](https://kgc.fandom.com/wiki/Heroes).
  - **Lyca (assassin-type):** always targets the farthest enemy — [NamuWiki 캐릭터 정보](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
  - **Jupiter:** 15-mana skill, so it casts on every basic attack — [same](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
  - **Kain + Mara (Seasons 28–30):** Mara stuns, spawns clones that build Kain's "Void" stacks, and breaks Absolute Defense every 4 hits. Kain needs time to power up — [NamuWiki 덱](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1).
  - **An unnamed form-changer:** bruiser in the front row, ranged carry in the back row — [NamuWiki 캐릭터 정보](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
- **Tier lists and meta (opinion, shifting):**
  - An older ranking puts Bombie, Luniare and Shelda in S tier for PvE, with Aramis A — [Twinfinite](https://twinfinite.net/guides/king-god-castle-tier-list/).
  - A more recent guide puts Aramis S and Luniare B — [MrGuider (Oct 2026)](https://www.mrguider.org/articles/king-god-castle-tier-list-guide/).
  - Tier lists rate PvE and PvP separately — [LevelsXP tier list](https://levelsxp.com/king-god-castle/tier-list/).
- **Power creep and balance complaints:**
  - "New characters are overpowered" — [Google Play NZ ("Defense RPG")](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_NZ).
  - Later updates added more pay-to-win elements — [Metacritic](https://www.metacritic.com/game/king-god-castle/).

### Inferences
- **Hero identity comes from rule-breaking hooks** rather than raw stats: farthest-target, cast every swing, form changes by row, ally stat transfer, Absolute Defense breaking. A small roster of about 70 stays distinct because each hero changes a combat rule.
- **Synergy is carry-centric.** Supports like Luniare and Mara amplify a single carry. Combined with solo relics and the old one-man late-team deck, the meta gravitates toward "1 carry + enablers" or "N copies of one carry". That gives strong build identity but limited diversity per season.
- Locking persistent levels (25–30) behind scarce items puts out-of-run power into combat balance. In a design with in-run merging, this risks drowning tactical decisions under account-power differences.

### Gaps
- The official **rarity tier names and count**. I found no reliable source. Item grades include God and King, but hero rarity was not confirmed.
- The full list of class or affinity labels and their **global** synergy bonuses, as opposed to mode-specific ones.
- Shard or duplicate mechanics for persistent upgrades, and the details of "hero medals".
- Representative PvP-meta heroes for late 2026.

---

## 7. Enemy design and boss behaviour

### Takeaway
Enemies scale through chapter difficulty and through player-accepted devil penalties (more or higher-level monsters). The bosses I found are built as **counters to specific defensive layers**: no-damage CC that ignores Absolute Defense, multi-hit barrages that drain it, an "ignore all protection, one-shot" attack, and damage-reduction rules against summons. Late chapters are reported as spiky, with enemy types that two-shot fully merged (tier-4) heroes.

### Cited Findings
- **Raid boss mechanics:**
  - **Demon Defense (마물 방어전):** One boss uses a skill with no attack power, so it ignores Absolute Defense. Another boss's attack ignores all protection, including absolute and spell defense, and kills instantly on hit. The "Apostle of Demons" verdict stuns the entire field with no damage — [en.namu Raid/Demon Defense Battle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EB%A7%88%EB%AC%BC%20%EB%B0%A9%EC%96%B4%EC%A0%84).
  - **Eternal Memory (영원의 기억):** the hit count is too high for Absolute Defense or spell defense to work — [en.namu Raid/Eternal Memory](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EC%98%81%EC%9B%90%EC%9D%98%20%EA%B8%B0%EC%96%B5).
  - **Encroachment (잠식) sub-raid page:** exists, but I saw no detail — [en.namu Raid/Monster Defense/Encroachment](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EB%A7%88%EB%AC%BC%20%EB%B0%A9%EC%96%B4%EC%A0%84/%EC%9E%A0%EC%8B%9D).
  - **Hero Raid:** King God Castle heroes are randomly selected and appear as enemies across stage 7 — [en.namu Arena](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%95%84%EB%A0%88%EB%82%98) / [en.namu King God Castle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC).
- **Divine boss:** Summons are penalised (the 30% / 50% damage rules, §4). The standard setup is 15 Hero altar plus 10 Greed or 10 Smith — [kgc.fandom Divine boss strategy](https://kgc.fandom.com/wiki/Divine_boss_strategy).
- **Great Rift (대균열):** a floor-based mode with randomly regenerated 11-tile floors, its own boss pages and runes — [kgc.fandom Great Rift](https://kgc.fandom.com/wiki/Great_Rift), [en.namu Crack/Monster/Boss](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EA%B7%A0%EC%97%B4/%EB%AA%AC%EC%8A%A4%ED%84%B0/%EB%B3%B4%EC%8A%A4), [en.namu Great Rift](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EA%B7%A0%EC%97%B4/%EB%8C%80%EA%B7%A0%EC%97%B4).
- **Monster targeting varies by type:** 8-tile forward detection; vampire monsters skip the back line (§2).
- **Scaling:** Devil offers raise monster count or level (§5). High chapters have strong mobs from round 1 — [Arca.live](https://arca.live/b/kinggod/69747856?p=1).
- **Late-chapter spikes:** a 2026 reviewer says late chapters are unbalanced, "with one enemy type with wraiths 2 shoting tier 4 units" — [Google Play IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_IN).

### Inferences
- Bosses work as **"exams" for specific defensive layers**. Each invalidates a common answer (Absolute Defense stacking, summon walls, single-target protection) and forces a different build. This is good for depth when it is telegraphed. It feels unfair when the counter is a hard one-shot that ignores all mitigation.
- Hero Raid, which turns player heroes into enemies, reuses the hero kit library as enemy design. That is cheap content, and it teaches players matchups.

### Gaps
- Boss attack patterns, phases, telegraphs and timers for the main Raid chapters.
- Whether enemies have enrage timers.
- Per-chapter stat-scaling formulas.

---

## 8. Combat pacing: battle length, speed-up, auto-play

### Takeaway
I could verify very little. Runs are multi-round, with rounds 1–5+ and elite rounds, and the number of runs per day is limited by an energy system. I could not confirm battle duration, speed-up multipliers or an auto-repeat option.

### Cited Findings
- A limited energy system restricts how many missions or runs you can do — [QooApp](https://m-apps.qoo-app.com/en-US/app/15621), [Metacritic](https://www.metacritic.com/game/king-god-castle/). "The energy system limits the game severely" — [Google Play IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_IN).
- The game "has become a daily chore and not a game" — [Google Play NZ](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_NZ).
- Round-by-round progression, with camp expansion keyed to rounds 1–5 — [en.namu Deck](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1).
- Some skills have timing windows of a few seconds: a 2 s focus on the blessed tile, a 5 s channel for Luniare, and 1.5–3 s stuns — sources in §2, §4. These suggest individual fights last on the order of tens of seconds.

### Inferences
- With battle-start effects and short channels mattering (2–5 s), fights are probably short and burst-heavy. Opening-moment buffs (Absolute Defense charges, shields at battle start) carry a lot of value.

### Gaps
- Typical battle and run length, speed-up (×2/×3) options, skip tickets, and auto-repeat. None was found in the snippets I reached.

---

## 9. Player-reported strengths and weaknesses of combat and hero systems

### Takeaway
Players praise the strategic depth of merging and positioning, the character collection, and, in some listings, the absence of forced ads. Recurring complaints are RNG overload (summons, draws, relic options), repetition, energy and grind gates on persistent power, power creep from new heroes, late-chapter difficulty spikes, content droughts, and a dominant entry-barrier strategy (the late team, now removed).

### Cited Findings
- **Strengths:**
  - An App Store reviewer calls it better than typical auto-battlers — [App Store US](https://apps.apple.com/us/app/king-god-castle/id1526791430).
  - Players praise the strategy and character collection. One says it's "the first merge game i've played without forced ads" — [Google Play US/IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_US).
  - A TapTap reviewer: "gets a bit repetitive, but atleast there are no intrusive ads" — [TapTap reviews](https://www.taptap.io/app/201530/review).
  - QooApp describes a "tower defense and auto chess blend" — [QooApp](https://m-apps.qoo-app.com/en-US/app/15621).
- **Repetition:**
  - "base units are fine but the repetition becomes boring very quickly" — [Google Play IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_IN).
  - The game gets repetitive over time — [QooApp](https://m-apps.qoo-app.com/en-US/app/15621).
- **RNG and luck:**
  - "the draw system [is] poor" — [Google Play IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_IN).
  - NamuWiki's criticism page says the game has too many luck factors and a chronic shortage of goods in the midgame — [en.namu Criticism and Controversy](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%B9%84%ED%8C%90%20%EB%B0%8F%20%EB%85%BC%EB%9E%80).
- **Balance and power creep:**
  - "new characters are overpowered and the gameplay is getting cut" — [Google Play NZ](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_NZ).
  - Late chapters are unbalanced, with wraiths two-shotting tier-4 units — [Google Play IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_IN).
  - Later updates added P2W — [Metacritic](https://www.metacritic.com/game/king-god-castle/).
- **Grind gates on combat power:** Legacies are near-impossible to grind; levels past 25 need a fortnightly cube — [Google Play IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_IN). The developer replied on 21 Aug 2026 promising a review — [Google Play US](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_US).
- **Dominant strategy and entry barrier [HISTORICAL]:** The late team became the most important strategy and an entry barrier — [en.namu Tips](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%ED%8C%81). It was removed in Dec 2025 — [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
- **Content droughts [HISTORICAL]:** No new Raid chapters from 2022 until Feb 2024 — [NamuWiki 비판 및 논란](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%B9%84%ED%8C%90%20%EB%B0%8F%20%EB%85%BC%EB%9E%80).
- **Relic-option controversy:** Players reacted to a drastic option rework, and the PD apologised and offered compensation — [en.namu Artifact Option Reorganization Controversy](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC%20%EC%9C%A0%EB%AC%BC%20%EC%98%B5%EC%85%98%20%EA%B0%9C%ED%8E%B8%20%EB%85%BC%EB%9E%80).
- **Ads and stability:** Some "Defense RPG"-era reviewers call ads intrusive. A Luminous Fate reviewer reports constant crashes after an update — [Google Play NZ](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_NZ), [Google Play IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_IN).
- **Aggregate score:** Metacritic user score 6.8 from only 4 ratings, split positive, mixed and negative — [Metacritic](https://www.metacritic.com/game/king-god-castle/).

### Inferences
- The complaints cluster in **meta-progression and RNG layers** (summons, relic options, level gates, energy) more than in the moment-to-moment combat rules, which players broadly describe as strategic. For an original design, the combat kernel is the part worth learning from. The persistent-power layers are the part to avoid copying.

### Gaps
- I could not reach Reddit (r/KingGodCastle), Steam reviews (no Steam version found), or Discord. No Reddit threads came up in search, so the community quotes are mostly Google Play, TapTap, Metacritic and Korean wikis.
- I found no professional reviews (Pocket Gamer, TouchArcade). The search budget ran out before I could check.

---

## 10. Why the combat is engaging, and where it could be improved (design analysis for an original game)

### Takeaway
King God Castle's combat holds attention because it layers **four small, legible decision systems** on top of a fully automatic fight:
1. a random-summon / merge-to-7★ economy with width-versus-depth tension;
2. tile placement with row, horizontal and area rules;
3. a run-level altar commitment;
4. a count-based defensive rule (Absolute Defense) that bosses deliberately attack.

Its weaknesses come from stacking too much RNG and too much persistent power on that kernel, and from systems that harden into mandatory strategies.

### Cited Findings
These are the grounds for the analysis; details and URLs are in §2–§9.
- Silver is spent on both summoning and formation expansion. Camp grows from 4 to 8–10 by round 5 — [en.namu King God Castle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC), [en.namu Deck](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1).
- Merging to 7★ in four tiers — [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
- Relics paying out at 1 hero or at ≥5 copies — [NamuWiki 유물 r258](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%9C%A0%EB%AC%BC?uuid=aa8b80e2-577c-45d8-a1c1-4563d5639c55), [LevelsXP](https://levelsxp.com/king-god-castle/beginners-guide/).
- Six altars capped at 15, with breakpoints at 5 and 10 — [kgc.fandom Altar](https://kgc.fandom.com/wiki/Altar).
- Absolute Defense charges, and bosses and heroes built to bypass them — [en.namu Raid/Demon Defense Battle](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%8A%B5%EA%B2%A9/%EB%A7%88%EB%AC%BC%20%EB%B0%A9%EC%96%B4%EC%A0%84), [NamuWiki 덱](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8D%B1).
- Row, horizontal and area positioning rules — [NamuWiki 대균열/룬](https://namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%8C%80%EA%B7%A0%EC%97%B4/%EB%A3%AC), [Mejoress](https://www.mejoress.com/en/king-god-castle-best-altars-to-choose-for-your-team/).
- The late team as a degenerate dominant strategy, removed in Dec 2025 — [en.namu Tips](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%ED%8C%81), [en.namu Character Information](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EC%BA%90%EB%A6%AD%ED%84%B0%20%EC%A0%95%EB%B3%B4).
- RNG and grind complaints — [en.namu Criticism](https://en.namu.wiki/w/%ED%82%B9%EA%B0%93%EC%BA%90%EC%8A%AC/%EB%B9%84%ED%8C%90%20%EB%B0%8F%20%EB%85%BC%EB%9E%80), [Google Play IN](https://play.google.com/store/apps/details?id=com.awesomepiece.castle&hl=en_IN).

### Inferences
Every point in this section is my own design inference from the findings above.

**Why it is engaging:**
1. **Width versus depth on one currency.** Every silver spent is a choice between another body (a formation slot plus a summon) and more stars on a carry. This is the auto-chess core, compressed for mobile with a small fixed deck (6 types), so outcomes feel authored rather than random.
2. **Run identity through binary relic and altar commitments.** "Solo carry" versus "army of one hero" versus "balanced" are clearly different plays. Hard altar caps (15) and breakpoints (5 and 10) make allocation readable.
3. **Count-based mitigation creates matchups without an element chart.** Absolute Defense charges make *number of hits* a stat. Multi-hit, zero-damage CC and "pierce or strip" effects become natural counters. It is a cheap, readable rock-paper-scissors.
4. **Rule-breaking hero hooks.** Heroes are memorable because each one changes a combat rule (farthest target, cast every swing, form by row, stat transfer, Absolute Defense break). That keeps a roster of about 70 distinct.
5. **Spatial rules a player can learn at a glance.** Row 1 buffs, ±2 horizontal adjacency, 3×3 and 5×5 areas, a blessed tile. Positioning matters without the cost of full tactics-RPG movement.
6. **Push-your-luck offers.** Devil's suggestions trade castle durability or harder waves for power, which gives the passive auto-fight an active strategic layer between rounds.
7. **Bosses as exams.** Each boss invalidates a stock answer, so the build has to adapt.

**Where it could be improved (lessons for an original design):**
1. **Too many stacked RNG layers** (gacha, in-run summons, relic option rolls) make losses feel unearned. Keep in-run randomness and **make out-of-run power deterministic**, or keep it small.
2. **Safety valves become exploits.** The late-team mechanic shows that any rule letting players control early RNG becomes mandatory knowledge. Prefer transparent tools such as a lock, a reroll or a guaranteed starter (KGC's own Dec 2025 fix) over hidden summon rules.
3. **Carry-centric synergy narrows diversity.** Add synergies that reward *mixed* teams (adjacency combos between different classes, role-pair bonuses) so the middle ground can compete with "1 carry + enablers".
4. **Hard counters need telegraphs.** "Ignore all protection, instant kill" and field-wide no-damage stuns should be readable and answerable: positioning to dodge, a cleanse, a pre-fight scouting screen. Otherwise they read as cheap.
5. **Little agency during the fight.** I found no evidence of a player-cast skill. A light, cooldown-gated "commander" action (one or two per fight) could add mid-battle decisions without breaking the auto-battle identity. This is an inferred opportunity, not something KGC is confirmed to lack beyond doubt.
6. **Persistent level gates distort tactical balance.** Gating levels 25–30 behind scarce items means account power can override placement and build skill. Cap or normalise persistent stats in challenge modes.
7. **Hidden mechanics drive players to wikis.** Absolute Defense counts, aggro ranges, target rules and summon rules are documented mostly by fans. Surface target lines, charge counts and range overlays in the UI.

### Gaps
- I could not observe actual fights (video or hands-on), so pacing and readability judgements are inferred.
- I could not confirm whether a player-cast ability exists in the current version (Season 75, Nov 2026).
