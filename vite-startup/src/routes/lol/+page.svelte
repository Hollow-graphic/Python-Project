<script lang="ts">
    import { onMount } from 'svelte';
    import Item from './Item.svelte';
    import Champion from './Champion.svelte';
    import json from './item_en_us.json';
    import builds_json from './build.json';
    let interval;
    const item_id_list = [
        1001, 1004, 1006, 1011, 1018, 1026, 1027, 1028, 1029, 1031, 1033, 1035, 1036, 1037, 1038, 1039, 1040, 1042, 1043, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1082, 1083, 1086, 1090, 1091, 1092, 1093, 1094, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1111, 1120, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1220, 1221, 1222, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 2001, 2002, 2003, 2007, 2008, 2010, 2015, 2019, 2020, 2021, 2022, 2031, 2033, 2049, 2050, 2051, 2052, 2055, 2056, 2065, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2150, 2151, 2152, 2161, 2162, 2163, 2403, 2420, 2421, 2422, 2501, 2502, 2503, 2504, 2508, 2510, 2512, 2517, 2520, 2522, 2523, 2524, 2525, 2526, 2530, 3001, 3002, 3003, 3004, 3005, 3006, 3008, 3009, 3010, 3011, 3012, 3013, 3020, 3023, 3024, 3026, 3031, 3032, 3033, 3035, 3036, 3039, 3040, 3041, 3042, 3044, 3046, 3047, 3050, 3051, 3053, 3057, 3065, 3066, 3067, 3068, 3070, 3071, 3072, 3073, 3074, 3075, 3076, 3077, 3078, 3082, 3083, 3084, 3085, 3086, 3087, 3089, 3091, 3094, 3095, 3100, 3102, 3105, 3107, 3108, 3109, 3110, 3111, 3112, 3113, 3114, 3115, 3116, 3117, 3118, 3119, 3121, 3123, 3124, 3128, 3131, 3133, 3134, 3135, 3137, 3139, 3140, 3142, 3143, 3144, 3145, 3146, 3147, 3152, 3153, 3155, 3156, 3157, 3158, 3161, 3165, 3168, 3170, 3171, 3172, 3173, 3174, 3175, 3176, 3177, 3179, 3181, 3184, 3190, 3193, 3211, 3222, 3302, 3330, 3340, 3348, 3349, 3363, 3364, 3398, 3399, 3400, 3430, 3504, 3508, 3513, 3599, 3600, 3742, 3748, 3801, 3802, 3803, 3814, 3850, 3851, 3853, 3854, 3855, 3857, 3858, 3859, 3860, 3862, 3863, 3864, 3865, 3866, 3867, 3869, 3870, 3871, 3876, 3877, 3901, 3902, 3903, 3916, 4003, 4004, 4005, 4010, 4011, 4012, 4013, 4014, 4015, 4016, 4017, 4401, 4402, 4403, 4628, 4629, 4630, 4632, 4633, 4635, 4636, 4637, 4638, 4641, 4642, 4643, 4644, 4645, 4646, 6029, 6032, 6035, 6333, 6609, 6610, 6616, 6617, 6620, 6621, 6630, 6631, 6632, 6653, 6655, 6656, 6657, 6660, 6662, 6664, 6665, 6667, 6670, 6671, 6672, 6673, 6675, 6676, 6677, 6690, 6691, 6692, 6693, 6694, 6695, 6696, 6697, 6698, 6699, 6700, 6701, 6702, 7050, 8001, 8010, 8020, 9168, 9171, 9172, 9173, 9174, 9175, 9176, 9177, 9178, 9179, 9180, 9181, 9183, 9184, 9185, 9187, 9188, 9189, 9190, 9192, 9193, 9271, 9272, 9273, 9274, 9275, 9276, 9277, 9278, 9279, 9280, 9281, 9283, 9284, 9285, 9287, 9288, 9289, 9290, 9292, 9293, 9300, 9301, 9302, 9303, 9304, 9305, 9306, 9307, 9308, 9400, 9401, 9402, 9403, 9404, 9405, 9406, 9407, 9408, 123430, 124011, 126697, 220000, 220001, 220002, 220003, 220004, 220005, 220006, 220007, 220008, 220009, 220010, 220011, 220012, 220013, 221011, 221026, 221031, 221038, 221043, 221053, 221057, 221058, 222022, 222051, 222065, 222141, 222502, 222503, 222504, 222510, 222512, 222517, 222522, 222523, 222524, 222525, 222526, 222530, 223001, 223002, 223003, 223004, 223005, 223006, 223008, 223009, 223011, 223020, 223026, 223031, 223032, 223033, 223036, 223039, 223040, 223042, 223046, 223047, 223050, 223053, 223057, 223065, 223067, 223068, 223069, 223071, 223072, 223073, 223074, 223075, 223078, 223084, 223085, 223087, 223089, 223091, 223094, 223095, 223100, 223102, 223105, 223107, 223109, 223110, 223111, 223112, 223115, 223116, 223118, 223119, 223121, 223124, 223135, 223137, 223139, 223142, 223143, 223146, 223152, 223153, 223156, 223157, 223158, 223161, 223165, 223172, 223177, 223181, 223184, 223185, 223190, 223193, 223222, 223302, 223504, 223508, 223742, 223748, 223814, 224004, 224005, 224401, 224403, 224628, 224629, 224633, 224636, 224637, 224644, 224645, 224646, 226035, 226333, 226609, 226610, 226616, 226617, 226620, 226621, 226630, 226631, 226632, 226653, 226655, 226656, 226657, 226660, 226662, 226664, 226665, 226667, 226668, 226671, 226672, 226673, 226675, 226676, 226691, 226692, 226693, 226694, 226695, 226696, 226697, 226698, 226699, 226701, 228001, 228002, 228003, 228004, 228005, 228006, 228008, 228009, 228020, 322065, 322526, 322530, 323002, 323003, 323004, 323040, 323042, 323050, 323070, 323075, 323107, 323109, 323110, 323119, 323121, 323190, 323222, 323504, 324005, 326616, 326617, 326620, 326621, 326657, 328020, 443054, 443055, 443056, 443058, 443059, 443060, 443061, 443062, 443063, 443064, 443069, 443079, 443080, 443081, 443083, 443090, 443193, 444636, 444637, 444644, 446632, 446656, 446667, 446671, 446691, 446693, 447100, 447101, 447102, 447103, 447104, 447105, 447106, 447107, 447108, 447109, 447110, 447111, 447112, 447113, 447114, 447115, 447116, 447118, 447119, 447120, 447121, 447122, 447123, 550001, 550002, 550003, 550004, 550005, 550006, 550007, 663039, 663056, 663058, 663059, 663060, 663064, 663146, 663172, 663193, 664011, 664403, 664644, 667101, 667109, 667112, 667666, 771001, 771004, 771006, 771011, 771018, 771026, 771027, 771028, 771029, 771031, 771033, 771036, 771037, 771038, 771039, 771042, 771043, 771051, 771052, 771053, 771054, 771055, 771056, 771057, 771058, 771080, 771500, 772001, 772003, 772004, 772009, 772037, 772038, 772039, 772041, 772042, 772043, 772044, 772045, 772049, 772050, 772139, 772140, 773001, 773003, 773004, 773005, 773006, 773009, 773010, 773020, 773022, 773023, 773024, 773025, 773026, 773027, 773028, 773031, 773035, 773037, 773040, 773041, 773042, 773044, 773046, 773047, 773050, 773052, 773056, 773057, 773060, 773063, 773064, 773065, 773067, 773068, 773069, 773070, 773071, 773072, 773073, 773074, 773075, 773077, 773078, 773082, 773083, 773084, 773085, 773086, 773087, 773089, 773091, 773092, 773093, 773096, 773098, 773100, 773101, 773102, 773105, 773106, 773107, 773108, 773109, 773110, 773111, 773114, 773115, 773116, 773117, 773123, 773124, 773128, 773131, 773132, 773134, 773135, 773136, 773138, 773139, 773140, 773141, 773142, 773143, 773144, 773145, 773146, 773151, 773152, 773153, 773154, 773155, 773156, 773157, 773158, 773160, 773165, 773172, 773173, 773174, 773178, 773190, 773191, 773206, 773207, 773209, 773211, 773222, 773340, 773348, 773504, 773512, 773513, 773514, 773515, 773516, 773517, 773518, 773519, 773521, 994403
    ];
    const item_name_list = [
        'Boots', 'Faerie Charm', 'Rejuvenation Bead', "Giant's Belt", 'Cloak of Agility', 'Blasting Wand', 'Sapphire Crystal', 'Ruby Crystal', 'Cloth Armor', 'Chain Vest', 'Null-Magic Mantle', 'Emberknife', 'Long Sword', 'Pickaxe', 'B. F. Sword', 'Hailblade', 'Obsidian Edge', 'Dagger', 'Recurve Bow', 'Amplifying Tome', 'Vampiric Scepter', "Doran's Shield", "Doran's Blade", "Doran's Ring", 'Negatron Cloak', 'Needlessly Large Rod', 'Dark Seal', 'Cull', "Doran's Bow", 'Quest: Top', 'Quest: Mid', 'Quest: Bot', 'Quest: Support', 'Quest: Jungle', 'Scorchclaw Pup', 'Gustwalker Hatchling', 'Mosstomper Seedling', 'Eye of the Herald', 'Mosstomper Seedling', 'Gustwalker Hatchling', 'Scorchclaw Pup', "Jarvan I's", "Doran's Helm", 'Top Lane Quest', 'Mid Lane Quest', 'Bot Lane Quest', 'Support Quest', 'Jungle Quest', 'Jungle Quest Reward', 'Mid Lane Quest Reward', 'Bot Lane Quest Reward', 'Support Quest Reward', 'Jungle Quest Reward', 'Jungle Quest Reward', 'Jungle Quest Reward', 'Unleashed Teleport (Top Lane Quest Reward)', 'Top Lane Quest Reward', 'Top Lane Quest', 'Penetrating Bullets', 'Fortification', 'Reinforced Armor', "Warden's Eye", 'Vanguard', 'Reinforced Armor', 'Reinforced Armor', 'Overcharged', 'Anti-tower Socks', 'Gusto', 'Phreakish Gusto', 'Super Mech Armor', 'Super Mech Power Field', 'Turret Plating', 'Structure Bounty', 'Structure Bounty', 'Structure Bounty', 'Structure Bounty', 'OvererchargedHA', 'Fortification', 'Tower Power-Up', 'Overcharged', 'Overgrowth', 'Recall', 'Enhanced Recall', 'Health Potion', 'Disabled Recall', '', 'Total Biscuit of Everlasting Will', 'Kircheis Shard', 'Steel Sigil', 'The Brutalizer', 'Tunneler', 'Glowing Mote', 'Refillable Potion', 'Corrupting Potion', "Guardian's Amulet", "Guardian's Shroud", "Guardian's Horn", 'Poro-Snax', 'Control Ward', 'Stealth Ward', "Shurelya's Battlesong", 'Elixir of Iron', 'Elixir of Sorcery', 'Elixir of Wrath', 'Cappa Juice', 'Juice of Power', 'Juice of Vitality', 'Juice of Haste', 'Lucky Dice', 'Enhanced Lucky Dice', 'Augment Level', 'Elixir of Skill', 'Elixir of Avarice', 'Elixir of Force', 'Bandle Juice of Power', 'Bandle Juice of Vitality', 'Bandle Juice of Haste', 'Minion Dematerializer', "Seeker's Armguard", 'Shattered Armguard', 'Slightly Magical Footwear', "Overlord's Bloodmail", 'Unending Despair', 'Blackfire Torch', 'Kaenic Rookern', 'Fated Ashes', 'Dusk and Dawn', 'Fiendhunter Bolts', 'Endless Hunger', 'Bastionbreaker', 'Actualizer', 'Hexoptics C44', 'Bandlepipes', 'Protoplasm Harness', 'Whispering Circlet', 'Diadem of Songs', 'Evenshroud', 'Trailblazer', "Archangel's Staff", 'Manamune', 'Ghostcrawlers', "Berserker's Greaves", 'Gluttonous Greaves', 'Boots of Swiftness', 'Symbiotic Soles', 'Chemtech Putrifier', 'Chalice of Blessing', 'Synchronized Souls', "Sorcerer's Shoes", 'Lifewell Pendant', 'Glacial Buckler', 'Guardian Angel', 'Infinity Edge', 'Yun Tal Wildarrows', 'Mortal Reminder', 'Last Whisper', "Lord Dominik's Regards", "Atma's Reckoning", "Séraph's Embrace", "Mejai's Soulstealer", 'Muramana', 'Phage', 'Phantom Dancer', 'Plated Steelcaps', "Zeke's Convergence", 'Hearthbound Axe', "Sterak's Gage", 'Sheen', 'Spirit Visage', 'Winged Moonplate', 'Kindlegem', 'Sunfire Aegis', 'Tear of the Goddess', 'Black Cleaver', 'Bloodthirster', 'Experimental Hexplate', 'Ravenous Hydra', 'Thornmail', 'Bramble Vest', 'Tiamat', 'Trinity Force', "Warden's Mail", "Warmog's Armor", 'Heartsteel', "Runaan's Hurricane", 'Zeal', 'Statikk Shiv', "Rabadon's Deathcap", "Wit's End", 'Rapid Firecannon', 'Stormrazor', 'Lich Bane', "Banshee's Veil", 'Aegis of the Legion', 'Redemption', 'Fiendish Codex', "Knight's Vow", 'Frozen Heart', "Mercury's Treads", "Guardian's Orb", 'Aether Wisp', 'Forbidden Idol', "Nashor's Tooth", "Rylai's Crystal Scepter", 'Mobility Boots', 'Malignance', "Winter's Approach", 'Fimbulwinter', "Executioner's Calling", "Guinsoo's Rageblade", 'Deathfire Grasp', 'Sword of the Divine', "Caulfield's Warhammer", 'Serrated Dirk', 'Void Staff', 'Cryptbloom', 'Mercurial Scimitar', 'Quicksilver Sash', "Youmuu's Ghostblade", "Randuin's Omen", "Scout's Slingshot", 'Hextech Alternator', 'Hextech Gunblade', 'Haunting Guise', 'Hextech Rocketbelt', 'Blade of The Ruined King', 'Hexdrinker', 'Maw of Malmortius', "Zhonya's Hourglass", 'Ionian Boots of Lucidity', 'Spear of Shojin', 'Morellonomicon', 'Immortal Path', 'Swiftmarch', 'Crimson Lucidity', 'Gunmetal Greaves', 'Chainlaced Crushers', 'Armored Advance', "Spellslinger's Shoes", 'Forever Forward', "Guardian's Blade", 'Umbral Glaive', 'Hullbreaker', "Guardian's Hammer", 'Locket of the Iron Solari', 'Gargoyle Stoneplate', "Spectre's Cowl", "Mikael's Blessing", 'Terminus', 'Scarecrow Effigy', 'Stealth Ward', 'Arcane Sweeper', 'Lucent Singularity', 'Farsight Alteration', 'Oracle Lens', 'Small Party Favor', 'Party Favor', 'Your Cut', 'Rite Of Ruin', 'Ardent Censer', 'Essence Reaver', 'Eye of the Herald', "Kalista's Black Spear", "Kalista's Black Spear", "Dead Man's Plate", 'Titanic Hydra', 'Crystalline Bracer', 'Lost Chapter', 'Catalyst of Aeons', 'Edge of Night', "Spellthief's Edge", 'Frostfang', 'Shard of True Ice', 'Steel Shoulderguards', 'Runesteel Spaulders', 'Pauldrons of Whiterock', 'Relic Shield', "Targon's Buckler", 'Bulwark of the Mountain', 'Spectral Sickle', 'Harrowing Crescent', 'Black Mist Scythe', 'World Atlas', 'Runic Compass', 'Bounty of Worlds', 'Celestial Opposition', 'Dream Maker', "Zaz'Zak's Realmspike", 'Solstice Sleigh', 'Bloodsong', '<rarityLegendary>Fire at Will</rarityLegendary><br><subtitleLeft><silver>500 Silver Serpents</silver></subtitleLeft>', "<rarityLegendary>Death's Daughter</rarityLegendary><br><subtitleLeft><silver>500 Silver Serpents</silver></subtitleLeft>", '<rarityLegendary>Raise Morale</rarityLegendary><br><subtitleLeft><silver>500 Silver Serpents</silver></subtitleLeft>', 'Oblivion Orb', 'Lifeline', 'Spectral Cutlass', 'Imperial Mandate', "Bloodletter's Curse", 'Sword of Blossoming Dawn', 'Sin Eater', 'Lightning Braid', 'Frozen Mallet', 'Perplexity', 'Wordless Promise', 'Hellfire Hatchet', 'Force of Nature', 'Innervating Locket', 'The Golden Spatula', 'Horizon Focus', 'Cosmic Drive', 'Blighting Jewel', 'Verdant Barrier', 'Riftmaker', 'Leeching Leer', 'Night Harvester', 'Demonic Embrace', 'Watchful Wardstone', 'Stirring Wardstone', 'Bandleglass Mirror', 'Vigilant Wardstone', 'Crown of the Shattered Queen', 'Shadowflame', 'Stormsurge', 'Ironspike Whip', 'Stat Bonus', 'Silvermere Dawn', "Death's Dance", 'Chempunk Chainsword', 'Sundered Sky', 'Staff of Flowing Water', 'Moonstone Renewer', 'Echoes of Helia', 'Dawncore', 'Goredrinker', 'Stridebreaker', 'Divine Sunderer', "Liandry's Torment", "Luden's Echo", 'Everfrost', 'Rod of Ages', "Bami's Cinder", 'Iceborn Gauntlet', 'Hollow Radiance', "Jak'Sho, The Protean", 'Radiant Virtue', 'Noonquiver', 'Galeforce', 'Kraken Slayer', 'Immortal Shieldbow', 'Navori Flickerblade', 'The Collector', 'Rageknife', 'Rectrix', 'Duskblade of Draktharr', 'Eclipse', "Prowler's Claw", "Serylda's Grudge", "Serpent's Fang", 'Axiom Arc', 'Hubris', 'Profane Hydra', 'Voltaic Cyclosword', 'Shield of the Rakkor', 'Opportunity', 'Scouting Ahead', 'Gangplank Placeholder', "Anathema's Chains", "Bloodletter's Curse", 'Abyssal Mask', 'Locked Weapon Slot', 'Cyclonic Slicers', 'YuumiBot', 'Radiant Field', 'Statikk Sword', "Lioness's Lament", 'Gatling Bunny-Guns', 'Searing Shortbow', 'The Annihilator', 'Battle Bunny Crossbow', 'UwU Blaster', 'Vortex Glove', 'Blade-o-rang', 'Bunny Mega-Blast', 'Anti-Shark Sea Mine', 'T.I.B.B.E.R.S', 'Ani-Mines', 'Final City Transit', 'Echoing Batblades', 'Paw Print Poisoner', 'Iceblast Armor', 'Unceasing Cyclone', 'YuumiBot_Final_FINAL', 'Explosive Embrace', "Prumbis's Electrocarver", 'Enveloping Light', 'Double Bun-Bun Barrage', 'Evolved Embershot', 'Animapocalypse', 'Bunny Prime Ballista', 'OwO Blaster', "Tempest's Gauntlet", 'Quad-o-rang', 'Rapid Rabbit Raindown', 'Neverending Mobstomper', 'T.I.B.B.E.R.S (B.E.E.G Edition)', "Jinx's Tri-Namite", 'FC Limited Express', "Vayne's Chromablades", 'Bearfoot Chem-Dispenser', 'Deep Freeze', 'Meow Meow', 'Shield Slam', 'Sound Wave', 'Pillory Swipe', 'Steel Tempest', 'Tentacle Slam', 'Winged Dagger', 'Guiding Hex', 'Bunny Hop', 'Battle Cat Barrage', 'Light of the Lion', 'Anima Echo', 'Savage Slice', 'Wandering Storms', 'Grizzly Smash', "Lover's Ricochet", 'Hopped-Up Hex', 'Carrot Crash', 'Rite of Ruin', 'Sword of Blossoming Dawn', 'Hubris', 'Stat Bonus', 'Legendary Fighter Item', 'Legendary Marksman Item', 'Legendary Assassin Item', 'Legendary Mage Item', 'Legendary Tank Item', 'Legendary Support Item', 'Prismatic Item', 'Anvil Voucher', 'Gold Stat Anvil Voucher', 'Prismatic Stat Voucher', 'Bravery Voucher', 'Shardblade', 'Poro-Snax', "Giant's Belt", 'Blasting Wand', 'Chain Vest', 'B. F. Sword', 'Recurve Bow', 'Vampiric Scepter', 'Negatron Cloak', 'Needlessly Large Rod', 'Glowing Mote', "Guardian's Horn", "Shurelya's Battlesong", 'Cappa Juice', 'Unending Despair', 'Blackfire Torch', 'Kaenic Rookern', 'Dusk and Dawn', 'Fiendhunter Bolts', 'Endless Hunger', 'Actualizer', 'Hexoptics C44', 'Bandlepipes', 'Protoplasm Harness', 'Whispering Circlet', 'Diadem of Songs', 'Evenshroud', 'Trailblazer', "Archangel's Staff", 'Manamune', 'Ghostcrawlers', "Berserker's Greaves", 'Gluttonous Greaves', 'Boots of Swiftness', 'Chemtech Putrifier', "Sorcerer's Shoes", 'Guardian Angel', 'Infinity Edge', 'Yun Tal Wildarrows', 'Mortal Reminder', "Lord Dominik's Regards", "Atma's Reckoning", "Seraph's Embrace", 'Muramana', 'Phantom Dancer', 'Plated Steelcaps', "Zeke's Convergence", "Sterak's Gage", 'Sheen', 'Spirit Visage', 'Kindlegem', 'Sunfire Aegis', 'Void Immolation', 'Black Cleaver', 'Bloodthirster', 'Experimental Hexplate', 'Ravenous Hydra', 'Thornmail', 'Trinity Force', 'Heartsteel', "Runaan's Hurricane", 'Statikk Shiv', "Rabadon's Deathcap", "Wit's End", 'Rapid Firecannon', 'Stormrazor', 'Lich Bane', "Banshee's Veil", 'Aegis of the Legion', 'Redemption', "Knight's Vow", 'Frozen Heart', "Mercury's Treads", "Guardian's Orb", "Nashor's Tooth", "Rylai's Crystal Scepter", 'Malignance', "Winter's Approach", 'Fimbulwinter', "Guinsoo's Rageblade", 'Void Staff', 'Cryptbloom', 'Mercurial Scimitar', "Youmuu's Ghostblade", "Randuin's Omen", 'Hextech Gunblade', 'Hextech Rocketbelt', 'Blade of The Ruined King', 'Maw of Malmortius', "Zhonya's Hourglass", 'Ionian Boots of Lucidity', 'Spear of Shojin', 'Morellonomicon', 'Zephyr', "Guardian's Blade", 'Hullbreaker', "Guardian's Hammer", "Guardian's Dirk", 'Locket of the Iron Solari', 'Gargoyle Stoneplate', "Mikael's Blessing", 'Terminus', 'Ardent Censer', 'Essence Reaver', "Dead Man's Plate", 'Titanic Hydra', 'Edge of Night', 'Spectral Cutlass', 'Imperial Mandate', 'Force of Nature', 'The Golden Spatula', 'Horizon Focus', 'Cosmic Drive', 'Riftmaker', 'Night Harvester', 'Demonic Embrace', 'Crown of the Shattered Queen', 'Shadowflame', 'Stormsurge', 'Silvermere Dawn', "Death's Dance", 'Chempunk Chainsword', 'Sundered Sky', 'Staff of Flowing Water', 'Moonstone Renewer', 'Echoes of Helia', 'Dawncore', 'Goredrinker', 'Stridebreaker', 'Divine Sunderer', "Liandry's Anguish", "Luden's Echo", 'Everfrost', 'Rod of Ages', '', 'Iceborn Gauntlet', 'Hollow Radiance', "Jak'Sho, The Protean", 'Radiant Virtue', 'Ultra Hydra', 'Galeforce', 'Kraken Slayer', 'Immortal Shieldbow', 'Navori Flickerblades', 'The Collector', 'Duskblade of Draktharr', 'Eclipse', "Prowler's Claw", "Serylda's Grudge", "Serpent's Fang", 'Axiom Arc', 'Hubris', 'Profane Hydra', 'Voltaic Cyclosword', 'Opportunity', "Anathema's Chains", "Wooglet's Witchcap", 'Deathblade', 'Adaptive Helm', 'Obsidian Cleaver', 'Sanguine Blade', 'Runeglaive', 'Multitool', 'Abyssal Mask', "Shurelya's Battlesong", 'Whispering Circlet', 'Diadem of Songs', 'Trailblazer', "Archangel's Staff", 'Manamune', "Seraph's Embrace", 'Muramana', "Zeke's Convergence", 'Tear of the Goddess', 'Thornmail', 'Redemption', "Knight's Vow", 'Frozen Heart', "Winter's Approach", 'Fimbulwinter', 'Locket of the Iron Solari', "Mikael's Blessing", 'Ardent Censer', 'Imperial Mandate', 'Staff of Flowing Water', 'Moonstone Renewer', 'Echoes of Helia', 'Dawncore', 'Rod of Ages', 'Abyssal Mask', 'Darksteel Talons', 'Fulmination', "Demon King's Crown", 'Shield of Molten Stone', 'Cloak of Starry Night', 'Sword of the Divine', 'Force Of Entropy', 'Sanguine Gift', "Eleisa's Miracle", 'Talisman Of Ascension', 'Hamstringer', 'Turbo Chemtank', 'Twin Mask', 'Hexbolt Companion', "Warmog's Armor", "Reaper's Toll", 'Gargoyle Stoneplate', 'Night Harvester', 'Demonic Embrace', 'Crown of the Shattered Queen', 'Divine Sunderer', 'Everfrost', 'Radiant Virtue', 'Galeforce', 'Duskblade of Draktharr', "Prowler's Claw", 'Mirage Blade', "Gambler's Blade", 'Reality Fracture', "Hemomancer's Helm", 'Innervating Locket', 'Empyrean Promise', 'Dragonheart', 'Decapitator', 'Runecarver', 'Cruelty', 'Moonflair Spellblade', "Overlord's Bloodmail", 'Flesheater', 'Detonation Orb', 'Reverberation', 'Regicide', 'Kinkou Jitte', "Pyromancer's Cloak", 'Lightning Rod', 'Diamond-Tipped Spear', "Twilight's Edge", 'Black Hole Gauntlet', 'Puppeteer', 'Healthbar Splash: Blue', 'Healthbar Splash: Orange', 'Healthbar Splash: Green', 'Healthbar Splash: Pink', 'Healthbar Cleanup: Reset Color', 'Healthbar Splash: Rainbow', 'Party Favor', "Atma's Reckoning", "Demon King's Crown", 'Shield of Molten Stone', 'Cloak of Starry Night', 'Sword of the Divine', "Veigar's Talisman of Ascension", 'Hextech Gunblade', 'Zephyr', 'Gargoyle Stoneplate', 'Sword of Blossoming Dawn', 'The Golden Spatula', 'Crown of the Shattered Queen', "Gambler's Blade", 'Cruelty', 'Flesheater', 'The Collector', 'Boots of Speed', 'Faerie Charm', 'Rejuvenation Bead', "Giant's Belt", 'Cloak of Agility', 'Blasting Wand', 'Sapphire Crystal', 'Ruby Crystal', 'Cloth Armor', 'Chain Vest', 'Null-Magic Mantle', 'Long Sword', 'Pickaxe', 'B. F. Sword', "Hunter's Machete", 'Dagger', 'Recurve Bow', "Brawler's Gloves", 'Amplifying Tome', 'Vampiric Scepter', "Doran's Shield", "Doran's Blade", "Doran's Ring", 'Negatron Cloak', 'Needlessly Large Rod', 'Spirit Stone', 'Penetrating Bullets', 'Recall', 'Health Potion', 'Mana Potion', 'Total Biscuit of Rejuvenation', 'Elixir of Fortitude', 'Elixir of Agility', 'Elixir of Brilliance', 'Crystalline Flask', "Oracle's Elixir", 'Vision Ward', 'Sight Ward', 'Ruby Sightstone', 'Sightstone', "Explorer's Ward", '', '', 'Abyssal Scepter', "Archangel's Staff", 'Manamune', "Atma's Impaler", "Berserker's Greaves", 'Boots of Swiftness', 'Catalyst the Protector', "Sorcerer's Shoes", 'Frozen Mallet', 'Twin Shadows', 'Glacial Shroud', 'Iceborn Gauntlet', 'Guardian Angel', 'Rod of Ages', 'Chalice of Harmony', 'Infinity Edge', 'Last Whisper', 'Mana Manipulator', "Seraph's Embrace", "Mejai's Soulstealer", 'Muramana', 'Phage', 'Phantom Dancer', 'Ninja Tabi', "Stark's Fervor", 'Emblem of Valor', 'Ohmwrecker', 'Sheen', 'Banner of Command', 'Soul Shroud', 'Force of Nature', 'Spirit Visage', 'Kindlegem', 'Sunfire Cape', "Shurelya's Reverie", 'Tear of the Goddess', 'The Black Cleaver', 'The Bloodthirster', 'Stack of Sunfire Capes', 'Ravenous Hydra', 'Thornmail', 'Tiamat', 'Trinity Force', "Warden's Mail", "Warmog's Armor", 'Innervating Locket', "Runaan's Hurricane", 'Zeal', 'Statikk Shiv', "Rabadon's Deathcap", "Wit's End", 'Shard of True Ice', 'Avarice Blade', "Philosopher's Stone", 'Lucky Pick', 'Lich Bane', 'Stinger', "Banshee's Veil", 'Aegis of the Legion', "Madred's Razors", 'Runic Bulwark', 'Fiendish Codex', "Madred's Bloodrazor", 'Frozen Heart', "Mercury's Treads", 'Malady', "Nashor's Tooth", "Rylai's Crystal Scepter", 'Boots of Mobility', "Executioner's Calling", "Guinsoo's Rageblade", 'Deathfire Grasp', 'Sword of the Divine', 'Heart of Gold', 'The Brutalizer', 'Void Staff', 'Haunting Guise', 'Leviathan', 'Mercurial Scimitar', 'Quicksilver Sash', 'Sword of the Occult', "Youmuu's Ghostblade", "Randuin's Omen", 'Bilgewater Cutlass', 'Hextech Revolver', 'Hextech Gunblade', "Liandry's Torment", 'Will of the Ancients', 'Blade of The Ruined King', "Wriggle's Lantern", 'Hexdrinker', 'Maw of Malmortius', "Zhonya's Hourglass", 'Ionian Boots of Lucidity', 'Feral Flare', 'Morellonomicon', 'Zephyr', "Eleisa's Miracle", "Shushei's Mana Jug", 'Ionic Spark', 'Locket of the Iron Solari', "Seeker's Armguard", 'Spirit of the Spectral Wraith', 'Spirit of the Ancient Golem', 'Spirit of the Elder Lizard', "Spectre's Cowl", "Mikael's Crucible", 'Yellow Trinket', 'Red Trinket', 'Ardent Censer', "Zz'Rot Portal", 'Prototype Hex Core', 'Hex Core mk-1', 'Hex Core mk-2', 'Perfect Hex Core', 'Eggnog', 'Bag of Tea', 'Candy Corn', 'Health Potion', 'Golden Spatula'
    ];
    const champ_name_list = [
        'Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Ambessa', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'AurelionSol', 'Aurora', 'Azir', 'Bard', 'Belveth', 'Blitzcrank', 'Brand', 'Braum', 'Briar', 'Caitlyn', 'Camille', 'Cassiopeia', 'Chogath', 'Corki', 'Darius', 'Diana', 'Draven', 'DrMundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Hwei', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'JarvanIV', 'Jax', 'Jayce', 'Jhin', 'Jinx', 'Kaisa', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', 'Khazix', 'Kindred', 'Kled', 'KogMaw', 'KSante', 'Leblanc', 'LeeSin', 'Leona', 'Lillia', 'Lissandra', 'Locke', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'MasterYi', 'Mel', 'Milio', 'MissFortune', 'MonkeyKing', 'Mordekaiser', 'Morgana', 'Naafiri', 'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nilah', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', 'RekSai', 'Rell', 'Renata', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Smolder', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'TwistedFate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', 'Velkoz', 'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Xayah', 'Xerath', 'XinZhao', 'Yasuo', 'Yone', 'Yorick', 'Yunara', 'Yuumi', 'Zaahen', 'Zac', 'Zed', 'Zeri', 'Ziggs', 'Zilean', 'Zoe', 'Zyra'
    ];
    let liveclientdata = $state({})
    let builds = $state(structuredClone(builds_json))
    let temp = $state(0)
    let search = $state("")
    let tab = $state(1)
    
    let loaded = $state(false)
    let search_focus = $state(false)

    let results = $derived(
        item_id_list
            .map(id => ({
                id,
                name: json.data[String(id)].name
            }))
            .filter(item =>
                item.name.toLowerCase().includes(search.toLowerCase())
            )
            .slice(0, 10)
    );


    function getGold(id) {
        if (typeof id === "number") {return json.data[String(item_id_list[id])].gold.total}
        if (Array.isArray(id)) {
            let gold = 0
            for (let item_id of id) {
                gold += getGold(item_id)
            }
            return gold
        }
    }
    function searching() {
        if (search.startsWith(":")) {temp = Number(search.slice(1, search.length));}
        else {temp = item_id_list[item_name_list.indexOf(search)]}
    }
    function selectItem(id) {
        id = Number(id)

        let index = item_id_list.indexOf(id)

        if (index === -1) {
            index = id
            id = item_id_list[index]
        }

        temp = index
        search = json.data[String(id)].name
        search_focus = false
    }
    function insertItem(build, id) {
        build["item"][id] = temp
    }
    function insertBonus(build) {
        build["bonus"].push(temp)
    }
    async function saveBuild() {
        const response = await fetch("/api/saveBuildLol", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                build: $state.snapshot(builds)
            })
        });
        const data = await response.json();

        console.log(data);
    }
    async function getLiveClientData() {
        if (tab == 2) {
            try {
                const response = await fetch("/api/liveclientdata");

                if (!response.ok) return;

                liveclientdata = await response.json();
            } catch (error) {
                // On ne fait rien : liveclientdata garde son ancienne valeur
                console.log("Live Client indisponible");
            }
        }
    }

    onMount(() => {
        getLiveClientData()
        loaded = true;
        interval = setInterval(() => {
            getLiveClientData()
        }, 1000);
    });
    let tmp = $state(true)
