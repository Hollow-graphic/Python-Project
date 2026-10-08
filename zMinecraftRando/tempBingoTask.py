import random

task = {
"ProjectE": [],
"MysticalAgriculture": [],
"ThermalExpansion": [["Craft Enderium Upgrade", 4]],
"Mekanism": [["Craft HDPE", 8]],
"Create": [["Craft a Mechanical Press, 1"]],
"IndustrialForegoing": [["Craft Plastic", 1.5]],
"ImmersiveEngineering": [["Build Multiblock furnace", 1.2]],
"ForbiddenAndArcanus": [],
"ArsNouveau": [],
"Eidolon": [],
"Occultism": [["Craft Storage", 3.5], ["Craft Storage +4 Copper Upgrade"]],
"SophisticatedStorage": [],
"RefinedStorage": [["Build Basic System",3]],
"AE2": [["Build Basic System",3.5]],
"IntegratedDynamics": [],
"LaserIO": [],
"Pipez": [],
"IntegratedDynamics": [],
"UniqueAccessories": [],
"Explorify": [],
"YungsBetter": [["Visit 1 enhanced structure", 2.4]],
"Relics": [["Collect 3 Relics", 3], ["Collect 5 Relics", 5]],
"Structory": [],
"Terralith": [],
"OhTheBiomesYoullGo": [],
"BiomesOPlenty": [],
"UndeadRevamped": [],
"BornInChaos": [],
"Apotheosis": [],
"MCA": [["Get Married", 4]],
"ProjectMMO": [["Get 3 Skill at level 25", 7]],
"VanillaBackprot": [["Finish a Trial chamber", 2.6]],
"GatewaysToEternity": [["Finish 3 Gateway"]],
"CompactMachine": [],
"Pipez": [],
"OtherworldArtifact": [["Collect 3 Charms", 3], ["Collect 5 Charms"], 5],
"BotanyPots": [],
"Farmer'sDelight": [["Cook 3 different recipe", 3]],
"AdditionalAdditions": [],
"Bountiful": [],
"RFTools": [],
"Brew'nChew": [],
"Identity": [],
"Botania": [],
"AmplifiedNether": [],
"Starcatcher": [],
"GregTech": [],
"Paraglider": [],
"TConstruct": [["Build Small Smelting ...", 2], ["Build Good Smelting ...", 2]],
"RiskOfRainMobs": [],
"IronSpellbook": [],
"SkyVillages": [],
"Psi": [],
"BonsaiTree": [],
"Quark": [],
"Malum": [],
}
task = {
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
}

task_list = [[],[],[],[],[],[],[],[],[]]
for i in range(9):
    random_task = random.choice(list(task))
    while random_task in task_list:
        random_task = random.choice(list(task))
        print("nope")
    task_list[i] = random_task
        
for i in range(3):
    for j in range(3):
        print(task_list[i*3+j])
    
