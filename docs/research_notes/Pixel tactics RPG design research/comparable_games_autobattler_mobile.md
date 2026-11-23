# Comparable Games: Autobattlers, Hero-Collection and Mobile Strategy (comparison points for an original KGC-like 2D pixel tactical autobattler RPG)

Research date: 2026-11-23. Scope: TFT, Auto Chess (Dota Auto Chess + Drodo/Dragonest mobile), Despot's Game, Guardian Tales, Dungeon Maker: Dark Lord, Arknights, Super Auto Pets, Backpack Battles, plus one optional game (The Bazaar, picked for async-ghost PvP and its monetization lessons).

**Evidence tags used in the profiles.** [V] = verified fact with a URL. [C] = community or anecdotal claim with a URL (Reddit/Steam/user reviews/aggregators). [I] = my own design inference. [U] = unverified background knowledge (not confirmed this session; check before relying on it).

**Method caveat (important for the report writer).** In this session the fetch tool could not reach teamfighttactics.leagueoflegends.com, invenglobal.com, naavik.co or en.wikipedia.org (host not allowed by the session network). The web-search budget then ran out partway through. Most [V]/[C] items below therefore rest on search-engine summaries of the linked pages, not on full reads. Each link is the page the summary attributed the claim to. Where that attribution was unclear, the bullet says so. Matrix fields that could not be sourced (mostly art, animation and UI specifics) are marked [U] or [I]. Treat those as hypotheses.

---

## 1. Teamfight Tactics (Riot Games): PC + mobile, F2P, live

### Takeaway
TFT is the best-documented reference for packing meaningful decisions into the pre-combat phase: interest economy, roll-vs-level, item components, traits and Augments. Riot publicly discusses its variance philosophy. Its 3D production, three sets per year and synchronous 8-player infrastructure are far beyond a small team's reach. Borrow its systems (interest, component items, curated run-modifiers, variance management), not its scope.

