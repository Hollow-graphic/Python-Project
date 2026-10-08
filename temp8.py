import random
from pathlib import Path
import shutil

base_dir = r"C:\Users\Adam\Desktop\Shortcut\Game\Archipelago\Players"
rando_dir = r"C:\Users\Adam\Desktop\Shortcut\Game\Archipelago\Players\Finished"
backup_dir = r"C:\Users\Adam\Desktop\Shortcut\Game\Archipelago\Players\backup"

MAX_TIMER = 30

rando_list = [
    ["Celeste64",   8,  "HollowC64-56.yaml"],
    ["HK",          15, "HollowHK-486.yaml"],
    ["KirbyAM",     10, "HollowKirbyAM-309.yaml"]  
]

chossen_rando = []
sum_timer = 0
while sum_timer < MAX_TIMER:
    if not rando_list: break
    
    rando = random.choice(rando_list)
    while rando[1] + sum_timer > MAX_TIMER:
        rando_list.pop(rando_list.index(rando))
        if not rando_list: break
        rando = random.choice(rando_list)
    if not rando_list: break
    sum_timer += rando[1]
    chossen_rando.append(rando)
    rando_list.pop(rando_list.index(rando))

print([i[0] for i in chossen_rando])
print(sum_timer)

if True:
    for file in Path(base_dir).glob("*.yaml"):
        shutil.move(file, Path(backup_dir) / file.name)
        
    for rando in chossen_rando:
        path = Path(rando_dir) / rando[2]
        shutil.copy2(path, Path(base_dir) / rando[2])
