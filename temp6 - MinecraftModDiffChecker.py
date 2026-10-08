import os

from lib.lib import *

import temp5

file = r"C:\Users\Adam\Desktop\Mes Projects\python\temp.txt"
dir = r"C:\Users\Adam\AppData\Roaming\PrismLauncher\instances\Mods Randomizer\minecraft\mods\_mods"

data = [
    nom for nom in os.listdir(dir)
    if os.path.isdir(os.path.join(dir, nom))
]

list_mods = []
list_mods.extend(mod for mods in temp5.mods_list.values() for mod in mods)

print([i for i in data if i not in list_mods])