import os

import main

file = r"C:\Users\Adam\Desktop\Mes Projects\python\temp.txt"
dir = r"C:\Users\Adam\AppData\Roaming\PrismLauncher\instances\Mods Randomizer\minecraft\mods\_mods"

data = [
    nom for nom in os.listdir(dir)
    if os.path.isdir(os.path.join(dir, nom))
]

list_mods = [mod for mods in main.mods_list.values() for mod in mods if mod in mods]

with open(file, "w") as f:
    for i in list_mods:
        f.write(i + "\n")

print([i for i in data if i not in list_mods])