### Cited Findings
**Current status (Nov 2026)**
- [V] Set 17 "Space Gods" launched on PC and mobile on 15 Apr 2026 after the PBE on 31 Mar. Its "Realm of the Gods" mechanic replaces the traditional carousel. — [ComicBook](https://comicbook.com/gaming/news/teamfight-tactics-space-gods-set); [Inven Global](https://www.invenglobal.com/teamfighttactics/articles/20370/teamfight-tactics-reveals-set-17-space-gods)
- [V] Set 18 "Enchanted Wilds" is forest-themed and built around Wisps. Riot support lists Part I as 26 Aug 2026 to 5 Oct 2026 ("subject to change"). — [Riot Support](https://support.riotgames.com/en-us/tft/events/teamfight-tactics-enchanted-wilds-i); [Liquipedia TFT18.1](https://liquipedia.net/tft/Patch_TFT18.1)
- [V] The 2026 roadmap (published Dec 2025) has three sets. Set 19 is music-themed for "Winter 2026". Riot pages conflict on the TFT19.1 date (18 Nov vs 1 Dec 2026), so whether Set 19 is live as of 23 Nov 2026 is unconfirmed. — [Sheep Esports, 14 Dec 2025](https://www.sheepesports.com/us/articles/tft-2026-roadmap-shows-everything-players-can-expect-up-to-set-19/en); [Riot patch schedule](https://support.riotgames.com/en-us/tft/events/patch-schedule-teamfight-tactics); [Esports Insider, Dec 2025](https://esportsinsider.com/2025/12/teamfight-tactics-unveils-2026-roadmap)
- [V, headline only] The roadmap includes "three new sets and a tech update". An Inven interview is headlined "'TFT' Developers: 'Unreal Engine Is Just the Beginning'". I did not verify the engine details. — [esports.net (DE)](https://www.esports.net/de/news/tft-roadmap-2026/); [Inven Global](https://www.invenglobal.com/articles/23690/tft-developers-unreal-engine-is-just-the-beginning). Win.gg headline: "Why TFT mid-set updates are going away". — [Win.gg](https://win.gg/news/why-tft-mid-set-updates-are-going-away/)
- [V, headline only] The TFT lead told Mein-MMO that "in 2020, TFT was close to death, but today it runs better than ever". — [Mein-MMO](https://mein-mmo.de/en/the-boss-reveals-to-us-in-2020-tft-was-close-to-death-but-today-it-runs-better-than-ever-before,1059164/)

**Design pillars and Augments (Riot /dev posts)**
- [V] Riot's "design pillars" post frames TFT around mastery, playful competition and discovery. It does not address Augments specifically. — [Riot /dev: Design Pillars of TFT](https://teamfighttactics.leagueoflegends.com/en-gb/news/dev/dev-design-pillars-of-tft)
- [V] Augments are an "evergreen system", but "some have overstayed their welcome". Riot planned to refresh "the vast majority" each set. — [Riot /dev: Monsters Attack! learnings](https://teamfighttactics.leagueoflegends.com/en-au/news/dev/dev-teamfight-tactics-monsters-attack-learnings/)
- [V] The Game Analysis Team stress-tests Augments by simulating optimized combos. It aims for diversity of skill requirements, balancing high-skill Augments with easier ones. — [Riot: Talking Tactics, GAT](https://teamfighttactics.leagueoflegends.com/en-au/news/dev/talking-tactics-game-analysis-team-gat/)
- [V; post attribution from search summary] After the complex Shadow and Radiant items, Riot concluded set mechanics should create excitement "without giant layers of complexity", and said Hextech Augments fit that goal. Riot also said it would watch, and if needed disable, Augments that grant early access to deep trait breakpoints. — [Riot /dev: Gizmos & Gadgets learnings](https://teamfighttactics.leagueoflegends.com/en-au/news/dev/dev-teamfight-tactics-gizmos-gadgets-learnings/)
- [V] Champion Augments work best when they change how a champion is played and are narrow enough to need a specific setup. "High Stakes" Augments were a mixed success. — [Riot /dev: Magic n' Mayhem learnings](https://teamfighttactics.leagueoflegends.com/en-au/news/dev/dev-tft-magic-n-mayhem-learnings/)
- [V] Team-Up Augments were a highlight. 6-cost Augment power being "purely economic" was judged a miss. — [Riot /dev: Into the Arcane learnings](https://teamfighttactics.leagueoflegends.com/en-gb/news/dev/dev-tft-into-the-arcane-learnings)

**Economy, rolling and positioning (community guides; numbers vary by set)**
- [V] Interest is +1 gold per 10 gold held, capped at +5 at 50 gold. Win and loss streaks add bonus gold. — [Upcomer](https://upcomer.com/teamfight-tactics-how-to-manage-your-economy-in-tft/); [Mobalytics](https://mobalytics.gg/blog/tft/how-to-manage-your-economy-in-teamfight-tactics-three-strategies/)
- [V] The roll-vs-level trade-off: rolling pays off when several shop hits would improve the board. Levelling is a tempo play that protects HP or a streak. "Slow roll" means rolling only the gold above 50 to hit 3-star units. — [PocketGamer](https://www.pocketgamer.com/teamfight-tactics/how-to-econ-in-tft-the-best-ways-to-manage-your-economy-in-teamfight-tactics/); [Bamboo Gaming](https://www.bamboogaming.net/tft/economy); [Mobalytics levelling](https://mobalytics.gg/blog/tft/leveling-guide/)
- [C] Basic positioning: put carries in a corner or the second row, and play around threats such as Zephyr, hooks, Shroud of Stillness and assassins that jump the backline. — [Mobalytics guide](https://mobalytics.gg/blog/tft-guide-how-to-climb-to-gold/)

**Variance**
- [V] For Set 11, design lead Mortdog ran a 1,000-roll test after Reddit complaints. Uncontested champions showed up about 45% of the time, so the math was correct, but he said: "Just because it is mathematically correct does NOT mean the design is perfect". He said good design does not "let RNG take the wheel" and that there is no easy fix for high variance. — [Dot Esports](https://dotesports.com/?p=1245514)
- [V; exact article not pinned] For Set 5, Riot said it would move away from RNG-focused mechanics toward ones that add "player agency". — Dot Esports, per search summary ([candidate](https://dotesports.com/?p=381497))
- [V, headlines] 2019: "Teamfight Tactics item RNG is bad right now, but Riot promises improvements". Later: "Teamfight Tactics Makes Blaming Bad Luck Harder" (bad-luck protection for items). — [AppTrigger 2019](https://apptrigger.com/2019/07/05/teamfight-tactics-item-rng-broken); [Screen Rant](https://screenrant.com/teamfight-tactics-bad-luck-protection-items-rng/)

**Monetization**
- [V] "Treasure Realms" is a gacha for premium cosmetics. Tokens sell 100 for 390 RP. Riot halved the per-pull cost to 50 tokens but cut the Mythic drop rate from 1% to 0.3%. It added Realm Crystals and Mythic Medallions to give "more agency", acknowledging complaints about getting many Little Legends while chasing a Mythic Chibi. — [Riot /dev: Treasure Realms](https://teamfighttactics.leagueoflegends.com/en-sg/news/dev/tft-treasure-realms-a-new-portal-to-personalization/); [LoL Wiki](https://wiki.leagueoflegends.com/en-us/TFT:Treasure_Realms)
- [C] Players called a Prestige TFT skin's pricing "disgusting": a Legendary-priced skin, a Mythic chroma sold through gacha, and skins at 250 ME each. — [Dexerto](https://dexerto.com/league-of-legends/lol-players-rebel-against-disgusting-prices-with-new-prestige-tft-skin-2311243). Riot also announced a rotating shop. — [Riot](https://www.leagueoflegends.com/en-us/news/game-updates/tft-s-rotating-shop-coming-soon/)

### Inferences
- **Core loop [U]:** 8-player free-for-all. Each round: buy champions from a 5-slot shop with gold (income + interest + streak). Three copies combine into a higher star level. Trait thresholds activate bonuses. PvE rounds drop item components. Losing a fight costs HP and the last player standing wins.
- **Combat [U]:** Hex board. Units auto-path and target, fill mana and cast abilities. Positioning counters threats: backline divers, hooks, AoE.
- **Character progression [U]:** Within a match only (star-ups, items, traits). No persistent unit power; meta progression is cosmetic and ranked.
- **Art and animation [U]:** 3D League champion models with VFX-heavy abilities and chibi "Little Legends" avatars. Not pixel art.
- **Narrative [U]:** Almost none. Each set has a Runeterra-flavored theme (e.g., "Space Gods") carried by art and trait names.
- **UI [U]:** Information-dense; trait tracker, shop and bench on one screen. The mobile and PC clients share content.
- **Difficulty [U]:** Self-calibrating through ranked matchmaking. No authored difficulty curve.
- **Retention [V+I]:** Set rotation every ~4 months, ranked seasons and cosmetics. The [V] roadmap shows three sets per year.
- **Technical complexity for a small team [I]:** Very high. Synchronous 8-player servers, around 60 champions per set with 3D VFX, and rapid set churn. The single-player subset (shop, merge, items, traits, augments) is very achievable in 2D.
- **Transferable principles [I]:**
  1. *Interest economy with banked-gold breakpoints.* Gold carried between nodes earns interest up to a cap. Even in a single-player roguelike this creates a "save vs. spend" tension every node.
  2. *A small set of combinable components.* A few base items combine into many finished items, and choosing which unit holds them is itself a positioning decision.
  3. *Curated run-modifiers ("augments") at fixed beats, 1 of 3.* Mix skill floors and prefer modifiers that change how a unit plays. Avoid purely economic ones and ones that unlock deep synergy breakpoints too early (Riot's own lessons).
- **Pitfalls [I]:** Shop variance feels unfair even when it is mathematically fine, so add bad-luck protection, visible odds, freeze/lock and pity. Complexity creep (the Shadow/Radiant lesson). Cosmetic gacha pricing backlash.

### Gaps
- Could not open Riot /dev pages directly, so quotes come from search summaries.
- Current-set shop odds, XP costs and board dimensions are not verified this session (the [U] items above).
- Set 19 name and launch not confirmed. No mobile-vs-PC player split or revenue data found.

---

## 2. Auto Chess: Dota Auto Chess (mod, 2019) and Drodo/Dragonest standalone Auto Chess (mobile/PC/PS4)

### Takeaway
The genre's origin: a 4-person studio's Dota 2 custom map (Jan 2019) went viral within weeks and was then cloned by Valve, Riot and others within months. The standalone mobile Auto Chess still operates under Dragonest but looks niche now. A Steam snapshot showed a few hundred concurrent players. Lesson: the loop itself is not defensible; differentiation, platform fit and live-ops are.

### Cited Findings
- [V] Dota Auto Chess was released by the four-person Drodo Studio as a Dota 2 custom mod on 4 Jan 2019 and became a hit within a week. Drodo's earlier work was GemTD, a tower-defense mod modelled on Warcraft 3 mods. — [Wikipedia (via search)](https://en.wikipedia.org/wiki/Dota_Auto_Chess); [Red Bull interview](https://redbull.com/int-en/dota-auto-chess-interview-drodo-studio)
- [V] In Feb 2019 Valve flew Drodo to Seattle. On 14 Mar 2019 Drodo announced it would build a standalone mobile Auto Chess itself, published by Dragonest (known for Cytus), without Dota characters. — [Sportskeeda](https://www.sportskeeda.com/esports/dota2-auto-chess-to-auto-chess-mobile-the-journey); [PocketGamer.biz](https://www.pocketgamer.biz/asia/news/70853/drodo-studios-soft-launches-dota-auto-chess-standalone-version-on-mobile/)
- [V] Standalone release dates: Android 18 Apr 2019, iOS 22 May 2019, Epic Games Store 19 Jul 2019, PS4 16 Dec 2020. Valve's own version became Dota Underlords. Many companies rushed out versions. Sources differ on whether Dragonest or Drodo is listed as publisher. — [Wikipedia (via search)](https://en.wikipedia.org/wiki/Dota_Auto_Chess); [TechRaptor](https://techraptor.net/game/auto-chess); [GamesRadar](https://www.gamesradar.com/dota-auto-chess)
- [V, headline] "Dota Auto Chess player number surges past six million mark" (2019). — [Win.gg](https://win.gg/news/dota-auto-chess-player-number-surges-past-six-million-mark/)
- [C, undated third-party snapshot] Steam (app 1530300): about 219 online, 24-hour peak 314, all-time Steam peak 433, roughly -13.7% month over month. Steam only. — [tracker.gg](https://tracker.gg/population/steam/1530300)
- [C, third-party estimate] The Android listing (package com.vng.autochess) shows about 3.1M installs and 103.6K ratings, credited to Dragonest Games. — [AppGoblin](https://appgoblin.info/apps/com.vng.autochess)
- [V] Dragonest still runs "Pocket Dragonest", an official companion app with battle records, analysis tools and community. — [App Store](https://apps.apple.com/us/app/-/id1478260765)
- Further reading, not opened: [Game Developer: Autochess market status and design analysis](https://gamedeveloper.com/design/autochess-market-status-and-design-analysis); [Inven: A rare glimpse behind the creation of Auto Chess](https://www.invenglobal.com/articles/7962/a-rare-glimpse-behind-the-creation-of-auto-chess)

### Inferences
- **Core loop and combat [U]:** 8 players draft from a **shared, finite piece pool**. Three copies star up a piece. Pieces carry two tags (race + class) whose counts trigger synergies. Gold, interest and XP levels raise the unit cap. PvE creep rounds drop items. The board is a chessboard half per player. Combat is fully automatic.
- **Art and animation [U]:** The mod reused Dota 2 3D assets. The standalone uses original stylized 3D pieces.
- **Narrative [U]:** Negligible.
- **Monetization [U]:** Cosmetics and passes (chess-player avatars, boards, effects). Not verified this session.
- **Replayability and retention [I]:** Driven by competitive ranked play. Weakened once TFT, with League's IP and Riot's scale, took the audience.
- **Technical complexity [I]:** High, because of real-time 8-player sync. The single-player subset is moderate.
- **Transferable principles [I]:**
  1. *A shared, contested pool.* When others take copies, your odds drop, which forces pivots. A single-player game can simulate this with AI rivals drafting from the same pool or a "market depletes" rule.
  2. *Two-tag units.* Each unit has, say, an origin and a role, so a roster of ~40 units yields many viable comps. This is cheap combinatorial depth per pixel-art asset.
  3. *Ship fast to own the moment.* The genre leader was decided in months.
- **Pitfalls [I]:** 30-40 minute matches are long for mobile [U]. IP dependence (the mod relied on Dota). A copyable core loop without a distinctive identity.

### Gaps
- No verified data on current mobile DAU/revenue, monetization specifics, or whether the original mod still gets updates in 2026.
- Dota Underlords' end-of-support status not verified ([U]: believed to have stopped receiving updates years ago).

---

## 3. Despot's Game: Dystopian Army Builder (Konfa Games): PC, Xbox, PlayStation, Switch; premium

### Takeaway
The closest analogue to "roguelike map traversal + autobattler squad + pixel art + dark humor". Its signature hooks are **food as a per-unit movement cost**, **class determined by equipped weapon**, and **class mutations that change behavior**. Critics praise the variety but fault RNG-gated mutations, little economic skill expression to offset luck, low interactivity and limited depth.

### Cited Findings
- [V] Announced Feb 2021. Steam Early Access 14 Oct 2021. 1.0 slipped from 15 to 29 Sep 2022 (PC/Xbox). PS5 on 12 May 2023, Switch later. — [Gematsu, Feb 2021](https://www.gematsu.com/2021/02/roguelike-tactics-game-despots-game-announced-for-pc); [Gematsu, Aug 2022](https://www.gematsu.com/2022/08/despots-game-launches-september-15); [Xbox Store](https://www.xbox.com/en-US/games/store/p/9P5ZDVMCJMFD); [Game Developer press release](https://www.gamedeveloper.com/press-release/despots-game-dystopian-army-builder-brings-chaotic-battles-to-pc-consoles-on-september-15)
- [V] Playable solo or in a competitive multiplayer mode; 1.0 added a mode focused on an enhanced multiplayer experience. The creator says the weapons are full of easter eggs referencing "movies, TV shows, games, and books we read growing up". — [Game Developer press release](https://www.gamedeveloper.com/press-release/despots-game-dystopian-army-builder-deploys-puny-humans-on-pc-xbox-today)
- [V; source attribution from search summary] "Simple graphics made with pixel art." — [GamePressure](https://gamepressure.com/games/despots-game/z063d3)
- [V] You lead "puny humans" through a labyrinth and they fight automatically. On death the run restarts and the world is regenerated. — [Epic Games Store](https://store.epicgames.com/p/despots-game-f61a0a)
- [V] **Food:** every human costs 1 food to move between rooms, so a bigger army needs more food. Food can be bought with tokens or obtained by sacrificing a human. **Tokens** buy humans, class items (weapons), mutations and some events. **Class by weapon:** humans become classes by equipping weapons. A class ability activates when you collect people of the same class with different weapons. There were about 10 classes when the guide was written. Room types: food, upgrades, resupply, quests, boss; every floor ends in a boss. — [gameplay.tips guide](https://gameplay.tips/guides/despots-game-dystopian-army-builder-beginners-tips.html); [Sportskeeda review](https://sportskeeda.com/esports/despot-s-game-dystopian-army-builder-review-mincing-puny-humans-food-never-felt-good)
- [V] **Mutations:** class mutations come from altar rooms or events and can change a class's role (e.g., Throwers hurling enemies). Team mutations are bought and mostly boost stats. — [Superjump Magazine review](https://www.superjumpmagazine.com/despots-game-review/)
- [C] Superjump's verdict: "quite fun but lacking engagement". Mutations are locked behind RNG, with "no skill-based economy management that lets you minimise the effects of luck". It is "fun, but just a limited amount of fun". — [Superjump](https://www.superjumpmagazine.com/despots-game-review/)
- [C] PC Gamer (Jon Bolding, pre-EA): "a real good bite-size strategy game", "all about finding weird combos". — [PC Gamer](https://pcgamer.com/an-autobattler-with-refrigerators-wizards-and-mecha-cerberus-comes-this-month)
- [C; individual review not pinned] Reviews say the skill lies mainly in drafting and positioning, and some compare it to TFT and Auto Chess. One calls the food system "unbalanced to the point of aggravation". Another notes "a definite lack of interactivity". Another says modifiers are limited, so PvP and new classes drive replay. — search summary over [Gamezebo](https://www.gamezebo.com/reviews/despots-game-review/), [Gigazine](https://gigazine.net/gsc_news/en/20211114-dystopian-army-builder/), [TheXboxHub](https://www.thexboxhub.com/despots-game-dystopian-army-builder-review/), [Gameluster](https://gameluster.com/review-despots-game-dystopian-army-builder-dungeon-crawlers-delight/), [IndieRanger](https://indieranger.com/review-despots-game)
- [V] Metacritic "mixed or average" (Wikipedia mirror, Mar 2026 snapshot). The Discord blurb promises fights against "enemies, and other players!". — [Wikipedia mirror](https://wiki.krisyotam.com/content/wikipedia_en_all_nopic_2026-03/Despot's_Game); [Discord](https://discord.com/game/despot-s-game-dystopian-army-builder-1124353373810995200)
- [V] Konfa continued the universe with "Slime 3K: Rise Against Despot", a survivor-like with deck-building. — [Game Developer press release](https://www.gamedeveloper.com/press-release/slime-3k-rise-against-despot-mixes-survivor-like-madness-with-strategic-deck-building-on-pc-this-november)

### Inferences
- **Narrative [I/U]:** Framing over plot. A sardonic AI overseer ("the Despot") runs humans through a maze. Humor comes from flavor text, weapon references and the grim food/sacrifice economy. The Superjump headline "Someone Call Sarah Connor" signals the AI-dystopia framing.
- **Animation [U]:** Small pixel sprites in large chaotic crowd battles. Readability comes from mass and VFX, not detailed per-unit animation.
- **UI [U]:** Simple room-node map plus a squad and shop screen. PC-first.
- **Monetization [U]:** Premium. Price not captured this session.
- **Technical complexity [I]:** Low to moderate. Many simple units with class behaviors, a node map and a pixel pipeline are within small-team range. The multiplayer mode adds backend work.
- **Transferable principles [I]:**
  1. *Upkeep that scales with squad size* (food per unit per move). A KGC-like run could charge supplies per hero per node, creating a "wide roster vs. deep run" trade-off and a reason to sacrifice or bench heroes.
  2. *Role from equipment, not body.* One base pixel body plus a weapon overlay and a class-behavior script cuts art cost sharply and makes "re-class" a strategic action.
  3. *Behavior-changing mutations at map nodes* (altars) rather than flat stat buffs. Pair them with economic agency (reroll, choose-1-of-3, lock) to avoid the "locked behind RNG" criticism.
- **Pitfalls [I]:** Long hands-off fights with little interaction; RNG-only access to build-defining upgrades; thin modifier variety.

### Gaps
- The competitive mode's actual mechanics (async snapshots or live) were not found.
- No sales or player numbers. No mobile version found. No developer interview on art pipeline or humor.

---

## 4. Guardian Tales (Kong Studios; Kakao Games global publisher): mobile + Switch; F2P gacha

### Takeaway
Shows that pixel art plus affectionate RPG parody plus Zelda-like puzzle exploration can carry a global gacha hero collector. Even the gacha is a joke ("Kamazon" deliveries). Criticism centers on stamina gating, gacha and PvP pay pressure, and pixel style putting off some players. Kong Studios is doubling down on pixel action with "Guardian Maiden" (Kakao global publishing deal, Jul 2026).

### Cited Findings
- [V] Developed by Kong Studios and published globally by Kakao Games. The Japanese version was self-published by Kong Studios with Shanghai Yostar and released 6 Oct 2021. — [Accessnewswire PR](https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/guardian-tales-a-global-hit-game-developed-by-kong-studios-enters-661117); [Wikipedia (via search)](https://en.wikipedia.com/wiki/Guardian_Tales)
- [V] Switch release 3 Oct 2022 (UK/EU). — [Time Extension](https://www.timeextension.com/companies/kong_studios); [Pocket Tactics](https://www.pockettactics.com/guardian-tales/switch)
- [V] Genres listed: Action, Puzzle, Arcade, RPG, with online play for 1-4 players. The store text promises lifting boulders, throwing bombs, uncovering hidden treasures, and dodge, attack and jump "manual-action". PvP uses a party of 3 heroes in real time. The listing claims 50+ heroes and 100 weapons, later 150+ "pixel heroes". The setting begins in Kanterbury under attack by "Invaders". — [Nintendo UK](https://nintendo.co.uk/Games/Nintendo-Switch-download-software/Guardian-Tales-2267901.html); [App Store](https://apps.apple.com/app/id1485526957)
- [V/C] Humor: TV Tropes calls it an "Affectionate Parody" of classic RPGs. Hero summons arrive through "Kamazon", an Amazon parody where you sign for the package, and the App Store sells a "Kamazon Shopping Package" IAP. A TapTap review notes pop-culture references throughout. PocketGamer's review is headlined "it's laughing with you, not at you". — [TV Tropes](https://www.tvtropes.org/pmwiki/pmwiki.php/VideoGame/GuardianTales); [App Store](https://apps.apple.com/app/id1485526957); [TapTap](https://www.taptap.io/post/8026157); [PocketGamer](https://ee.pocketgamer.com/articles/084102/guardian-tales-review-its-laughing-with-you-not-at-you/)
- [C] Screen Rant (Switch, 4/5): gameplay, art style and quirky characters are highlights, but the game is "bogged down by its mobile-game origins" such as stamina costs, and "the gacha mechanics will make or break" it. — [Screen Rant](https://screenrant.com/guardian-tales-review-nintendo-switch/)
- [C] Mobile Bytes: stamina limits daily play without paid refreshes. — [Mobile Bytes](https://mobilebytes.gg/rpg-games/guardian-tales-feels-right-at-home-on-the-nintendo-switch/). PocketGamer: it does not make you feel you must pay to win despite many currencies. — [PocketGamer](https://www.pocketgamer.com/guardian-tales/review/). Multiplayer.it: competitive PvP clearly pushes toward pay-to-win, and progression leans on grinding. — [Multiplayer.it](https://multiplayer.it/recensioni/guardian-tales-la-recensione.html)
- [V] OpenCritic lists Screen Rant 4/5, Pure Nintendo 8/10 and Nindie Spotlight 8.7/10. The Metacritic Switch user score is 6.9 from only 8 ratings. — [OpenCritic](https://opencritic.com/game/13816/guardian-tales); [Metacritic](https://legacy.prod.metacritic.com/game/switch/guardian-tales)
- [C] A QooApp reviewer says pixel style is "the most reason peoples skip the game", even though the art is modern and attractive. Another QooApp reviewer says gacha rates could be better but the gacha "can easily be ignored". — [QooApp](https://apps.qoo-app.com/en/comment-detail/6967639) (individual review links from search; attribution approximate)
- [V] On 28 Jul 2026 Kakao Games signed global publishing (Korea + global excluding Greater China) for Kong Studios' next title, Guardian Maiden, an action RPG for PC and mobile. PocketGamer calls it the "next pixel-art adventure" and says Kong "does crunchy pixel art so well". It is unconfirmed whether it relates to Guardian Tales. — [Asiae](https://view.asiae.co.kr/en/article/2026072817354035652); [Game Developer PR](https://www.gamedeveloper.com/press-release/new-action-rpg-guardian-maiden-announced-for-worldwide-release-on-pc-and-mobile); [PocketGamer](https://www.pocketgamer.com/guardian-maiden/announcement/)

### Inferences
- **Core loop [U]:** Story "worlds" with action stages, puzzles and secrets. Collect heroes and their signature weapons. Daily modes, guild raids and Arena/Colosseum PvP.
- **Combat [U]:** Real-time manual control of a leader with AI companions, plus chain skills (stun or knock-down states feeding follow-ups).
- **Art direction [U]:** Small, chunky pixel character sprites on top-down or slightly tilted environments with modern lighting and effects. A "retro SNES Zelda" pastiche with contemporary polish.
- **Animation [U]:** Frame-by-frame sprite animation on small canvases, with strong squash, hit-flash and screenshake for feedback. Pixel cut-ins for specials. No verified pipeline source.
- **Narrative [I]:** Comedy-first, parody of RPG and pop-culture tropes, but with sincere arcs per world. Humor also defuses monetization cynicism (Kamazon).
- **Technical complexity [I]:** Moderate to high. Action combat, puzzles, many handcrafted worlds, real-time PvP and live-ops. The pixel pipeline is feasible; the content volume is not.
- **Transferable principles [I]:**
  1. *Diegetic, self-aware monetization and recruitment framing* (a parody delivery service). Gives the summon screen personality and softens cynicism, as long as rates stay fair.
  2. *Interludes that change pace.* Light puzzles or exploration rooms between autobattles (event nodes, "secret" rooms) add variety without new combat systems.
  3. *Humor as a cheap retention driver.* Short, punchy text and visual gags suit mobile session lengths better than long VN dumps (contrast Arknights).
- **Pitfalls [I]:** Stamina gates; dual gacha (heroes + weapons) raising spend pressure; competitive PvP perceived as pay-to-win; pixel art reading as "cheap" in store thumbnails (counter with high-res key art and animated previews).

### Gaps
- No Kong Studios interview on pixel art or animation pipeline, puzzle design or humor writing found.
- 2025-2026 live status, revenue and whether Kong took over global publishing not confirmed.

---

## 5. Dungeon Maker: Dark Lord (GameCoaster): mobile; premium + IAP; offline

### Takeaway
Puts the player in the defender's chair. You are the Dark Lord, placing rooms, traps and facilities and hiring and training monsters against invading heroes, inside a roguelike day calendar (card choices each day, rest before a boss every 20th day). It was critically adored (TouchArcade, 2018). It sells as a $3.99 offline premium app with a large IAP catalog, some of it gameplay-affecting. GameCoaster's 2026 successor, Dungeon Within, keeps dungeon-building and monster squads but switches from real-time to turns.

### Cited Findings
- [V] iOS: paid ($3.99 US) with In-App Purchases. IAPs include a card-game DLC, "succession" packages, a Dark Lord awakening bundle and skin/costume packs. Big bundles reach about $25.99 ("Little Hero Costume Package") and $39.99 ("Myth full pack"). — [App Store](https://apps.apple.com/app/id1359652100)
- [V] TouchArcade review (22 Jun 2018), headline: "Hands Down One of the Greatest Dungeon Games You Will Ever Play". It is a roguelike that "seamlessly incorporates elements from the card, tower defense and strategy genres". You play the bad guys. A run starts with a chosen Dark Lord, random monsters and one battle room in the centre. Every 19th day is a row of cards that lets the Dark Lord rest, and every 20th day is a boss battle. The mix and placement of rooms matter for survival. Monsters can be trained to elite. A merchant card sells monsters and facilities. Facility rooms do nothing to heroes but buff the Dark Lord or monsters. — [TouchArcade review](https://toucharcade.com/2018/06/22/dungeon-maker-dark-lord-review/); [TouchArcade guide, May 2018](https://toucharcade.com/2018/05/24/dungeon-maker-dark-lord-guide/)
- [C] TouchArcade forum (2018): a "premium + offline game with some IAPs", and the developer said IAPs help "pay the bills". — [TouchArcade forum](https://toucharcade.com/community/threads/dungeon-maker-dark-lord-by-gamecoaster.319369/)
- [C, low reliability, auto-generated aggregator] 4.62/5 from about 55k reviews, described as premium with no ads. — [marlvel.ai](https://marlvel.ai/api/llm/apps/games/com-gamecoaster-dungeonmaker)
- [V] **Dungeon Within** (GameCoaster) "harkens back to" Dungeon Maker: Dark Lord with dungeon building and monster squads, but "where DMDL was entirely real time, this uses a turn system". Release date 20 Apr 2026 per Discord. — [App Store](https://apps.apple.com/app/id6761328517); [Discord](https://discord.com/game/dungeon-within-1509034691410268240)

### Inferences
- **Combat [U]:** Heroes walk a path of rooms toward the Dark Lord. Each room resolves a small auto-fight between the room's monsters (or trap effect) and the party. The Dark Lord fights last.
- **Art and animation [U]:** Cute low-resolution pixel sprites, room-tile dungeon view, simple attack and hit animations. Charm comes from monster variety and Dark Lord personalities.
- **Narrative [U]:** Light; each Dark Lord has a flavor premise. The "you are the villain" inversion is the hook.
- **Progression [I/U]:** Within a run: rooms, monsters, elite training, Dark Lord HP. Between runs, unlocks and "succession", which is partly monetized per the IAP list.
- **Replayability [I]:** Multiple Dark Lords with distinct kits, random cards and merchants, and an escalating calendar with boss gates.
- **Technical complexity [I]:** Low to moderate. Offline and single-player, data-driven content, small sprites. Well within small-team range and the closest scope comparable here.
- **Transferable principles [I]:**
  1. *Defender framing on a tiny map.* "Heroes invade, you place units in slots or rooms" turns positioning into **path/ordering design**, which maps neatly onto a KGC-like small battlefield (KGC itself is defend-the-castle).
  2. *Calendar pacing:* daily pick, a rest beat, then a boss every N days. Readable tension curves in a roguelike.
  3. *Facilities vs. combat rooms.* Some slots buff your side instead of fighting, so occupying a slot has an opportunity cost.
- **Pitfalls [I]:** Selling gameplay-affecting "succession/awakening" packs on top of a paid app risks double-dip complaints (not verified as a widespread complaint). Real-time auto-resolution may be opaque, which Dungeon Within's move to turns may be addressing.

### Gaps
- Could not read the full TouchArcade review or find player criticism on Reddit or Google Play.
- Android pricing and model, sales figures, and Dungeon Within reception not found.
- That it is pixel art is assumed ([U]).

---

## 6. Arknights (Hypergryph; Yostar global): mobile tower-defense hero collector; F2P gacha; live

### Takeaway
Placement and timing matter because deployment is a **tempo economy**. Deployment Points (DP) regenerate slowly, re-deploying costs escalate (×1.5 then ×2), and redeploy timers lock units out. Block counts and tile types (melee on ground, ranged on high ground) constrain where each class can go. Eight classes split into many sub-archetypes with distinct traits, which prevents stat-stick sameness. The story is a skippable visual novel, praised for depth and criticized as walls of text. The permanent roguelike mode Integrated Strategies (recruit from scratch with a run currency) is directly relevant to a hero-collection roguelike.

### Cited Findings
- [V] DP is needed to deploy operators, summons and devices, and accumulates over time or via skills. Melee operators go on ground tiles, ranged on elevated tiles. — [Arknights Terra Wiki: Deployment Point](https://arknights.wiki.gg/wiki/Deployment_Point)
- [V] Retreating refunds part of the cost (usually 50%; 100% for Kill-DP-Recovery Vanguards). Re-deploy cost rises ×1.5 on the first redeploy and ×2 afterwards, capped at 99. Deaths refund nothing. Summons and deployables do not escalate. — [Terra Wiki: Cost](https://arknights.wiki.gg/wiki/Attribute/Cost); [GamePress](https://gamepress.gg/node/39291)
- [V] Redeployment time is the wait before re-placing a unit. Fast-Redeploy is a trait (Executors, Merchant Specialists, Agent Vanguards). — [Terra Wiki: Redeployment time](https://arknights.wiki.gg/wiki/Redeployment_time); [Terra Wiki: Operators](https://arknights.wiki.gg/wiki/Operators)
- [V] **Block** is how many enemies a unit can stop at once; extras walk past. AoE Guards hit as many enemies as their current block. Pioneers block 2 while Chargers block 1, a safety vs. DP-gain trade-off. — [GamePress](https://ak.gamepress.gg/node/11736); [GamePress](https://gamepress.gg/node/11746); [Terra Wiki: Intermediate Guide](https://arknights.wiki.gg/wiki/Intermediate_Guide)
- [V] There are 8 classes (Caster, Defender, Guard, Medic, Sniper, Specialist, Supporter, Vanguard). Class mainly sets tile eligibility, and archetypes or sub-classes define specific roles. Vanguards are usually deployed first: cheap, with DP-recovery skills. — [GamePress: Stay Classy](https://gamepress.gg/node/39426); [class guide blog](https://guide-wodn.blogspot.com/2020/01/arknights-class-guide.html)
- [V; search summary] Naavik describes the loop as deploying operators rather than upgrading towers with mid-fight resources, with slow DP regeneration pacing the defense. — [Naavik deep dive](https://naavik.co/deep-dives/arknights-tower-defense-redefined/)
- [V] **Integrated Strategies (IS)** is a permanent roguelike mode unlocked after stage 3-8. Runs are floors of nodes and you start with no team. You recruit with the run currency "Hope", where higher rarity costs more and "Temporary Recruitment" is free. Operator levels, skills and potentials carry over from the account. Themes are numbered #1 to #6 with different gimmicks, and some were CN-first. — [Terra Wiki: Integrated Strategies](https://arknights.wiki.gg/wiki/Integrated_Strategies)
- [C] Kotaku (2022): IS "forced me to use the free gacha characters I had long retired". — [Kotaku](https://kotaku.com/arknights-roguelike-integrated-strategy-gacha-1849197379)
- [V] Gacha: 6★ rate +2% per pull once 50 pulls pass without a 6★ (resets on a 6★). Standard and special banners share a counter; limited banners track separately. Special banners have a 150-pull rate-up guarantee. — [Terra Wiki: Headhunting](https://arknights.wiki.gg/wiki/Headhunting); [Fandom: Banners](https://arknights.fandom.com/wiki/Headhunting/Banners)
- [C] Reputation: "one of the most free-to-play-friendly gacha games" (2023). A Mein-MMO review headline calls it a "Cure against (greedy) Gacha Games". — [Sportskeeda 2023](https://sportskeeda.com/esports/is-arknights-free-to-play-friendly); [Mein-MMO](https://mein-mmo.de/en/review-of-the-free2play-tactic-rpg-arknights-cure-against-greedy-gacha-games,865002)
- [C] Story: presented mostly as a visual novel; it "tells a lot, but unfortunately shows too little"; it can be skipped and caught up later. — [Mein-MMO](https://mein-mmo.de/en/review-of-the-free2play-tactic-rpg-arknights-cure-against-greedy-gacha-games,865002). A player says event story is often "a wall of text". — [Steam discussion, anecdotal](https://steamcommunity.com/app/1973530/discussions/0/3771239049942840764/?ctp=2)
- [V] **Status:** the spin-off *Arknights: Endfield* was reviewed in early 2026 ("Anime Factorio Versus Routine", 9 Feb 2026). Its 6★ base rate is 0.8%, guaranteed at 80, with the featured unit at 120. Push Square calls its narrative a "spaghetti of proper nouns". Developers say Hypergryph's tower-defense background (placement, resources, efficiency) shaped Endfield's base-building. — [iXBT](https://ixbt.games/en/reviews/2026/02/09/obzor-arknights-endfield-anime-factorio-protiv-rutiny.html); [Game8](https://game8.co/games/Arknights-Endfield/archives/576231); [Push Square](https://pushsquare.com/reviews/ps5/arknights-endfield); [Final Weapon, 11 Nov 2025](https://finalweapon.net/2025/11/11/interview-gryphline-on-arknights-endfield-exploring-new-possibilities-for-the-series/)

### Inferences
- **Combat [U]:** Real time with 1×/2× speed and slow-mo while placing. Skills are auto- or manually triggered by SP. Facing direction on placement sets the attack range shape, a key positioning decision.
- **Art direction and animation [U]:** High-end anime illustrations with dark industrial-sci-fi UI. In battle, 2D chibi operators use skeletal (Spine-style) animation on a tilted 3D-looking stage. Not pixel art. Its stylish, minimal UI is often cited as a strength.
- **Difficulty [I/U]:** Authored stages with hard challenge modes (Contingency Contract, challenge mode). High-end clears often depend on guides, and community "low-rarity clears" are a culture.
- **Retention [I]:** Story events, base management, IS seasons and monthly modes. The generous pity reputation drives goodwill.
- **Technical complexity [I]:** High in content (hundreds of operators and stages, VN script volume). The core deploy/DP/block/tile system is very buildable in 2D for a small team.
- **Transferable principles [I]:**
  1. *Deployment as a tempo resource.* A KGC-like game could add a mid-battle "summon from bench" using a regenerating meter, with retreat refunds and escalating redeploy cost. This gives a manual skill layer on top of auto combat without full micro.
  2. *Class decides where; archetype decides how.* Restrict tile eligibility by class, then give each sub-archetype a rule-bending trait (hits up to block count, fast redeploy, ignores block). Units differ in verbs, not just numbers.
  3. *Roguelike mode that "levels the field but honors collection".* A run currency recruits heroes inside the run and free temporary recruits keep unowned heroes viable. It resurfaces neglected units, which is good for both retention and monetization fairness.
- **Pitfalls [I]:** Long VN text dumps on mobile; stage puzzles with one "correct" solution that push players to guides; content treadmill scale.

### Gaps
- No primary Hypergryph or Yostar interview on the original game's deployment or class design found. Naavik content was not readable directly.
- Revenue and player counts not gathered. Spine and animation details unverified.

---

## 7. Super Auto Pets (Team Wood Games): PC + mobile; F2P with packs; live

### Takeaway
Minimal-scope, maximal-readability async autobattler. A 5-pet **linear** team where order is the positioning, trigger-word abilities (buy, sell, faint, start of battle), tiny shops with roll and freeze, and arena runs bounded by lives and wins. It was built by a two-person team. It is F2P with pet packs, a free weekly pack and a cheap subscription, and its monetization is generally seen as fair. Criticisms are RNG shop frustration, pack-gated pets in PvP felt as pay-to-win (contested), and early pets going obsolete.

### Cited Findings
- [V] Arena mode: untimed, asynchronous battles against opponents picked from a pool of teams; start with 5 lives, lose one per defeat, win at 10 victories. Versus: asynchronous or real-time 1v1 or 8-player lobbies, last player standing. If no players exist at that turn, you face AI-generated teams. — [Wikipedia (via search/Wikiwand)](https://www.wikiwand.com/en/articles/Super_Auto_Pets)
- [V] Version 0.28 (Sep 2023) added ranked 1v1 with a score that governs matchmaking. — [SAP Wiki: Version 0.28](https://superautopets.wiki.gg/wiki/Version_0.28)
- [V] Rolling costs 1 gold and refreshes the shop. Freezing keeps a shop item across rolls but occupies a slot. — [SAP Wiki: The Basics](https://superautopets.wiki.gg/wiki/The_Basics)
- [C, 2022] Two developers worked on it for about 1.5 years, growing to 3 full-time staff plus 2 freelancers. Multi-platform was planned early. The devs do not disclose payer counts. Discord had 35k+ members. — [Medium/CodeX](https://medium.com/codex/why-super-auto-pets-is-so-good-and-what-is-still-to-come-5c02854c675b)
- [V] Store pages describe a "chill free-to-play auto battler". — [App Store](https://apps.apple.com/app/id1597449908); [Steam](https://store.steampowered.com/app/1714040/Super_Auto_Pets/)
- [C] Monetization: the free tier is "generous", with a rotating Weekly Pack free players can choose. Pricing snapshot: Plus $1.99/month; packs and items from $0.99 to $9.99 (Puppy $4.99, Star $9.99). — [TapTap review](https://www.taptap.io/post/1557189); [Adapty paywall library](https://adapty.io/paywall-library/super-auto-pets/)
- [C, conflicting] An aggregator says monetization is "generally praised for being fair, non-intrusive, and free of ads", with an 89% user score from about 30k reviews. An auto-generated Steam-review summary lists "Pay-to-win dominates" and "Unfair matchmaking" among common complaints. — [GameBrain](https://gamebrain.co/game/super-auto-pets); [VaporLens](https://vaporlens.app/app/1714040/super_auto_pets)
- [C] RNG criticism: one critic calls it "fundamentally a luck/gambling simulator" because of shop rolls. A Steam suggestion says low-tier pets become useless mid-game and proposes a "Hibernate" option and a gold-to-upgrade shop item. — [GameBrain](https://gamebrain.co/game/super-auto-pets); [Steam discussion](https://steamcommunity.com/app/1714040/discussions/0/5260782129619975331)
- [C] PocketGamer review: "chill auto chess game with deep strategic gameplay". — [PocketGamer](https://ee.pocketgamer.com/articles/084151/super-auto-pets-review-chill-auto-chess-game-with-deep-strategic-gameplay/)

### Inferences
- **Core loop [U]:** About 10 gold per turn; pets cost 3, roll 1, sell for gold. New shop tiers unlock as turns progress. Merge duplicate pets to level them. Food items buff pets. Battle resolves front pet vs front pet.
- **Positioning [I]:** Order is everything. Who takes the first hit, who sits behind a "faint" trigger, who buffs the pet ahead. One dimension, fully readable.
- **Art and animation [U]:** Flat, emoji-like animal icons with bounce, tween and particle "animation". Near-zero per-unit animation cost. Charm comes from the pets and the sound.
- **Narrative [U]:** None.
- **UI [I]:** Huge touch targets, a single screen with drag and drop. A gold standard for mobile autobattler readability.
- **Technical complexity [I]:** Low (art and sim) to moderate (async backend, ranked, packs, cross-platform accounts).
- **Transferable principles [I]:**
  1. *Readable positional rules on a tiny board.* Simple adjacency or order rules make positioning matter without hex-board complexity. A KGC-like 3x3 to 5x5 board should keep the rules this legible (front row tanks, behind-ally triggers).
  2. *Trigger vocabulary.* A dozen keywords (on deploy, on ally death, start of battle, on hurt) compose hundreds of combos cheaply. Each pixel unit only needs one verb.
  3. *Bounded runs: lives plus a win target.* 5 lives and 10 wins makes run length predictable (mobile-friendly) and softens variance, because one bad roll is not fatal.
- **Pitfalls [I]:** Selling packs that put new units into ranked PvP invites pay-to-win perception. Early units with no late-game role ("dead tiers"). Unmitigated shop RNG.

### Gaps
- No primary Team Wood interview on async design, matchmaking pool or anti-cheat found.
- No current (2026) player or revenue data found.

---

## 8. Backpack Battles (PlayWithFurcifer; publisher Shochiku Games for Japan materials): PC + mobile; premium

### Takeaway
Turns the **inventory grid into the battlefield**. Shapes, adjacency "stars/diamonds" and recipes formed by placing items next to each other make spatial arrangement the core decision. Async PvP pits you against other players' saved builds. Made by a two-person team, it sold over 1M copies in Early Access, reached 1.0 in June 2025 and launched on mobile at $9.99 in Feb 2026. Community worries: suspected cheated or impossible builds in the async pool, and balance and meta abuse.

### Cited Findings
- [V] Developer PlayWithFurcifer, a couple who began it as an after-hours side project. — [PC Gamer](https://pcgamer.com/games/action/steams-latest-breakout-indie-hit-is-a-fantasy-autobattler-about-how-many-magic-items-you-can-fit-in-your-backpack)
- [V/C] Async: your backpack fights other players' builds, not live opponents, and the build you face "may have been made hours earlier". Decision appeal without waiting through others' fights; fights can be skipped. — [PC Gamer](https://pcgamer.com/games/arrange-your-items-to-optimize-your-fights-in-asynchronous-autobattler-backpack-battles); [Green Man Gaming blog](https://www.greenmangaming.com/blog/backpack-battles-turns-inventory-management-into-a-moreish-pvp-game/)
- [V] Items have grid shapes, and many buff only adjacent items. "Stars" and "diamonds" are adjacency activation slots; an item usually fills one star and one diamond of another. Recipes: adjacent ingredients show a thick gold line and combine at the next shop, and you can lock items to prevent combining. Buffs include Empower (+1 weapon damage per stack), Heat (+2% trigger speed per stack) and Luck (+5% accuracy per stack); crits deal double. Each shop item has a 10% chance to be on sale at half price. Unique items can appear from round 4, one at a time. — [Backpack Battles Wiki: Game Mechanics](https://backpackbattles.wiki.gg/wiki/Game_Mechanics); [EarlyGuides](https://earlyguides.com/backpack-battles/beginners-guide)
- [C, conflicting] Run length and lives: one guide says 5 hearts per run. The wiki reportedly says players start with 12 gold and 25 health, growing per round. Another summary describes 10 rounds plus an optional Survival Mode to round 18. Likely version differences; verify in-game. — [EarlyGuides](https://earlyguides.com/backpack-battles/beginners-guide); [Wiki](https://backpackbattles.wiki.gg/wiki/Game_Mechanics)
- [V] Sales: 100k units two days after Early Access launch (Mar 2024). 500k in two weeks. 640k by 8 Apr 2024, with China the top country. Over 1M copies in Early Access, about 40 updates and about 35M hours played. 1.0 released 14 Jun 2025 (JST) with two new classes, $11.99 at 20% off at launch. — [Game Developer](https://gamedeveloper.com/business/backpack-battles-sells-100-000-units-two-days-after-early-access-launch); [GamingOnLinux, Mar 2024](https://www.gamingonlinux.com/2024/03/backpack-battles-has-sold-500000-copies-in-two-weeks-on-steam); [Game World Observer, 25 Apr 2024](https://gameworldobserver.com/2024/04/25/backpack-battles-sales-640k-copies-china-top-country); [GameDiscoverCo](https://newsletter.gamediscover.co/p/how-backpack-battles-sold-650k-copies); [Shochiku Games](https://game.shochiku.co.jp/?p=144); [PCGamesN](https://www.pcgamesn.com/backpack-battles/1-0-launch-inventory-auto-battler)
- [V] Mobile: announced for 4 Feb 2026 at $9.99, with the same classes and items as PC. PocketGamer reports it "out now on iOS and Android". — [Shochiku Games](https://game.shochiku.co.jp/?p=117); [PocketGamer](https://www.pocketgamer.com/backpack-battles/official-launch-android-ios)
- [C] About 90% positive Steam reviews (Mein-MMO headline). — [Mein-MMO](https://mein-mmo.de/en/an-indie-hit-from-germany-has-90-positive-reviews-on-steam-now-even-better-thanks-to-a-big-update,1398230)
- [C, anecdotal] Steam threads suspect cheats from "suspiciously lucky" early builds, though one poster saw more abuse of powerful (legitimate) builds. Another player reported an "impossible-looking" build to the dev. An itch.io user complains of being kicked "for cheating just for playing good". A thread asks how ranked matchmaking works, with no official answer in-thread. — [Steam](https://steamcommunity.com/app/2427700/discussions/0/4035851529336381025); [Steam](https://steamcommunity.com/app/2427700/discussions/0/6770657417430301203); [itch.io comments](https://playwithfurcifer.itch.io/backpack-battles/comments?before=42)

### Inferences
- **Combat [I/U]:** Fully automatic. Weapons fire on cooldowns, and stamina, buffs and debuffs resolve over time. The battle is a readout of the build's timing math.
- **Art and animation [U]:** Hand-drawn 2D cartoon item icons. Animation is mostly icon pulses, projectiles and numbers. Very low animation cost; the items are the "characters".
- **Narrative [U]:** Minimal. Furcifer the shopkeeper gives personality.
- **Progression [I/U]:** Within a run: items and recipes. Between runs: ranked rating, classes and subclasses. No power carry-over.
- **Technical complexity [I]:** Low to moderate for the sim and UI. The async backend, ranked play and anti-cheat are the real engineering work.
- **Transferable principles [I]:**
  1. *Relational positioning.* Adjacency auras and links between heroes ("buffs the unit to its right", "shares shield with diagonal") make a tiny KGC-like grid strategically rich.
  2. *Visible pre-commit previews.* Show synergy and recipe lines before confirming; the gold line is an excellent discoverability device.
  3. *Small shop affordances that tame variance:* random sale prices, lock/hold, and caps on uniques.
- **Pitfalls [I]:** Async pool contamination by cheated builds. Opaque matchmaking explanations breed distrust. Dominant builds that the pool keeps replaying.

### Gaps
- No official statement on anti-cheat, server validation or opponent selection (same round? rating band?) was found.
- Current run structure (hearts vs HP; 10 vs 18 rounds) unresolved. Mobile sales not found.

---

## 9. Optional: The Bazaar (Tempo, created by Reynad): PC; F2P; async-ghost roguelike autobattler

### Takeaway
Included as a cautionary case for **async-ghost PvP plus monetization**. Players fight recorded ghosts of other players' builds. When the paid season-pass tier gated character expansions and was seen as speeding up item acquisition, despite earlier "truly free-to-play" messaging, there was a major backlash. The creator dismissed it at first, then Tempo walked the changes back in Season 1. Ghosts built by far more experienced players also fed frustration.

### Cited Findings
- [V/C] PvP uses recorded ghosts of other players' builds, with no live matchmaking or timer. One source notes the frustration of facing builds from players "with vastly more knowledge and experience". — [PC Gamer](https://pcgamer.com/games/roguelike/the-bazaar-could-be-the-future-of-autobattlers-if-it-stops-strangling-itself-to-death-with-its-own-microtransactions); [Mobalytics review](https://mobalytics.gg/gamebase/reviews/the-bazaar-review)
- [V] At open-beta launch, character expansion packs were locked behind the paid season-pass tier, and players said the paid pass could speed up hero item acquisition. Tempo had earlier called the game "truly Free-to-Play". Reynad called criticism "dramatized fearmongering" and preferred players "vote with their wallets". — [PC Gamer](https://www.pcgamer.com/games/card-games/early-backers-of-game-decry-bait-and-switch-after-it-backtracks-on-monetisation-promises-dev-chooses-to-stir-the-pot-seeing-reddit-lose-it-lets-me-breathe-a-huge-sigh-of-relief); [OpenCritic News](https://opencritic.com/news/13549/the-bazaar-creator-says-monetisation-feedback-is-dishonest-and-studio-wont-back-down); [GamePressure](https://www.gamepressure.com/newsroom/is-the-bazaar-pay-to-win-players-complain-about-monetization/zd7aad); [PCGamesN](https://www.pcgamesn.com/the-bazaar/patch-prize-pass-controversy)
- [V] Season 1 patch notes walked back the controversial changes. A later review says character expansions are generally free or unlockable through play, while new heroes remain paid. The game came to Steam on 13 Aug 2025. — [PCGamesN](https://www.pcgamesn.com/the-bazaar/season-1-patch-notes-monetization); [PC Gamer](https://pcgamer.com/games/card-games/we-are-so-back-after-a-month-of-spent-strangling-itself-with-monetisation-promising-new-auto-battler-the-bazaar-finally-makes-things-right-for-its-players); [Mobalytics](https://mobalytics.gg/gamebase/reviews/the-bazaar-review)
- [C] Critics also accused the team of banning dissenters from official forums. — search summary over the PC Gamer and OpenCritic pieces above (attribution approximate)

### Inferences
- **Date conflict:** The search summary placed the open-beta flashpoint in March 2025. My recollection ([U]) is December 2024 to January 2025. Verify before citing a date.
- **Transferable principles [I]:**
  1. Never sell run-power or acceleration in a mode with PvP ghosts. Monetize identity (cosmetics, alternate pixel skins) and possibly new heroes, with free unlock paths.
  2. Bucket ghost pools by rating and progress, so new players are not fed veteran ghosts.
  3. State the business model early and keep to it; reversals cost trust out of proportion.
- **Pitfall:** Combative developer communication magnifies monetization controversies.

### Gaps
- Core loop details (day/hour structure, item cooldown board, encounter choices) not researched because the search budget ran out.
- Mechabellum, Hero Wars and AFK Arena/AFK Journey were not covered.

---

## 10. Cross-cutting: how autobattlers create meaningful pre-combat decisions, make positioning matter and keep variance fun

### Takeaway
With combat automated, these games push decisions into **economy (save vs. spend, interest), shop manipulation (roll, freeze, lock, sale), merging (copies to star-ups), crafting (components, adjacency recipes), synergy tags (traits, classes-by-weapon) and placement (corners and rows, linear order, adjacency, deployment timing)**. Variance stays fun when players have **agency over it** (bank, freeze, reroll, choose 1 of 3), **visibility** (previews, odds), **cushioning** (lives, HP pools, pity or bad-luck protection) and **short runs**.

### Cited Findings
- Economy as decision: interest (+1 per 10 gold, cap +5), streak gold, roll vs. level. — [Upcomer](https://upcomer.com/teamfight-tactics-how-to-manage-your-economy-in-tft/); [Mobalytics](https://mobalytics.gg/blog/tft/how-to-manage-your-economy-in-teamfight-tactics-three-strategies/); [Bamboo Gaming](https://www.bamboogaming.net/tft/economy)
- Shop control: SAP roll for 1 gold and freeze at the cost of a slot. — [SAP Wiki](https://superautopets.wiki.gg/wiki/The_Basics). Backpack Battles: 10% sale chance at half price, item lock, one unique at a time. — [BB Wiki](https://backpackbattles.wiki.gg/wiki/Game_Mechanics)
- Crafting by placement: BB recipes trigger when ingredients sit adjacent (gold line preview). — [BB Wiki](https://backpackbattles.wiki.gg/wiki/Game_Mechanics)
- Synergy by equipment: Despot's Game classes come from weapons, with abilities when same-class units hold different weapons. — [gameplay.tips](https://gameplay.tips/guides/despots-game-dystopian-army-builder-beginners-tips.html)
- Positioning drivers: TFT counter-positioning against divers, hooks and Zephyr. — [Mobalytics](https://mobalytics.gg/blog/tft-guide-how-to-climb-to-gold/). Arknights tile types, block counts, escalating redeploy cost and timers. — [Terra Wiki: Cost](https://arknights.wiki.gg/wiki/Attribute/Cost); [GamePress](https://ak.gamepress.gg/node/11736). BB adjacency stars and diamonds. — [BB Wiki](https://backpackbattles.wiki.gg/wiki/Game_Mechanics)
- Variance philosophy: "mathematically correct does NOT mean the design is perfect"; don't let RNG "take the wheel". — [Dot Esports](https://dotesports.com/?p=1245514). Item bad-luck protection. — [Screen Rant](https://screenrant.com/teamfight-tactics-bad-luck-protection-items-rng/). Augment skill-floor diversity. — [Riot GAT](https://teamfighttactics.leagueoflegends.com/en-au/news/dev/talking-tactics-game-analysis-team-gat/)
- Variance done badly: Despot's mutations "locked behind RNG" with no economic skill to offset luck. — [Superjump](https://www.superjumpmagazine.com/despots-game-review/). SAP "luck/gambling simulator" complaint. — [GameBrain](https://gamebrain.co/game/super-auto-pets)
- Cushioning: SAP arena gives 5 lives and needs 10 wins. — [Wikiwand/Wikipedia](https://www.wikiwand.com/en/articles/Super_Auto_Pets)

### Inferences
- **What makes positioning matter on a small KGC-like board [I]:**
  - (a) Targeting rules that can be exploited or countered: nearest-target melee, backline-jumping assassins, pull/push, line or cone AoE.
  - (b) Facing and range shapes (Arknights' directional ranges).
  - (c) Relational buffs: adjacency, row and column auras, "ally behind".
  - (d) Lane or block mechanics: blockers stop N enemies and leakers hit the castle.
  - (e) Visible enemy intents or formations before placement, so placement is a response, not a guess.
  - Without at least two of these, players' positioning converges on one optimal layout.
- **Variance kit for the game [I]:**
  - Choose 1 of 3 for every reward.
  - Free reroll tokens tied to economy.
  - Freeze or lock.
  - Pity on rare heroes and items within a run.
  - A lives or HP buffer.
  - Visible next-fight preview.
  - Interest-capped banking.
  - Runs of 15 to 25 minutes.
- **Synergy design [I]:**
  - Two tags per hero (origin + role) or role-by-equipment.
  - Breakpoints of 2/4/6 on a small board. Breakpoints must scale to board size; a 5x5 board cannot support TFT's 6-to-9 trait tiers.
  - Watch early access to deep breakpoints (Riot lesson).

### Gaps
- No quantitative study found on how players perceive variance (e.g., retention vs. shop odds) beyond Riot's commentary.

---

## 11. Cross-cutting: asynchronous PvP (snapshot or ghost opponents), server and anti-cheat implications

### Takeaway
SAP (arena and async versus), Backpack Battles and The Bazaar match you against **stored snapshots of other players' teams or builds**. SAP falls back to AI teams when no player snapshot exists for that turn and runs a score-based ranked 1v1. This removes waiting and live netcode, which fits mobile. It also creates new problems: a ghost pool that can be poisoned by cheated builds, mismatched experience levels, and opaque matchmaking that breeds distrust. No developer-published architecture or anti-cheat writeups were found in this session.

### Cited Findings
- SAP: untimed async arena against "a pool of teams"; AI teams "if there are no players at that turn"; ranked score matchmaking since v0.28 (Sep 2023). — [Wikiwand/Wikipedia](https://www.wikiwand.com/en/articles/Super_Auto_Pets); [SAP Wiki](https://superautopets.wiki.gg/wiki/Version_0.28)
- Backpack Battles: you fight builds that may be hours old; skippable fights. — [PC Gamer](https://pcgamer.com/games/arrange-your-items-to-optimize-your-fights-in-asynchronous-autobattler-backpack-battles). Players suspect impossible or cheated builds and ask how ranked matching works. — [Steam](https://steamcommunity.com/app/2427700/discussions/0/4035851529336381025); [Steam](https://steamcommunity.com/app/2427700/discussions/0/6770657417430301203)
- The Bazaar: ghosts from much more experienced players frustrate newer players. — [PC Gamer](https://pcgamer.com/games/roguelike/the-bazaar-could-be-the-future-of-autobattlers-if-it-stops-strangling-itself-to-death-with-its-own-microtransactions)
- General async design (Soren Johnson): async play favors mechanics that "minimize waiting and keep players involved". — [Game Developer: Analysis: Asynchronicity in Game Design](https://www.gamedeveloper.com/game-platforms/analysis-asynchronicity-in-game-design)
- Despot's Game's Discord blurb promises fighting "other players", but the mechanics are unknown. — [Discord](https://discord.com/game/despot-s-game-dystopian-army-builder-1124353373810995200)

### Inferences (architecture and anti-cheat; not sourced, design reasoning)
- **Snapshot record:** `{build (units, items, positions, levels), round/turn index, player rating, game version/balance hash, RNG seed, timestamp}`. The pool is indexed by (version, round, rating band). Purge it on balance patches, or tag by version, to avoid stale-meta ghosts.
- **Determinism:** Make combat a pure function of (snapshot A, snapshot B, seed), using fixed-point or integer math and a fixed tick. The client can render it, but ranked results should be re-simulated server-side or sampled for audit. Cross-device float divergence is the classic trap.
- **Build legality:** Generate shop rolls from server-seeded RNG and log purchases, so the server can verify that a submitted build was reachable (gold spent, items offered, recipes valid). Without this, a modded client can upload impossible builds that poison other players' pools, which is exactly what Backpack Battles players suspect.
- **Cost profile:** Storage and compute are cheap (small JSON snapshots, sub-millisecond 2D sims). A serverless or small-VM backend is feasible for a small team. The expensive parts are moderation tooling, rating integrity and balance-patch versioning.
- **Fairness UX:** Show the opponent's name and rank, offer replays, explain "you fought X's build from round N", and use AI fallback for empty buckets (as SAP does). Bucket by rating to avoid veteran-ghost stomps (the Bazaar lesson).
- **Single-player-first option:** A KGC-like roguelike can ship PvE first and add an "async gauntlet" (fight ghosts of other players' run-end parties) later. This defers backend risk.

### Gaps
- No primary sources found on SAP, BB or Bazaar server validation, ghost selection or anti-cheat. The search budget was exhausted before targeted searches on deterministic simulation and anti-cheat could run.

---

## 12. Cross-cutting: monetization and fairness perception, plus compact comparison matrix

### Takeaway
Fairness perception tracks one line: **does money buy run power or PvP advantage?**
- Premium titles (Backpack Battles, Despot's Game) avoid the issue.
- Cosmetic-only F2P (TFT) draws price complaints but not fairness ones.
- Gacha hero collectors are judged on pity generosity (Arknights praised) and on stamina and PvP pressure (Guardian Tales mixed).
- Pack-based autobattlers (SAP) get some pay-to-win grumbling when packs feed ranked.
- Monetizing acceleration in a ghost-PvP game (The Bazaar) caused a crisis.
- Dungeon Maker shows the "paid app + gameplay IAP" hybrid.

### Cited Findings
- TFT: cosmetic gacha (Treasure Realms) with price and odds changes. — [Riot](https://teamfighttactics.leagueoflegends.com/en-sg/news/dev/tft-treasure-realms-a-new-portal-to-personalization/). Prestige pricing backlash. — [Dexerto](https://dexerto.com/league-of-legends/lol-players-rebel-against-disgusting-prices-with-new-prestige-tft-skin-2311243)
- Arknights: 50-pull soft pity at +2% per pull and a 150-pull special-banner guarantee. — [Terra Wiki](https://arknights.wiki.gg/wiki/Headhunting). F2P-friendly reputation. — [Sportskeeda](https://sportskeeda.com/esports/is-arknights-free-to-play-friendly)
- Guardian Tales: stamina and gacha criticism; PvP pay-to-win claims vs. "doesn't feel pay-to-win". — [Screen Rant](https://screenrant.com/guardian-tales-review-nintendo-switch/); [Multiplayer.it](https://multiplayer.it/recensioni/guardian-tales-la-recensione.html); [PocketGamer](https://www.pocketgamer.com/guardian-tales/review/)
- SAP: F2P, free weekly pack, packs $0.99 to $9.99, Plus $1.99/month; mixed fairness signals. — [Adapty](https://adapty.io/paywall-library/super-auto-pets/); [GameBrain](https://gamebrain.co/game/super-auto-pets); [VaporLens](https://vaporlens.app/app/1714040/super_auto_pets)
- Backpack Battles: premium (PC 1.0 launch $11.99 at 20% off; mobile $9.99). — [Shochiku](https://game.shochiku.co.jp/?p=144); [Shochiku](https://game.shochiku.co.jp/?p=117)
- Dungeon Maker: $3.99 plus IAPs up to $39.99, including succession and awakening packs. — [App Store](https://apps.apple.com/app/id1359652100)
- The Bazaar: paid-pass gating backlash, then Season 1 reversal. — [PCGamesN](https://www.pcgamesn.com/the-bazaar/season-1-patch-notes-monetization)

### Inferences: compact comparison matrix
Legend: tags as above. "Small-team build" is a 1-5 difficulty estimate [I] for building something *similar in scope*.

| Game | Platform / status (Nov 2026) | Business model | Battlefield & placement | Main pre-combat levers | Run vs. meta progression | Art / animation | PvP form | Small-team build |
|---|---|---|---|---|---|---|---|---|
| TFT | PC + mobile; Set 17 (Apr), Set 18 (Aug), Set 19 due ~late Nov/Dec 2026 [V] | F2P cosmetics + cosmetic gacha [V] | Hex board, ~28 slots per side [U] | Interest, roll vs. level, items, traits, augments [V] | Run only; cosmetic meta [I] | 3D League models, VFX-heavy [U] | Live 8-player [U] | 5 (scope); systems 2-3 |
| Auto Chess (mobile) | Mobile/PC/PS4; niche (Steam ~200-400 CCU snapshot) [C] | F2P cosmetics/pass [U] | Chess grid half-board [U] | Shared pool, gold/interest, race + class [U] | Run only [I] | Stylized 3D [U] | Live 8-player [U] | 4-5 |
| Despot's Game | PC, Xbox, PS, Switch; 1.0 Sep 2022 [V] | Premium [U price] | Squad formation in rooms [C] | Food upkeep, tokens, weapons = class, mutations [V] | Run + light unlocks [U] | Pixel, crowd battles [V/U] | Competitive mode, mechanics unknown [V] | 2-3 |
| Guardian Tales | Mobile + Switch; live [V/U] | F2P gacha (heroes + weapons), stamina [C] | Real-time action, party of 3-4 [V/U] | Team and weapon choice, chain skills [U] | Persistent collection [U] | Chunky pixel sprites, comedic [C/U] | Real-time 3v3 arena [V] | 4 (content) |
| Dungeon Maker | Mobile; offline; successor Dungeon Within (Apr 2026) [V] | $3.99 + IAP (cosmetic + gameplay) [V] | Rooms around a central core, path defense [V/U] | Room choice and placement, monster hiring and training, facilities [V] | Run + succession meta [V/U] | Small pixel sprites [U] | None [V] | 2 |
| Arknights | Mobile; live; Endfield spin-off 2026 [V] | F2P gacha, 50-pull soft pity [V] | Lane map, ground/high-ground tiles, facing [V/U] | Squad of operators, DP timing, block, redeploy [V] | Persistent collection; IS roguelike mode [V] | Anime illustrations + skeletal chibis [U] | None (PvE) [U] | 4 (content); core 2-3 |
| Super Auto Pets | PC + mobile; live [V] | F2P + packs + Plus sub [C] | 5-slot line, order = position [U] | Roll/freeze, merge, food, triggers [V/U] | Run only + pack unlocks [C] | Flat icons, tweens [U] | Async ghosts + AI fallback; ranked [V] | 2 (+ backend) |
| Backpack Battles | PC + mobile (Feb 2026); 1.0 Jun 2025 [V] | Premium [V] | Inventory grid, adjacency stars/diamonds [V] | Shop (sale/lock), recipes by adjacency, classes [V] | Run only + rank [I] | 2D drawn icons [U] | Async builds; ranked [V/C] | 2-3 (+ backend) |
| The Bazaar | PC (Steam Aug 2025) [V] | F2P + pass + paid heroes [V] | Item board [U] | Item and encounter choices [U] | Run + hero unlocks [V] | Not researched | Async ghosts [V] | 3 (+ backend) |

### Gaps
- KGC itself is outside this file's scope (covered by another researcher), so direct KGC comparisons are inferential.
- No revenue figures gathered for any title.
- Not covered: Mechabellum, Hero Wars, AFK Arena/AFK Journey (formation and idle design).
- Many art, animation and UI matrix fields are [U] because art-pipeline interviews were not found and the search budget ran out. A follow-up pass (with Riot, Wikipedia and Naavik domains allowed and more search budget) should verify the [U] items, especially board dimensions, shop odds, Arknights' animation tech, Guardian Tales' sprite pipeline, Despot's price and PvP mode, and the Backpack Battles run structure.
