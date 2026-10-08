import zipfile
from pathlib import Path

mod = r'zCraftRando/mods/IntegratedDynamics-1.20.1-1.30.7.jar'

jars = mod

with zipfile.ZipFile(jars, "r") as zip_ref:
    data = zip_ref.filelist

type_craft = []
json_craft = []

for i in data:
    if i.filename.startswith("data/"):
        if not i.filename.startswith("data/forge/") and not i.filename.startswith("data/minecraft/"):
            if "/recipes/" in i.filename:
                if i.filename.endswith(".json"):
                    print(i.filename)
                    json_craft.append(i.filename)
                else:
                    type_craft.append(i.filename)

print("----")

for i in type_craft[1:]:
    i_split = i.split("/")
    if len(i_split) == 5 and f"data/{i_split[1]}/recipes/crafting/{i_split[3]}.json" in json_craft:
        print(i_split[-2], f"data/{i_split[1]}/recipes/crafting/{i_split[3]}.json")
    
