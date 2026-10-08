import zipfile
from pathlib import Path
import json

minecraft_jar = "C:\\Users\\Adam\\AppData\\Roaming\\.minecraft\\versions\\1.20.1\\1.20.1.jar"

type_craft = ['minecraft:crafting_shaped', 'minecraft:crafting_shapeless', 'minecraft:stonecutting', 'minecraft:smelting', 'minecraft:campfire_cooking', 'minecraft:smoking', 'minecraft:blasting', 'minecraft:smithing_trim', 'minecraft:crafting_decorated_pot', 'minecraft:smithing_transform']
json_craft = []

with zipfile.ZipFile(minecraft_jar, "r") as zip_ref:
    for i in zip_ref.filelist:
        if i.filename.startswith("data/minecraft/recipes"):
            content = str(zip_ref.open(i).read())
            crafting_type = content.split('"type": "')[1].split('",')[0]
            if not crafting_type.startswith("minecraft:crafting_sp"):
                items = [i.split('"\\n')[0] for i in content.split('    "item": "')][1:]
                ingredients = items[:-1]
                result = items[-1]
                print(i.filename, "|", crafting_type, "|", ingredients, ":", result)
                json_craft.append(i.filename)

print(type_craft)







