import random
from pathlib import Path
import shutil

dir = r"C:\Users\Adam\AppData\Roaming\PrismLauncher\instances\Mods Randomizer\minecraft\mods"
base_dir = dir + r"\_base"
mods_dir = dir + r"\_mods"

nb_mod_category = {}
#//////////////["//////////"] = [nb, Random, Bonus]
nb_mod_category["production"] = [1-1, True, False]
nb_mod_category["mechanical"] = [1-1, True, False]
nb_mod_category["magic"     ] = [0, True, False]
nb_mod_category["storage"   ] = [0, False, False]
nb_mod_category["cables"    ] = [0, False, False]
nb_mod_category["structure" ] = [0, False, True]
nb_mod_category["biome"     ] = [1, False, True]
nb_mod_category["difficulty"] = [0, False, False]
nb_mod_category["utility"   ] = [1-1, True, True]
nb_mod_category["other"     ] = [0, False, True]

nb_random_mods = 0
nb_bonus_mods = 6 -6
chosen_mods_list = ['Blocklings', 'Psi', 'MysticalAgriculture', 'Mekanism']
banned_mods_list = ["Occultism","AE2", "Terralith", "ForbiddenAndArcanus", "ProjectE", "ImmersiveEngineering", "Etheria"]
bonus_chosen_mods_list = ["GregTech", "Eidolon", "IntegratedDynamics", "Apotheosis", "MCA"]

_skip_mods = False
_load_mods = True

_print = True
_load_all_mods = False

if True:
    chosen_mods_list =          ['MysticalAgriculture', 'IndustrialForegoing', 'Create', 'Mekanism', 'IronSpell', 'Eidolon', 'ArsNouveau', 'IntegratedDynamics', 'RefinedStorage', 'SophisticatedStorage', 'Pipez', 'DungeonCrawl', 'Relics', 'Apotheosis', 'MCA', 'Blocklings', 'CompactMachine', 'AmplifiedNether', 'RFTools', "Farmer'sDelight", 'VanillaBackprot', 'OtherworldArtifact', 'Botania', 'BotanyPots', 'BonsaiTree']
    bonus_chosen_mods_list =    []

mods_list = {
    "production": {
        "ProjectE",
        "MysticalAgriculture",
    },
    "mechanical": {
        "Create",
        "Mekanism",
        "ImmersiveEngineering",
        "ThermalExpansion",
        "IndustrialForegoing",
    },
    "magic": {
        "ArsNouveau",
        "Eidolon",
        "ForbiddenAndArcanus",
        "IronSpell",
    },
    "storage": {
        "RefinedStorage",
        "SophisticatedStorage",
        "AE2",
        "Occultism",
        "IntegratedDynamics",
    },
    "cables": {
        "IntegratedDynamics",
        "Pipez",
        "LaserIO",
    },
    "structure": {
        "Relics",
        "YungsBetter",
        "Explorify",
        "UniqueAccessories",
        "Structory",
        "DungeonCrawl",
    },
    "biome": {
        "Terralith",
        "BiomesOPlenty",
        "OhTheBiomesYoullGo",
    },
    "difficulty": {
        "BornInChaos",
        "UndeadRevamped",
    },
    "utility": {
        "MCA",
        "Apotheosis",
        "ProjectMMO",
        "Psi",
        "Blocklings",
    },
    "other": {
        "Quark",
        "Paraglider",
        "RFTools",
        "BotanyPots",
        "TConstruct",
        "Pipez",
        "RiskOfRainMobs",
        "AdditionalAdditions",
        "SkyVillages",
        "AmplifiedNether",
        "GatewaysToEternity",
        "Brew'nChew",
        "Starcatcher",
        "Bountiful",
        "Botania",
        "Etheria",
        "Farmer'sDelight",
        "GregTech",
        "CompactMachine",
        "BonsaiTree",
        "VanillaBackprot",
        "Malum",
        "Identity",
        "OtherworldArtifact",
    }
}
  
