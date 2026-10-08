import os
import random

import time

dir = r"C:\Users\Adam\AppData\Roaming\PrismLauncher\instances\Mods Randomizer\minecraft\mods"
base_dir = dir + r"\_base"
mods_dir = dir + r"\_mods"

duplicate_mods = {"Apotheosis":{"magic","structure","other"}}

nb_mod_category = {}
nb_mod_category["production"] = 1
nb_mod_category["mechanical"] = 1 -1
nb_mod_category["magic"] = 1
nb_mod_category["storage"] = 1
nb_mod_category["structure"] = 0
nb_mod_category["biome"] = 0
nb_mod_category["other"] = 0

nb_mods = 5 -1 
chosen_mods_list = ["MCA", "IndustrialForegoing"]
#chosen_mods_list = 
banned_mods_list = ["Apotheosis", "Quark","Occultism","AE2","ProjectE","Paraglider"]

_load_mods = False

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
        "Apotheosis",
    },
    "storage": {
        "RefinedStorage",
        "SophisticatedStorage",
        "AE2",
        "Occultism",
        "IntegratedDynamics",
    },
    "structure": {
        "Apotheosis",
        "Relics",
        "YungsBetter",
    },
    "biome": {
        "Terralith",
        "BiomesOPlenty",
        "OhTheBiomesYoullGo",
    },
    "other": {
        "Pipez",
        "Quark",
        "Paraglider",
        "Farmer'sDelight",
        "RFTools",
        "Apotheosis",
        "TConstruct",
        "BotanyPots",
        "MCA",
    }
}

def choose_category(category):
    nb = nb_mod_category[category]
    for _ in range(nb):
        choose_mod(category)
        
def choose_mod(category):
    category_mod_list = list(mods_list[category])
    mod_name = random.choice(category_mod_list)
    failed = False
    print(f"//:{category} : {nb_mod_category[category]}", end="")
    while mod_name in chosen_mods_list or mod_name in banned_mods_list:
        if not failed:
            failed = True
            print()
        print(f"--:{mod_name}")
        category_mod_list.remove(mod_name)
        if not category_mod_list:
            print(f"ERROR: No more mods available in {category}")
            print(f"Chosen mods: {chosen_mods_list}")
            return
        mod_name = random.choice(category_mod_list)
        time.sleep(0.1)
        
    if mod_name in duplicate_mods:
        for i in duplicate_mods[mod_name]:
            nb_chosen_category[i] += 1
    else:
        nb_chosen_category[category] += 1
    if not failed:
        print(f" : {mod_name}")
    else:
        print(f"++: {mod_name}")
    chosen_mods_list.append(mod_name)
    #print(mod_name)

def unlist_mod(mod_name):
    for category in mods_list:
        if mod_name in mods_list[category]:
            mods_list[category].remove(mod_name)
            if category == {}:
                mods_list.pop(category, None)
            


nb_chosen_category = {i: 0 for i in mods_list}
total_mods = sum([len(mods_list[i]) for i in mods_list])
total_mods += len(duplicate_mods) - sum([len(duplicate_mods[i]) for i in duplicate_mods])
min_mods = sum([nb_mod_category[category] for category in mods_list])
bonus_mods = max(0, nb_mods - min_mods)
    

if nb_mods>total_mods:
    exit(f"ERROR: nb_mods is above the total number of mods available, which is {total_mods}")
for category in mods_list:
    if nb_mod_category[category] > len(mods_list[category]):
        exit(f"ERROR: nb_{category}_mod is above the mods in {category}")
if nb_mods + len(chosen_mods_list) < min_mods:
    exit("ERROR: nb_mods is below the sum of the category selected")

if nb_mods != 0:
    for i in mods_list:
        choose_category(i)
    for i in range(bonus_mods):
        category = random.choice(list(mods_list))
        while nb_chosen_category[category] >= len(mods_list[category]) or nb_mod_category[category] == 0:
            print(f"--:{category} : {nb_mod_category[category]}")
            category = random.choice(list(mods_list))
        choose_mod(category)
        
#move the mod file in dir
def add_mods(mod_dir):
    for file in os.listdir(mod_dir):
        os.system(f'copy "{mod_dir}\\{file}" "{dir}\\{file}"')

if _load_mods:
    #remove all the files in dir
    for file in os.listdir(dir):
        if file.endswith(".jar"):
            os.remove(f"{dir}\\{file}")
    # add all the mods in _base dir
    add_mods(base_dir)
    # add all the mods chosen
    for i in chosen_mods_list:
        add_mods(f"{mods_dir}\\{i}")


print("[----------------------------------------------]")
print(f"Mods Counts: {nb_mods}, Min Mods: {min_mods}, Bonus Mods: {bonus_mods}, Total mods: {total_mods}")
print(chosen_mods_list)
print("[----------------------------------------------]")