</script>
{#if loaded}

<button class="bg-zinc-700 rounded-lg" onclick={() => {tab = 1}}>Item Build</button>
<button class="bg-zinc-700 rounded-lg" onclick={() => {tab = 2}}>Current Match</button>

{#if tab == 1}
<div class="grid grid-cols-2">
<div id="main">
    <button onclick={saveBuild}>Save Build</button>
    <button onclick={() => {}}>New Build</button>
    <div class="builds">
        {#each Object.values(builds) as build}
            <div class="build">
                <input bind:value={build["name"]} readonly={tmp} ondblclick={() => {tmp=false}} onfocusout={() => {tmp=true}}>
                <div class="build-item">
                    {#each build["item"] as item, id}
                        {#if item != -1}
                            <Item id={item} onclick={() => selectItem(item)} oncontextmenu={() => {build["item"][id] = -1}}/>
                        {:else}
                            <button class="add-block" onclick={() => {insertItem(build, id)}} >+</button>
                        {/if}
                    {/each}
                    <div class="bonus-item" style={`grid-template-columns: repeat(${build["bonus"].length+1}, 64px);`}>
                    {#each build["bonus"] as item, id}
                           <Item id={item} onclick={() => selectItem(item)} oncontextmenu={() => {build["bonus"].splice(id, 1)}}/>
                    {/each}
                    <button class="add-block" onclick={() => {insertBonus(build)}} >+</button>
                    </div>
                </div>
            </div> 
        {/each}
    </div>
</div>

<div id="item-tab">
    <input 
        bind:value={search} 
        onkeyup={searching} 
        onfocusin={() => {search_focus=true}}
        id="search-tab"
        type="text"
    >
    {#if search.length > 0 && search_focus}
        <div id="suggestions">
            {#each results as item}
                <button class="suggestion-button" onclick={() => selectItem(item.id)}>
                    <Item id={item_id_list.indexOf(item.id)}/>
                    <span>{item.name}</span>
                </button>
            {/each}
        </div>
    {/if}

    {#if temp != undefined && search.length != 0}
        <div id="little-box">
            <Item id={temp}/>
            {json.data[String(item_id_list[temp])].name}<br>
            {getGold(temp)} gold<br>
        </div>
        <div id="item-info">{@html json.data[String(item_id_list[temp])].description}</div>

        {#if json.data[String(item_id_list[temp])].from}
            <div id="item-info">
                Craft Item: <br>
                {#each json.data[String(item_id_list[temp])].from as item}
                    <Item id={item_id_list.indexOf(Number(item))} onclick={() => selectItem(item)}/>
                {/each}
            </div>
        {/if}
        {#if json.data[String(item_id_list[temp])].into}
            <div id="item-info">
                Used for Item: <br>
                {#each json.data[String(item_id_list[temp])].into as item}
                    <Item id={item_id_list.indexOf(Number(item))} onclick={() => selectItem(item)}/>
                {/each}
            </div>
        {/if}
    <details style={"border-top: 2px solid rgb(12, 25, 39); margin: 8px;"}>
        <summary>More Details</summary>
        {#if temp != undefined}
            <pre>{JSON.stringify(json.data[String(item_id_list[temp])], null, '  ')}</pre>
        {/if}
    </details>
    {/if}
</div>
</div>
{/if}
{#if tab == 2}
{#each liveclientdata.allPlayers as player}
    <div style="border: 2px solid black; background-color: rgb(53, 70, 88); color: white;">
    <div>
    <Champion id={champ_name_list.indexOf(player["championName"].replace("'", ""))}/>
    {player["riotId"]}
    <pre>{JSON.stringify(String(player["scores"]), null, '  ')}</pre>
    
    </div>
    <div style="display: grid; grid-template-columns: repeat(10, 64px);">
    {#each player["items"] as items}
        <Item id={item_id_list.indexOf(Number(items["itemID"]))} onclick={() => selectItem(item)}/>
    {/each}
    </div>
    </div>
{/each}
<i>Most Kill</i>
<pre>{JSON.stringify(liveclientdata.allPlayers, null, '  ')}</pre>
{/if}
{/if}
<style>
    #item-tab {
        color: white;
        background-color: rgb(53, 70, 88);
        border: 2px solid black;
        width: auto;
        height: 100%;
        font-family: "Roboto", sans-serif;
        resize: horizontal;
        overflow: auto;
    }
    #little-box {
        color: white;
        border: 2px solid black;
        border-radius: 5px;
        margin: 10px;
        display: flex;
        background-color: rgb(91, 111, 132);
    }
    #item-info {
        border-top: 2px solid rgb(12, 25, 39);
        margin: 8px;
    }
    .builds {
        display: grid;
        margin: 4px;
    }
    .build {
        border: 2px solid black;
        border-radius: 5px;
        margin: 4px;
        background-color: rgb(53, 70, 88);
    }
    .build input {
        background-color: rgb(53, 70, 88);
        color: white;
    }
    .search {
        position: relative;
        width: 300px;
    }

    #search-tab {
        width: 100%;
        box-sizing: border-box;
        padding: 8px;
    }

    .suggestions {
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: rgb(53, 70, 88);
        border: 2px solid black;
        z-index: 10;
    }

    .suggestions button {
        width: 100%;
        height: 50px;
        display: flex;
        align-items: center;
        gap: 10px;
        border: none;
        background: transparent;
        color: white;
        cursor: pointer;
        text-align: left;
    }

    .suggestions button:hover {
        background: rgb(91, 111, 132);
    }
    .add-block {
        width: 64px;
        height: 64px;
        font-size: xx-large;
        color: white;
        background: linear-gradient(to top, rgb(53, 70, 88), rgb(91, 111, 132));
        background-repeat: no-repeat;
    }
    .build-item {
        display: grid;
        grid-template-columns: repeat(8, 64px);
    }
    .suggestion-button {
        color: white;
        background: rgb(91, 111, 132);
    }
    .bonus-item {
        display: grid;
        border-left: 2px solid rgb(12, 25, 39);
        margin-left: 24px;
    }
</style>