def choose_mod(category, category_mod_list, current_mods_list):
    mod_name = random.choice(category_mod_list)
    print(f"//:{category} : {mod_name}")
    unlist_mod(mod_name)
    current_mods_list.append(mod_name)

def unlist_mod(mod_name):
    for category in list(mods_list.keys()):
        if mod_name in mods_list[category]:
            mods_list[category].remove(mod_name)
            if not mods_list[category]:
                mods_list.pop(category)

def possible_mods_list(category):
    category_mod_list = list(mods_list[category])
    category_mod_list = [mod for mod in category_mod_list if mod not in chosen_mods_list + bonus_chosen_mods_list]
    return category_mod_list

# move the mod file in dir
def add_mods(mod_dir):
    mod_dir = Path(mod_dir)
    for file in mod_dir.iterdir():
        if file.is_file():
            shutil.copy2(file, Path(dir) / file.name)

def main():
    for mod_name in banned_mods_list:
        unlist_mod(mod_name)

    total_mods = sum([len(mods_list[i]) for i in mods_list])
    nb_mods = int(not _skip_mods) * sum([nb_mod_category[category][0] for category in mods_list]) + len(chosen_mods_list)
    integration_chosen_mods_list = []
    
    if _load_all_mods:
        for mods in chosen_mods_list[:]:
            chosen_mods_list.remove(mods)
        for category in list(mods_list.keys()):
            for mods in mods_list[category]:
                if mods not in chosen_mods_list:
                    chosen_mods_list.append(mods)
        
    if not _skip_mods and not _load_all_mods:
        for category in mods_list:
            if nb_mod_category[category][0] > len(mods_list[category]):
                exit(f"ERROR: nb_{category}_mod is above the mods in {category}")

        for category in list(mods_list.keys()):
            for _ in range(nb_mod_category[category][0]):
                category_mod_list = possible_mods_list(category)
                choose_mod(category, category_mod_list, chosen_mods_list)
        selected_mods_list = chosen_mods_list
        
        for _ in range(nb_random_mods):
            # category = random.choice(list(random_mods_list))
            category_list = [category for category in mods_list if nb_mod_category[category][1]]
            category_mod_list = []
            while not category_mod_list:
                category = random.choice(list(category_list))
                category_mod_list = possible_mods_list(category)
            choose_mod(category, category_mod_list, chosen_mods_list)
        selected_random_mods_list = [mods for mods in chosen_mods_list if mods not in selected_mods_list]
            
        if nb_bonus_mods:
            print("--: Bonus :--")
        for _ in range(nb_bonus_mods):
            # category = random.choice(list(bonus_mods_list))
            category_list = [category for category in mods_list if nb_mod_category[category][2]]
            category_mod_list = []
            while not category_mod_list:
                category = random.choice(list(category_list))
                category_mod_list = possible_mods_list(category)
            choose_mod(category, category_mod_list, bonus_chosen_mods_list)
        selected_bonus_mods_list = bonus_chosen_mods_list

    if _load_mods:
        # remove all the files in dir
        for file in Path(dir).glob("*.jar"):
            file.unlink()
        # add all the mods in _base dir
        add_mods(base_dir)
        # add all the mods chosen
        for i in chosen_mods_list:
            add_mods(f"{mods_dir}\\{i}")
        for i in bonus_chosen_mods_list:
            add_mods(f"{mods_dir}\\{i}")
        for i in integration_chosen_mods_list:
            add_mods(f"{mods_dir}\\{i}")
        print("[Mod Loaded]")

    print("[----------------------------------------------]")
    print(f"[Mods Counts: {nb_mods} +{len(bonus_chosen_mods_list)}, Total mods: {total_mods}]")
    print(chosen_mods_list)
    if bonus_chosen_mods_list:
        print(bonus_chosen_mods_list)
    if integration_chosen_mods_list:
        print(integration_chosen_mods_list)
    print("[----------------------------------------------]")
    
    if not _skip_mods and False:
        print("")
        print(selected_mods_list)
        print(selected_random_mods_list)
        print(selected_bonus_mods_list)

if __name__ == "__main__":
    main()