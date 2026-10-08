import zipfile
from pathlib import Path
import json

minecraft_jar = "C:\\Users\\Adam\\AppData\\Roaming\\.minecraft\\versions\\1.20.1\\1.20.1.jar"

type_craft = ['minecraft:crafting_shaped', 'minecraft:crafting_shapeless', 'minecraft:stonecutting', 'minecraft:smelting', 'minecraft:campfire_cooking', 'minecraft:smoking', 'minecraft:blasting', 'minecraft:smithing_trim', 'minecraft:crafting_decorated_pot', 'minecraft:smithing_transform']
json_craft = []

with zipfile.ZipFile(minecraft_jar, "r") as zip_ref:
    for i in zip_ref.filelist:
        if i.filename.startswith("data/minecraft/recipes"):
            data = json.load(zip_ref.open(i))
            if data["type"] == 'minecraft:crafting_shaped':
                ingredients = []
                for key in data["key"].values():
                    if "item" in key:
                        ingredients.append(key["item"])
                    if "tag" in key:
                        ingredients.append(key["tag"])
                print(i.filename, ingredients, data["result"]["item"])