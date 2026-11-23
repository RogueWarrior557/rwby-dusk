# Concept proposal: three directions, one recommendation

**Status:** awaiting approval. No game code will be written until the
decisions in §9 are made.
**Inputs:** the synthesized research report
(`docs/reports/Pixel tactics RPG design research.md`), the raw notes in
`docs/research_notes/`, and two first-hand feasibility tests in
`docs/research/art_spike/`.
**Evidence key:** **[R]** is a research finding (see the report for
sources and confidence). **[T]** is something we tested ourselves in this
repo. **[D]** is a design judgement. Design judgements are opinions argued
from evidence, not facts.

---

## 1. What the research tells us to build

### 1.1 What makes King God Castle engaging (and what it gets wrong)
King God Castle (AWESOMEPIECE, iOS/Android, October 2020, still updated in
November 2026 with Season 75 and a 2026 story mode) is a portrait
"merge + tower-defence + auto-chess" hybrid **[R]**. As far as the
snippet-level evidence shows, its appeal rests on six things:

| Strength | Why it works | Evidence |
|---|---|---|
| **Merge-and-place decisions every round.** Silver buys random summons from a 6-hero deck; duplicates merge up to 7★; you pay to expand the formation | A small, legible decision each round that compounds into a build | [R] |
| **A paced run arc.** 20 rounds with elite beats at 5, 10 and 15 and a boss at 20 | A clear rhythm of tension and release in a short session | [R] |
| **Risk/reward bargains.** "Devil's offers" trade castle durability for power | Agency, and a memorable story for each run | [R] |
| **A signature defensive rule.** "Absolute Defense" charges negate hits; multi-hit attacks, stuns and certain bosses counter it | Gives targeting and hero choice counterplay | [R] |
| **Build-around relics and permanent altars** | Extreme builds (solo carry vs. many copies) create variety | [R] |
| **Character collection** | Long-term attachment | [R], player reviews |

What players criticise, recurring across reviews and press snippets **[R]**:
randomness in summons; stamina and energy gates; grind gates on permanent
power (level 25–30 cubes); gear gacha ("Noble Phantasms") described as the
most pay-to-win element; power creep from new heroes; trust-breaking
reworks (relics in March 2023, heroes in August 2024); a dominant
"late team" strategy that lasted until its removal in December 2025; and
story added only years after launch. We found **no player-cast skill**:
combat appears fully automatic **[R, unverified detail]**.

**Takeaway [D]:** keep the merge-and-place round loop, the paced run arc
and the risk/reward bargains. Fix the RNG, the opacity, the grind and the
monetization. Give the player a few deliberate decisions *during* combat.
Make story a founding pillar, not a late addition.

### 1.2 The principles worth importing from other games
Ranked by how much each would deepen a King God Castle-like foundation
without bloating it **[R + D]**:

1. **Telegraph everything that matters** (Into the Breach, Wildfrost).
   Show enemy intents and timers during prep so the placement phase *is*
   the player's turn. Into the Breach's rule was "sacrifice cool ideas
   for the sake of clarity every time."
2. **Position should change what a unit can do,** not just who it hits
   (Darkest Dungeon's ranks, Arknights' blocking and deployment cost,
   Backpack Battles' adjacency).
3. **Agency over randomness** (TFT and Super Auto Pets shop freeze, lock
   and roll; Slay the Spire draft-or-skip). Randomness belongs in
   *offers*, not in hidden combat dice.
4. **Story advances when you fail** (Hades). Repetition becomes the
   delivery vehicle for narrative, not an interruption to it.
5. **Bonds earned by fighting together** (Fire Emblem supports). Write
   them only for curated pairs, because Engage's roughly 650 support
   conversations were widely called shallow.
6. **Adjacency-driven board building** (Loop Hero, Backpack Battles).
7. **Data-driven balance from the first playtest** (Slay the Spire:
   cards should be "reasonably viable, not equally powerful").
8. **Short runs and fair pricing** (Wildfrost and Backpack Battles sell a
   one-time unlock on mobile; Soul Knight keeps ads optional).

Pitfalls repeated across the corpus: hidden RNG undermining automated
combat; slow meta grind; infinite on-hit trigger chains; random
relationship progress; steep early difficulty on mobile; walls of story
text.

### 1.3 Constraints we verified ourselves [T]
* Code-authored pixel art can reach a credible standard at 32×32, but
  only with mandatory rendered-preview review passes
  (`docs/research/art_spike/`).
* A 7-column board of 32 px tiles fits a 270 px-wide portrait canvas at
  4× integer scale, with 14+ units legible.
* Light/dark board states read clearly using precomputed palette variants
  and dithered falloff, with no blending (`art_spike/light_test/`).
* This container can fetch npm, PyPI and Godot's official release asset.
  It cannot fetch the Android SDK repository, and it cannot build iOS.

---

## 2. Design pillars (shared by all three concepts)
1. **Every placement is a sentence.** Where a hero stands changes what
   they can do. Raw stats must never outweigh positioning.
2. **Fair and readable.** No hidden dice in combat. Enemy intent is
   telegraphed. Randomness lives in offers the player can steer.
3. **Story is a pillar, not a garnish.** The world exists beyond the
   screen. Story is woven into progression and fully skippable without
   losing rewards.
4. **A recognisable look.** One strong visual rule that doubles as a
   gameplay rule.
5. **Respect the player.** No stamina, no gacha, no pay-to-win.

---

## 3. Three original concepts

### Concept A — HUSHLIGHT *(working title)*
> *Every light burns a memory.*

| Field | |
|---|---|
| **Genre** | Portrait tactical autobattler and defence RPG, with a story campaign and a roguelite expedition mode |
| **Premise** | The sun is failing. The only light that holds back the dark is made by burning memories. You command a Lamplighter's company defending the last lit roads, and every lantern you raise costs someone something. |
| **Setting** | The Lantern Reach: a continent under a dimming sun called the Vigil. Lake-cities of a thousand lamps, memory distilleries, a cathedral that harvests the memories of the dead, and frontiers already swallowed by the Hush. |
| **Core loop** | **Dusk** (prep): read the telegraphed Night Chart, draft heroes from a 3-card offer drawn from your Company, merge duplicates, place heroes *and lanterns*. **Night** (auto combat in waves): heroes fight on their own while you spend Resolve on 2–3 Lantern Rites. **Dawn**: rewards, bargains and keepsakes. Between battles, campfire conversations, upgrades and the next node. |
| **Combat identity** | **Light is terrain you build.** Lantern pools change the rules of every tile they touch. |
| **Signature mechanic** | **The Light Board.** Lanterns cast tile-based light, which burns down over a Night. Heroes need light to build mana. Enemies in darkness are *veiled*: only adjacent attackers can hit them, and they render as silhouettes. Shadow-affinity heroes invert the rule. Some enemies hunt lanterns or snuff them. |
| **Narrative premise** | A Lamplighter who has burned away half her own past learns that burning memory is what is killing the sun. |
| **Progression** | In-run hero ranks through merges. Permanent **Recollections**: story-unlocked skill evolutions with a choice of two at each. **Kindred bonds** between curated pairs. **Hearth** hub facilities. **Keepsakes** (relics) in the Expedition. No gacha. |
| **Art direction** | Cold, low-value darkness against warm lantern pools. 32 px chibi-stylised units. Veiled enemies are silhouettes with ember eyes. A brass-and-vellum UI. **[T]** tested in `light_test/`. |
| **Replayability** | The Expedition: branching map, recruiting from scratch, Flames (lantern modifiers), Keepsakes and bargains. A Deep Night difficulty ladder, daily seeded runs, and Trials. |
| **Differentiators** | Light as a buildable, decaying terrain layer; a visual identity that *is* the gameplay rule; story and progression bound by one theme (memory). |
| **Complexity** | **Medium–high.** Tile light is cheap to compute and render. The heaviest load is writing and content. |

### Concept B — CROWN OF OATHS *(working title)*
> *Every vow is a weapon. Every betrayal is a wound.*

| Field | |
|---|---|
| **Genre** | Portrait tactical autobattler with a branching political campaign |
| **Premise** | A dead king's oath-magic bound every knight in the realm to their lord. When he dies, the oaths shatter. As a regent in hiding, you gather sworn champions and decide who wears the crown. |
| **Setting** | Seven duchies where spoken vows are literal magic: oaths empower, and breaking one curses. |
| **Core loop** | Campaign turn (choose which duchy to support, resolve court events) → battle (place champions) → aftermath (oaths strengthen or strain, faction influence shifts) → court hub. |
| **Combat identity** | **Relationships are geometry.** |
| **Signature mechanic** | **Oath tethers.** Sworn pairs within range form visible tethers that grant shared techniques, damage-sharing and vengeance triggers. Campaign decisions forge and break oaths, so betrayal literally removes synergies and recruits. |
| **Narrative premise** | A succession war fought through promises. Every ally is someone whose oath you hold, or who holds yours. |
| **Progression** | Oath ranks, champion ascension, court upgrades, faction reputation. |
| **Art direction** | Heraldic palettes for each house (palette-swapped tabards). Banners. A parchment war-table UI. |
| **Replayability** | A branching campaign with three endings, and a "Pretender's Gambit" roguelite where oaths form randomly. |
| **Differentiators** | A roster that changes with political choices; pair-based positioning. |
| **Complexity** | **High.** Branching content multiplies writing, and pairwise synergies multiply balance work. |

### Concept C — EBBWATCH *(working title)*
> *The sea keeps time. You keep the line.*

| Field | |
|---|---|
| **Genre** | Portrait tactical autobattler with scheduled battlefield mutation (puzzle-leaning) |
| **Premise** | A city built on a tidal causeway between two seas. Its tides are governed by a failing moon-clock. Tide-wardens hold the line during the Ebb, when things crawl out of the exposed trenches. |
| **Setting** | A stilt-and-lock archipelago city with drowned districts. |
| **Core loop** | Prep: read the Tide Chart (which rows flood, and when). Battle: scheduled tide shifts mid-fight displace units and change paths. Then rewards, and repairs to the city's locks in the hub. |
| **Combat identity** | **Time is terrain.** Fully predictable, scheduled board changes, in the spirit of Into the Breach. |
| **Signature mechanic** | **The Tide Chart.** Scheduled flooding, currents that push units, land and sea affinities, and one lock gate the player can toggle each wave. |
| **Narrative premise** | Rebuild the moon-clock by binding the sea-spirit again, let the sea reclaim the city, or move the city. |
| **Progression** | Lock engineering, tide-forged weapons that transform with exposure, relics. |
| **Art direction** | Animated water tiles, wet and dry palettes, reflections. |
| **Replayability** | Handcrafted tide puzzles, and procedural tide schedules in the expedition mode. |
| **Differentiators** | The strongest tactical predictability of the three. |
| **Complexity** | **High.** Animated water, pathing changes and level-design load. |

### 3.1 Scoring [D]
Each criterion is scored 1–10 and weighted equally. The scores are
judgements, but each is argued from the evidence above.

| Criterion | A · Hushlight | B · Crown of Oaths | C · Ebbwatch |
|---|---|---|---|
| Originality | **8.** Buildable, decaying light terrain is uncommon in autobattlers. Memory-as-fuel is fresh. | **6.** Bond systems exist (Fire Emblem). Political branching exists (Triangle Strategy). | **7.** Scheduled terrain is known from tactics games, rare in autobattlers. |
| Tactical depth | **8.** Light interacts with every role, enemy type and relic, plus active Rites. | **7.** Pair geometry is deep, but it narrows into "keep pairs together". | **9.** Strongest puzzle depth. |
| Narrative potential | **9.** The core mechanic *is* the theme. Moral cost is built in. | **9.** Political drama and betrayal. | **6.** The setting is strong; the mechanics carry little theme. |
| Visual appeal | **9.** Light pools on dark boards are striking and tested **[T]**. | **6.** Heraldry is pleasant but common. | **7.** Water is beautiful but expensive to do well. |
| Technical feasibility | **7.** Tile light is cheap. Precomputed palettes are proven **[T]**. | **5.** Branching content and N² balance. | **5.** Water animation, dynamic pathing, handcrafted puzzles. |
| Replayability | **8.** Light, roles, Flames and Keepsakes multiply cleanly. | **7.** Endings drive replay; runs are less varied. | **7.** Puzzles are finite; procedural tides risk unfairness. |
| **Total** | **49 / 60** | **40 / 60** | **41 / 60** |

---

## 4. Recommendation: **Hushlight**

**Why:**
1. **One idea does triple duty.** Light is the tactical layer, the visual
   identity and the story's moral question. Every system reinforces the
   others instead of competing for attention. That is the coherence the
   research says separates deep games from feature piles **[R + D]**.
2. **It fixes King God Castle's weaknesses structurally, not
   cosmetically.**
   * Positioning matters because light changes what heroes and enemies can
     do.
   * Telegraphed waves and deterministic combat replace hidden dice.
   * Lantern Rites add a few in-combat decisions without micro.
   * There is no gacha or stamina to monetize around.
3. **It is the most feasible ambitious option.** Light is tile-based,
   both in rules and in rendering, with precomputed palettes. We have
   already rendered it **[T]**.
4. **It has the best narrative ceiling.** A world that literally runs on
   burning its past supports serious themes: exploitation, grief,
   identity, what we owe the dead. It does so without lore that exists
   only to explain mechanics.

**What it absorbs from the runners-up (and what it refuses):**
* From **Crown of Oaths**, it takes *curated* Kindred bonds: two or
  three per hero, earned by fighting adjacent in light and through
  campfire scenes. It does **not** take politics that rewrite the
  roster. That causes a content explosion and is deferred indefinitely.
* From **Ebbwatch**, it takes the **Night Chart**: a scheduled, visible
  timeline of waves, Hush-tides (darkness pulses) and boss attacks. It
  does **not** take animated water or path mutation.

**Its biggest risks, and the plan for each:**
* **Darkness could become a pure penalty.** Shadow-affinity heroes,
  enemies that are weaker in dark, and bargains that *spend* light make
  darkness a resource as well.
* **Mobile readability of light levels.** Each state is encoded three
  ways (value, temperature and dither pattern) plus silhouettes. There
  will be a colour-blind check.
* **Writing load.** Scope Act I only for launch. Use curated bonds, not
  pairwise ones.

---

## 5. Hushlight — world and narrative premise

### 5.1 Cosmology
In the oldest liturgies, before anything was, there was **the Hush**: not
darkness but *unmemory*, a silence in which nothing had ever happened.
Out of it rose **the Witness**, and the Witness *remembered*. The world
became real because it was remembered. The great memory that held it in
place burned in the sky as **the Vigil**.

Everything that is remembered carries a faint inner light, **lumen**.
Things no one remembers lose it and slide back into the Hush. A road no
one walks, a song no one sings, a person no one mourns all thin out,
becoming grey, then translucent, then gone.

### 5.2 History (Reckoning of the Dimming, "R.D.")
* **The Age of Noon** (myth). The Vigil never set. The Ember-folk still
  sing it.
* **0 R.D.: the Dimming.** The Vigil faltered. The first night that did
  not end, the Long Night of Orra, lasted forty days. Whole cities did not
  fall; they were *forgotten*. Bell-city Myrr is on no map now. Nobody
  knows why it happened. The Church says sin; the scholars of the Glass
  Wastes say entropy; the Ember-folk say grief.
* **22 R.D.: the Discovery.** The alchemist-anchoress **Idony Vash**
  learns to draw memories out of a living mind and distil them into
  **recall**, an oil that burns with *true light*. The Hush cannot cross
  true light. Idony saves the Reach and is canonised as Saint Idony of the
  Wick.
* **41 R.D.: the Order of Lamplighters.** Founded by Idony's apprentices
  on one principle: *burn only what is yours.* A Lamplighter carries an
  **Old Lantern** bound to the bearer, which can burn only the bearer's
  own memories. They keep the light-roads between cities open.
* **150–163 R.D.: the Tallow Wars.** The Lantern Houses (merchant
  dynasties) fight over the distilleries. The **Chandlers' Compact** ends
  the war by giving the Houses a monopoly on recall and the Church the
  **Last Rite**: a tithe of the memories of the dead.
* **312 R.D.: the present.** Day is a single grey hour. Harvests fail.
  In Candlemere's lower wards the poor sell memories to House brokers at
  the going rate: a childhood summer buys a week of lamplight. The
  Lamplighters are underfunded, mistrusted and few. Something in the
  Vigil is accelerating.

### 5.3 The rules of light (the magic system)
1. **True light comes only from recall or from Vigilglass,** the crystal
   where the Vigil's light fell in the Glass Wastes. Ordinary fire
   frightens the weakest Unremembered and stops nothing.
2. **A burned memory is gone from the one who held it,** permanently.
3. **An Old Lantern burns only its bearer.** The bearer chooses which
   memory feeds the wick.
4. **The Telling.** Ember-folk practice: a memory spoken aloud kindles a
   faint lumen in those who listen. It cannot fight the Hush. Nobody has
   ever measured whether it does anything at all.
5. **The secret** (revealed in Act II, foreshadowed from Chapter 1):
   burning a memory does not only empty a mind. It severs the remembered
   thing's hold on the world. Distillery towns lose their history, and
   then their streets. **Recall is feeding the Hush.** The Dimming came
   first, but the cure has been accelerating the disease for three
   centuries, and the Church has known since it suppressed Saint Idony's
   final testament.

### 5.4 Nations and factions
| Faction / place | What they want | Why they are believable |
|---|---|---|
| **The Order of Lamplighters** | Keep the light-roads open, at personal cost | An honourable institution in decline; its ethic of self-burning has hollowed out its own members |
| **The Lantern Houses** (seat: **Candlemere**, the lake-city of a thousand lamps) | Profit and stability | They genuinely keep the cities lit. The market prices a poor child's memories below a rich man's candle. |
| **The Church of the Witness** (seat: **Aurel**, the mountain sanctum) | Rekindle the Vigil through faith and sacrifice | Sincere believers running the harvest of the dead; their theology needs the sun to be savable |
| **The Quiet** | Put out the great lanterns and let the world forget | Former memory-sellers, the grieving, the exploited. They believe forgetting is mercy, and the Unremembered *have been spared* by them. |
| **The Ember-folk** (the Ashen Marches) | Keep their oral tradition and their freedom | They refused recall for three centuries and paid in blood. They know the Telling. |
| **The Glass Wastes scholars** | Understand the Vigil | Their science is real and their ambition is dangerous |
| **Myrr, the Unremembered City** | Unknown | It still exists, inside the Hush. Endgame. |

### 5.5 Central conflict
The Vigil will go out within a generation, and three answers are at war:
* **The Great Kindling** (the Church). Burn the memories of an entire
  city's poor wards at Aurel's Sun-Altar to buy a century of daylight.
* **The Silence** (the Quiet). Extinguish the Sun-Altar and Candlemere's
  Lighthouse Spire and let the world rest.
* **The Market** (the Houses). Fund both sides and sell light to whoever
  survives.

The protagonist's road leads to a fourth, unproven answer: **remember
instead of burn**. Restore the Unremembered by giving them back their
names. It may be too slow, too costly in grief, or simply false. The
player decides how far to trust it.

### 5.6 The protagonist
**Maren Vey**, 24, Lamplighter of the Greywater Road.
* **Wants:** to keep her road lit and to earn back the Order's faith in
  her mentor's lantern, which she carries.
* **Fears:** running out of herself, becoming "a lantern with no one
  inside".
* **Contradiction:** she preaches burning only what is yours, and she has
  burned nearly everything she loved, including (unknown to her) her
  younger brother **Tobin**. She burned the last memory of him to survive
  a night six years ago. He has been walking with the Unremembered ever
  since.
* **Agency:** at five signposted moments in the campaign, the player
  chooses **which of Maren's memories to burn**: her mother's voice, the
  first song she learned, the night she nearly quit the Order, and so on.
  Each choice permanently removes a scene thread, changes how Maren
  speaks, and is reflected in the epilogue. The story is literally
  consumed by the player's decisions.
* **On the board,** Maren is the Hearth lantern. Her presence is the light
  you defend, and her Rites are the player's active powers.

### 5.7 Supporting cast (launch-roster candidates)
| Hero | Role / light affinity | Core of the character | Combat identity reflects… |
|---|---|---|---|
| **Bram Ostrow** | Vanguard · Lightsworn | A former distillery guard who *cannot forget* (perfect memory). His mind is worth a fortune, so the Houses hunt him. Gentle, slow to anger, carrying every grief he has ever had. | *Weight of Years:* the longer he holds a tile, the harder he is to move or wound |
| **Sefa of the Ninth Fire** | Marksman · Edgewalker | An Ember-folk exile who scorns lanterns. Exiled for selling her clan's Telling to a House to save her sister. | Fire arrows *briefly reveal* veiled enemies; strongest standing in dim light |
| **Brother Tamsin Reed** | Warden (healer) · Lightsworn | A Church confessor who "takes your worst memory so you can sleep". Secretly he never burns them: he keeps them, and he is full of other people's pain. | Mends wounds by carrying them, with heals that convert damage into his own shield |
| **Noemi "Nox" Castell** | Duskborn (assassin) | A memory thief who sold her own childhood. She is Magnate Tallis's daughter and doesn't know it. | Stealth in darkness; executes veiled enemies |
| **Isolde Grey** | Arcanist · Lightsworn | A Glass Wastes scholar with a Vigilglass lens. Warm, brilliant, ambitious. A Church informant for the Kindling, which she believes is science's only answer. Her betrayal ends Act I. | Focused light beams that strengthen in bright tiles |
| **Pellam "Old Pell" Fosse** | Tinker (summoner) · Lightsworn | A grumpy lamp-maker who keeps his late wife's memory unburned in a locket and will not burn it even to save himself | Builds *Wicklings*, walking clockwork lanterns that are **mobile light sources** |
| **The Nameless Knight** | Blade (melee) · Duskborn | An Unremembered who regained a fragment of a name through Maren's Telling. Proof that the enemy are people. | Fights at full strength in darkness, fading in bright light |
| **Hester Quill** | Archivist (support/control) · Edgewalker | A disgraced House ledger-keeper who knows whose memories were bought, and for how little | Marks enemies; marked enemies stay revealed |

The full **24-hero roster plan** across 7 roles × 3 light affinities is a
post-approval deliverable (Phase 7). This table shows the design space.

### 5.8 Antagonists
* **Ansel Marrow, the Unlit Shepherd.** Leader of the Quiet, and Maren's
  mentor and predecessor as bearer of her lantern. He burned nearly all of
  himself in service and found, in the emptiness, peace. He is not cruel:
  he has seen what light costs and who pays it. His question to Maren
  drives Act II: *"What did your light ever cost you? You burned it so you
  wouldn't have to carry it."*
* **High Witness Aurelie Sancroft.** Architect of the Great Kindling. She
  has never burned a memory, and she is terrified of the dark, which took
  her parish when she was nine. A utilitarian whose arithmetic is
  sincere, and therefore monstrous.
* **Magnate Corvin Tallis.** He funds both sides. He loves the daughter
  who sold every memory of him to escape him, and he will burn the world to
  be recognised by her once.
* **The Boy Without a Name.** Tobin, Unremembered. A narrative boss who
  calls Maren "sister" from the dark in Chapter 1's final frame, long
  before she understands why.

### 5.9 Themes and structure
**Themes:** memory and identity; the cost of keeping going; grief versus
forgetting; a world that literally burns its poor's past to light its
rich; what the living owe the dead.

**Structure:** Prologue plus three acts. **Act I, "The Greywater Road"**
(4 chapters), is the launch campaign. Act II, "Candlemere", and Act III,
"Myrr", are planned expansions.

**Chapter 1 sketch (the vertical-slice story), "The Lamp at Greywater":**
A Hush-tide is coming to Greywater, a ferry town that sold its own
history for light a generation ago. Maren defends it. She shelters Bram
from House hunters, clashes with Sefa, and receives Tamsin and a Church
writ ordering Greywater's recall stores seized. The boss is **the
Ferryman**: the town's forgotten founder, made Unremembered by the very
light that saved his town. At the end, the player chooses whether to
**burn one of Maren's memories** to relight the town beacon, or to
evacuate and let Greywater go dark. Both choices carry consequences into
Chapter 2. The final frame: a small figure at the edge of the light,
faceless, saying *"Sister."*

### 5.10 Story delivery (research-led)
* **Campfire Vigils between Nights:** 1–3 minute portrait conversations
  at the lantern. They are the source of bonds and Recollections, and the
  story as reward for playing, including after defeats (Hades) **[R]**.
* **Skip without loss:** every scene has Skip, a one-line summary, a log
  and full reward credit (the Honkai: Star Rail 3.4 pattern) **[R]**.
  Combat-focused players lose nothing mechanically.
* **Recollections:** character missions that unlock skill evolutions
  (Arknights ties backstory to trust levels) **[R]**.
* **The Archive:** codex, letters and broadsheets. Burned documents
  appear with visibly missing passages.
* **Narrative bosses:** barks before and during battle; the Ferryman and
  the Boy Without a Name.
* **Environmental storytelling:** memory-sale posters, distillery
  chimneys, and empty plinths where statues were forgotten.
* **Tooling:** Ink (MIT) or Yarn Spinner. The licence differs for Godot,
  so legal review is needed **[R]**. Choice deferred to implementation.

---

## 6. Hushlight — combat foundation

### 6.1 Board and orientation
* **Portrait**, to match the genre's familiar one-handed play, and the
  vertical theme of darkness descending toward your light **[R]**.
* **Board: 7 columns × 9 rows of 32 px tiles** on a 270 px-wide logical
  canvas, integer-scaled **[T]**.
  * Rows 0–3 are the **Verge**, where enemies emerge from the dark.
  * Rows 4–8 are the **Watch**, the deploy zone.
  * **Maren's Hearth lantern** stands at the bottom centre. Enemies that
    reach it drain the Hearth's light (run health).
* The **squad cap** starts at 4 heroes and grows to 8 by spending Embers.
  This echoes King God Castle's formation expansion as a tempo decision.

### 6.2 The round (a "Night" is 6–10 waves; about 8–12 minutes)
1. **Dusk** (untimed prep):
   * The **Night Chart** shows the next two waves completely: enemy types,
     spawn columns and intents. It also marks scheduled Hush-tides and
     boss attacks.
   * Spend **Embers** to recruit from a 3-card offer drawn from your
     6-hero **Company**, or to reroll (rising cost), lock an offer, or
     expand the squad cap.
   * **Two copies at the same rank merge into the next rank** (Ranks
     I–IV). Rank III upgrades the hero's skill.
   * Place and move heroes and lanterns freely.
   * A bad-luck guard means no Company hero goes unoffered for more than
     2 rerolls.
2. **Night** (auto combat): heroes act on their own AI. Lanterns burn
   down. The player spends **Resolve**, earned when enemies die in light,
   on **Lantern Rites**:
   * *Flare:* every lantern +1 radius for 5 s.
   * *Beacon:* move one lantern instantly.
   * *Last Ember:* a huge burst of light, at a cost to the Hearth's
     light; once per Night.
3. **Dawn:** Embers are awarded for kills and for Hearth health. Every
   third wave offers a choice:
   * a **Keepsake** (relic), 1 of 3; or
   * a **Bargain of the Hush**: a risk/reward offer, for example "your
     lanterns burn 25% faster this Night; gain a rare Keepsake now".

### 6.3 Light rules (tile-level, deterministic)
* Each light source has a **radius** and **oil**. A tile's light value is
  `max over sources of (radius − distance)`. That gives four states:
  **Bright** (≥ 1.5), **Lit** (> 0), **Dim** (> −1) and **Dark**.
  Radius drops 0.5 at oil thresholds, which paces each Night.
* **Heroes:**
  * *Skills need light.* Heroes gain mana from attacks only in Lit or
    Bright tiles (+25% in Bright). In darkness they gain mana only from
    taking hits.
  * **Duskborn** heroes invert this: they gain mana in Dim and Dark, and
    gain Stealth in Dark.
  * **Edgewalkers** peak in Dim.
* **Enemies:** in Dark they are **Veiled**. Only attackers on adjacent
  tiles can target them. They render as silhouettes with eye glints
  **[T]**. In light they are **Revealed**.
* **Enemy archetypes built around light:**
  * *Moths* hunt lanterns.
  * *Snuffers* cut a lantern's radius on hit.
  * *Lightbane* take bonus damage in Bright.
  * *Hush-callers* trigger telegraphed darkness pulses.
  * Bosses telegraph phase attacks on the Night Chart.
* **Lanterns** are destructible objects. **Flames** (from Keepsakes and
  Hearth upgrades) alter them:
  * *Ember:* bright tiles burn enemies.
  * *Pale:* slow enemies.
  * *Verdant:* heal heroes.
  * *Azure:* wider reveal, no bonus.

**Decisions this creates [D]:**
* Light the backline casters, or push light forward so marksmen can see?
* Who stands at the edge of the light?
* Do you send a Duskborn into the dark to hunt veiled enemies?
* Guard the lantern from Moths, or let it fall and re-light?
* Spend Last Ember now, or save it for the boss's telegraphed phase?

### 6.4 Combat rules (data-driven; first-pass numbers will be tuned by simulation)
* **Stats:** HP, Power, Armor, Ward (magic resist), attack interval,
  range (tiles), move speed, mana, plus skill data.
* **Damage:** `dmg = base × multiplier × 100 / (100 + effective_defence)`,
  where `effective_defence = max(0, def × (1 − %pen) − flat_pen)`. There
  are diminishing returns and no immunity through stacking. Physical
  damage is reduced by Armor, Arcane by Ward, and True damage is rare and
  flagged.
* **No hidden dice:** critical hits come from visible **Momentum** pips
  (every Nth attack crits), not from a chance roll. Combat runs at a
  fixed **30 ticks per second** with integer or fixed-point maths. That
  makes it deterministic, replayable, and verifiable later by a server
  for async PvP.
* **Crowd control:** stun, root, silence and slow. After a CC ends the
  target gets **Steadfast** (1.5 s CC immunity). Bosses use a **Poise**
  bar instead.
* **Stacking:**
  * A same-name buff refreshes rather than stacking, unless it is
    explicitly stackable to N.
  * Bonuses add within a category and multiply across categories.
  * Hard caps: attack speed ≤ +150%, damage reduction ≤ 70%, shields
    decay over time.
* **Safety rules:**
  * Trigger depth is capped, so on-hit effects can't loop infinitely.
  * Each hero has a summon cap.
  * Healing-reduction counterplay exists.
* **Enemy scaling:** per-wave multiplier tables, elite affixes, and boss
  phases on the Night Chart.

### 6.5 Signature mechanics evaluated (requirement: ≥ 3)
| Candidate | Depth | Clarity | Replay | Balance risk | Visual feedback | Mobile UX | Feasibility | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Light Board** | High | High (three encodings) | High | Medium | Built in **[T]** | Drag, same as units | High | **Core** |
| **Night Chart** (telegraphs) | Medium | Very high | Medium | Low | Icon strip | Glanceable | High | **Core** |
| **Kindred Bonds** (curated pairs) | Medium | High | Medium | Low–medium | Tether glint | Passive | Medium (writing) | **Core** |
| **Recollections** (story-unlocked skill evolutions, choose 1 of 2) | Medium | High | Medium | Medium | Skill VFX variants | Hub menu | Medium | **Core** (progression) |
| **Lantern Rites** (2–3 player actives) | Medium | High | Low | Low | Big, clear | One tap | High | **Core** |
| Burn a Memory (story choices) | n/a | High | Medium (endings) | n/a | Scene-level | Menu | Medium | **Story layer** |
| Weather / terrain mutation | Medium | Medium | Medium | High | Costly | OK | Low | **Rejected:** overlaps light |
| Equipment transformation | Medium | Medium | Medium | Medium | Icons | Inventory UI | Medium | **Deferred** past launch |
| Faction influence on roster | High | Low | High | High | n/a | Menus | Low | **Rejected** (content explosion) |

---

## 7. Hushlight — progression, economy, modes

### 7.1 Progression (decisions over inflation)
* **Hero levels** (Lumen): modest stat growth, capped per chapter, so
  levels supply under 40% of power and tactics supply the rest.
* **Recollections:** 3 per hero, each a choice of two skill evolutions.
  Respec is free at the Hearth.
* **Kindred bonds:** ranks earned by fighting adjacent in light and
  through Vigil scenes. A pair passive applies when the pair is adjacent
  and lit.
* **Heirlooms:** one signature item per hero with upgrade branches, plus
  two **Trinket** slots crafted from fixed recipes. No random gear.
* **The Hearth** (hub): the Chandlery (Flames), the Archive (lore and
  replay), the Yard (Trials), the Map Room (Expedition) and the
  Infirmary. Upgraded with Lumen and story progress.

### 7.2 Economy and monetization
* **Two currencies:** **Embers** (run-only, reset every run) and
  **Lumen** (permanent, earned in every mode). Keepsakes and Trinkets are
  items, not currencies.
* **Heroes unlock through story and Expedition milestones,** so there are
  no duplicates to manage.
* **Business model:** free prologue and Chapter 1, then a **one-time
  unlock** (the Wildfrost and Backpack Battles precedent **[R]**), then
  paid story acts and direct-sale cosmetics (palette outfits, lantern
  skins). **No gacha, no stamina, no paid power, no forced ads.** This
  also keeps the game outside current and proposed loot-box regulation
  (Korea's 2024 disclosure law, the EU Digital Fairness Act proposal)
  **[R]**.

### 7.3 Modes and release roadmap
| Mode | Why it exists | When |
|---|---|---|
| **Story campaign** | Narrative spine; teaches mechanics chapter by chapter | Vertical slice: Chapter 1 · Launch: Act I |
| **Trials** | Fixed-squad puzzles that teach mastery (light geometry, Rites timing) | Slice: 1–2 · Launch: 20 |
| **Expedition** (roguelite) | Replayability: branching map, recruit from scratch, Flames, Keepsakes, Bargains, Deep Night ladder | Launch |
| **Character stories** | Recollections, the bond-driven narrative | Launch (for launch roster) |
| **Hearth** (hub) | Persistent home; unlocks systems diegetically | Slice: basic · Launch: full |
| **Long Night** (endless) | Score-chasing mastery; local leaderboard first | Post-launch |
| **Boss hunts** ("Named Unremembered") | Unique mechanics, cosmetic rewards | Post-launch |
| **Rival Lamplighters** (async PvP) | Uses deterministic combat for server-side verification; **only after** a backend and anti-cheat design exist | Post-launch, conditional |

---

## 8. Production plan

### 8.1 Art direction summary (a full style guide follows approval)
* **Canvas:** 270 px-wide portrait; height expands to the device
  (≈480–600); integer scale only (4× on 1080-wide phones). Fixed safe-core
  board with decorative margins **[R]**.
* **Units:** 32×32 canvas, characters ≈24–28 px tall at about 2.25 heads.
  1 px violet-black outline with selective outlining on lit edges. Each
  character uses at most 16 colours from the master palette. Every hero
  must pass a silhouette-only identification test.
* **Bosses:** 64×64 (up to 96×64). **Portraits:** 64×64 busts with three
  expressions. **Icons:** 16×16.
* **Palette:** one master palette of 48–64 colours. Hue-shifted ramps
  (≤ 20° per ramp **[R]**), shadows toward violet, lights toward amber.
  Four precomputed light levels; emissive pixels are exempt **[T]**.
* **Animation:**
  * idle 4 frames (180–240 ms);
  * walk 6 frames (≈100 ms);
  * attack 4–6 frames with a held anticipation frame, a smear frame and an
    80–120 ms impact hold;
  * cast 6–8 frames; hit 2 frames plus a flash; death 6–8 frames,
    dissolving into memory motes;
  * victory 4 frames **[R]**.
* **VFX:** palette ramps ending in white, 4–8 frames, no alpha fades
  (step down the ramp or dither dissolve), particles snapped to the pixel
  grid.
* **UI:** brass and vellum, 9-slice pixel panels. A bitmap font for
  numbers and labels. Long-form text in a high-legibility font rendered at
  native resolution (for localisation and accessibility).

### 8.2 Audio direction (honest scope)
* **SFX:** synthesised procedurally (jsfxr and ChipTone output are CC0
  **[R]**, plus our own code-based synthesis), layered for impacts.
  **We can produce these.**
* **Music:** leitmotif plan. The Lamplighters' five-note hope figure; the
  Hush as a descending, unresolved motif; music-box and bowed-synth
  timbres. **Music is our weakest capability.** We can produce simple
  synthesised stems in code. A composer or licensed score is recommended
  before commercial release. We will not claim finished music until real
  files exist.

### 8.3 Technical stack
* **Engine: Godot 4.7.x (stable), GDScript, Compatibility renderer.**
  * MIT licence; integer scaling (4.2+); 2D batching on all renderers
    since 4.4. The docs recommend Compatibility for 2D and low-end mobile
    **[R]**.
  * Headless CLI tests and exports; Slay the Spire 2 moved from Unity to
    Godot **[R]**.
  * Unity is impractical here: no headless Personal licence activation,
    and its download hosts are blocked **[R][T]**.
  * C# in Godot is still experimental on mobile and cannot export to web
    **[R]**, so we use GDScript.
* **Architecture:**
  * a deterministic combat core as plain GDScript classes (no scene
    nodes), driven by JSON data validated by Python tools;
  * presentation subscribes to combat events (frame events sync VFX and
    SFX to real hits);
  * saves are versioned JSON in `user://`, written to a temp file then
    renamed, with a backup copy.
* **Testing:**
  * GUT or gdUnit4 headless unit tests;
  * thousands of headless combat simulations for balance;
  * web export plus Playwright screenshots for visual QA.
* **Pipeline:** pixelforge (`.pxs` → PNG + JSON) → importer → Godot
  SpriteFrames. Lossless import, nearest filtering, no VRAM compression on
  pixel art **[R]**.
* **Builds:**
  * web: from this container;
  * Android: needs the Android SDK, from `dl.google.com` (blocked here),
    so it needs an environment change or a local/CI machine;
  * iOS: needs macOS and Xcode.
* **Fallback:** if Godot cannot run here, use a TypeScript + WebGL 2D
  renderer + Capacitor stack. It builds and tests fully in this container
  today **[T]**.

### 8.4 Roadmap and exit criteria
| Milestone | Scope | Exit criteria (measurable) |
|---|---|---|
| **M1: Foundation** | Godot project, pixel-perfect rendering settings, scene flow, input, data schemas, pixelforge importer, save system skeleton, CI test runner | Headless tests pass. A web export renders a test sprite pixel-exact at 3×, 4× and 5×. A save round-trips. |
| **M2: Playable combat** | Board, deployment drag, deterministic combat core, light rules, 3 heroes, 3 enemy types, waves, win/lose, Embers | Unit tests for damage, targeting, light states and cooldowns. 1,000 sims run with no exceptions. A full Night is playable in the browser. |
| **M3: Vertical slice** | Menu, 4–6 polished heroes with full animation sets, 4+ enemies, the Ferryman boss, Chapter 1 story with Vigils and the burn-a-memory choice, Hearth (basic), Recollections (first tier), VFX, SFX, save/load, settings | Chapter 1 completable start to finish. Visual QA checklist passed on rendered screenshots. Balance targets met in simulation. Bug log reviewed. |
| **M4: Systems expansion** | Kindred bonds, Keepsakes, Flames, Bargains, Expedition (1 region), Trials, more heroes | Expedition run completable. Win-rate spread across heroes within target band in sims. |
| **M5: Content** | Act I chapters 2–4, 12–14 heroes, 3 regions, character stories | Act I completable. Writing pass reviewed. |
| **M6: Optimisation and testing** | Profiling on real mid-range Android, frame pacing, battery modes, accessibility, localisation readiness | Measured, not claimed: 60 fps target on a named reference device, plus a 30 fps battery mode. |
| **M7: Release preparation** | Store builds, privacy, ratings, unlock purchase, analytics (opt-in) | Signed Android build; an iOS build on a macOS host. |

M1–M3 can be built and verified in this environment. M6–M7 need physical
devices and machines outside it.

---

## 9. Decisions requested
1. **Concept:** approve **Hushlight**, or choose B or C, or ask for a
   hybrid.
2. **Narrative premise:** approve the world of memory-fuelled light, Maren
   Vey as a defined protagonist (not a blank avatar), and the
   burn-a-memory choice structure.
3. **Combat direction:** approve the portrait 7×9 Light Board,
   deterministic no-dice combat, the telegraphed Night Chart, and 2–3
   player Rites.
4. **Business model:** approve premium unlock plus expansions plus
   cosmetics (no gacha or stamina), or ask for alternatives.
5. **Engine:** approve Godot 4.7 + GDScript, and **permit downloading and
   running the official Godot binary in this environment** so it can be
   verified headlessly here.
6. **Working title:** "Hushlight" is provisional and needs a trademark and
   store-name search before any public use.

---

## 10. What is verified, what is assumed, and the limits
* **Research limits:** most researchers could not open source pages
  (network policy) and worked from search-result snippets. The shared
  search budget ran out mid-research. King God Castle's grid size, exact
  formulas, sprite sizes and UI layout are **unverified**. See the
  report's limitations section.
* **Assumed, not verified:** player-retention effects of any mechanic;
  the market performance of premium mobile games in this genre; the
  readability of light levels for colour-blind players (to be tested in
  M2); Godot's mobile in-app purchase and cloud-save maturity (a spike
  planned in M1).
* **Verified first-hand [T]:** 32 px code-authored sprites, board fit,
  lighting readability, and container tooling and network facts.
