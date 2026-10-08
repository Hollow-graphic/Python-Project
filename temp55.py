import json
from pathlib import Path
import os

class vanilla:
    MAX_HEALTH = "Attributes.MAX_HEALTH"
    ARMOR_TOUGHNESS = "Attributes.ARMOR_TOUGHNESS"
    ARMOR = "Attributes.ARMOR"
    ATTACK_DAMAGE = "Attributes.ATTACK_DAMAGE"
    ATTACK_SPEED = "Attributes.ATTACK_SPEED"
    ATTACK_KNOCKBACK = "Attributes.ATTACK_KNOCKBACK"
    KNOCKBACK_RESISTANCE = "Attributes.KNOCKBACK_RESISTANCE"
    MOVEMENT_SPEED = "Attributes.MOVEMENT_SPEED"
    FOLLOW_RANGE = "Attributes.FOLLOW_RANGE"
    FLYING_SPEED = "Attributes.FLYING_SPEED"
    LUCK = "Attributes.LUCK"
    BLOCK_BREAK_SPEED = "Attributes.BLOCK_BREAK_SPEED"
    BLOCK_INTERACTION_RANGE = "Attributes.BLOCK_INTERACTION_RANGE"
    STEP_HEIGHT = "Attributes.STEP_HEIGHT"
    SCALE = "Attributes.SCALE"
    GRAVITY = "Attributes.GRAVITY"
    SAFE_FALL_DISTANCE = "Attributes.SAFE_FALL_DISTANCE"
    FALL_DAMAGE_MULTIPLIER = "Attributes.FALL_DAMAGE_MULTIPLIER"
    JUMP_STRENGTH = "Attributes.JUMP_STRENGTH"
    BURNING_TIME = "Attributes.BURNING_TIME"
    EXPLOSION_KNOCKBACK_RESISTANCE = "Attributes.EXPLOSION_KNOCKBACK_RESISTANCE"
    MAX_ABSORPTION = "Attributes.MAX_ABSORPTION"
    TEMPERATURE = "Attributes.TEMPERATURE"
    MOVEMENT_EFFICIENCY = "Attributes.MOVEMENT_EFFICIENCY"
    OXYGEN_BONUS = "Attributes.OXYGEN_BONUS"
    WATER_MOVEMENT_EFFICIENCY = "Attributes.WATER_MOVEMENT_EFFICIENCY"
    
class apothic:
    ARMOR_PIERCE = "ALObjects.Attributes.ARMOR_PIERCE.get()"
    ARMOR_SHRED = "ALObjects.Attributes.ARMOR_SHRED.get()"
    ARROW_DAMAGE = "ALObjects.Attributes.ARROW_DAMAGE.get()"
    ARROW_VELOCITY = "ALObjects.Attributes.ARROW_VELOCITY.get()"
    COLD_DAMAGE = "ALObjects.Attributes.COLD_DAMAGE.get()"
    CRIT_CHANCE = "ALObjects.Attributes.CRIT_CHANCE.get()"
    CRIT_DAMAGE = "ALObjects.Attributes.CRIT_DAMAGE.get()"
    CURRENT_HP_DAMAGE = "ALObjects.Attributes.CURRENT_HP_DAMAGE.get()"
    DODGE_CHANCE = "ALObjects.Attributes.DODGE_CHANCE.get()"
    EXPERIENCE_GAINED = "ALObjects.Attributes.EXPERIENCE_GAINED.get()"
    FIRE_DAMAGE = "ALObjects.Attributes.FIRE_DAMAGE.get()"
    GHOST_HEALTH = "ALObjects.Attributes.GHOST_HEALTH.get()"
    HEALING_RECEIVED = "ALObjects.Attributes.HEALING_RECEIVED.get()"
    LIFE_STEAL = "ALObjects.Attributes.LIFE_STEAL.get()"
    OVERHEAL = "ALObjects.Attributes.OVERHEAL.get()"
    PROT_PIERCE = "ALObjects.Attributes.PROT_PIERCE.get()"
    PROT_SHRED = "ALObjects.Attributes.PROT_SHRED.get()"

class forge:
    SWIM_SPEED = "ForgeMod.SWIM_SPEED.get()"
    NAMETAG_DISTANCE = "ForgeMod.NAMETAG_DISTANCE.get()"
    ENTITY_GRAVITY = "ForgeMod.ENTITY_GRAVITY.get()"
    BLOCK_REACH = "ForgeMod.BLOCK_REACH.get()"
    ENTITY_REACH = "ForgeMod.ENTITY_REACH.get()"
    STEP_HEIGHT_ADDITION = "ForgeMod.STEP_HEIGHT_ADDITION.get()"

class OA:
    LOL_AD = "ModAttributes.LOL_AD.get()"
    LOL_AP = "ModAttributes.LOL_AP.get()"


class operation:
    ADDITION = "ADDITION"
    MULTIPLY_BASE = "MULTIPLY_BASE"
    MULTIPLY_TOTAL = "MULTIPLY_TOTAL"

main_dir = Path(r"C:\Users\hollo\Desktop\Mods Minecraft\Otherworld Artifact\src\main")

item_name = "Dead Cells Stats"

item_name_under = item_name.replace(" ", "_").replace("'", "").replace("-", "_")
item_name_lower = item_name_under.lower()
item_name_upper = item_name_under.upper()

item_lol_id = 3089

if item_lol_id != -1:
    with open("./data/lol/item.json", "r", encoding="utf-8") as f:
        item_json = json.load(f)["data"]
    with open("./data/lol/item_fr.json", "r", encoding="utf-8") as f:
        item_json_fr = json.load(f)["data"]
    item_name = item_json[str(item_lol_id)]["name"]
    item_name_under = item_name.replace(" ", "_").replace("'", "").replace("-", "_")
    item_name_lower = item_name_under.lower()
    item_name_upper = item_name_under.upper()

print(item_name_under, item_name_lower, item_name_upper)

def get_lol_name(item_lol_id):
    return item_json[item_lol_id]["name"].replace(" ", "_").lower().replace("'", "")

def get_lol_image():
    import requests
    path = main_dir / "resources" / "assets" / "otherworld_artifact" / "textures" / "item" / f"{item_name_lower}.png"
    data = requests.get(f"https://ddragon.leagueoflegends.com/cdn/16.17.1/img/item/{item_lol_id}.png")
    data.raise_for_status()
    with open(path, "wb") as f:
        f.write(data.content)

def create_model():
    path = main_dir / "resources" / "assets" / "otherworld_artifact" / "models" / "item" / f"{item_name_lower}.json"
    text = {'parent': 'item/generated', 'textures': {'layer0': 'otherworld_artifact:item/' + item_name_lower}}

    with open(path, 'w') as f:
        json.dump(text, f, indent=2, ensure_ascii=False)
    print(text)

def create_lol_craft():
    try:
        ingredients = [get_lol_name(item_lol_id) for item_lol_id in item_json[str(item_lol_id)]["from"]]
        craft_json = {"type": "minecraft:crafting_shapeless", "ingredients": [], "result": {}}
        for i, v in enumerate(ingredients):
            craft_json["ingredients"].append({"item": "otherworld_artifact:" + v.replace("-", "_")})
        craft_json["result"]["item"] = "otherworld_artifact:" + item_name_lower

        print(craft_json)
        path = main_dir / "resources" / "data" / "otherworld_artifact" / "recipes" / f"{item_name_lower}.json"
        with open(path, "w") as f:
            json.dump(craft_json, f, indent=4, ensure_ascii=False)
    except:
        pass

def create_craft(ingredients):
    try:
        craft_json = {"type": "minecraft:crafting_shapeless", "ingredients": [], "result": {}}
        for i, v in enumerate(ingredients):
            craft_json["ingredients"].append({"item": "otherworld_artifact:" + v.replace("-", "_")})
        craft_json["result"]["item"] = "otherworld_artifact:" + item_name_lower

        print(craft_json)
        path = main_dir / "resources" / "data" / "otherworld_artifact" / "recipes" / f"{item_name_lower}.json"
        with open(path, "w") as f:
            json.dump(craft_json, f, indent=4, ensure_ascii=False)
    except:
        pass

def create_lang():
    path = main_dir / "resources" / "assets" / "otherworld_artifact" / "lang" / "en_us.json"
    with open(path, "r") as f: data = json.load(f)
    data[f"item.otherworld_artifact.{item_name_lower}"] = item_name
    with open(path, "w") as f: json.dump(data, f, indent=4, ensure_ascii=False)
    
    if item_lol_id:
        path = main_dir / "resources" / "assets" / "otherworld_artifact" / "lang" / "fr_fr.json"
        with open(path, "r") as f: data = json.load(f)
        data[f"item.otherworld_artifact.{item_name_lower}"] = item_json_fr[str(item_lol_id)]["name"]
        with open(path, "w") as f: json.dump(data, f, indent=4, ensure_ascii=False)

def create_curio(curio: str):
    path = main_dir / "resources" / "data" / "curios" / "tags" / "items" / (curio + ".json")
    with open(path, "r") as f: data = json.load(f)
    if f"otherworld_artifact:{item_name_lower}" not in data["values"]:
        data["values"].append("otherworld_artifact:" + item_name_lower)
        with open(path, "w") as f: json.dump(data, f, indent=4, ensure_ascii=False)

def create_java_charm(stats_list: list, force_id=-1, folder="other"):
    path = main_dir / "java" / "net" / "hollow" / "otherworld_artifact" / "otherworld_artifact" / "item" / "lol" / "Base_Charm.txt"

    text = path.read_text(encoding="utf-8")
    if force_id == -1:
        uuid = f"{len(os.listdir(path.parent)):03d}"
    else:
        uuid = f"{force_id:03d}"
    text = text.replace("Base_Charm", item_name_under).replace("247", uuid)
    
    text_stats = ""
    for i in reversed(stats_list):
        text_stats += f'map.put(\n                {i[0]},\n                new AttributeModifier(\n                        ATTR_ID,\n                        Otherworld_artifact.MODID + ":{item_name_lower}",\n                        {i[1]}D,\n                        AttributeModifier.Operation.{i[2]}\n                )\n        );\n        '
    
    text = text.replace("//STATS_LIST", text_stats)
    
    new_path = path.parent.parent / folder / f"{item_name_under}.java"
    new_path.write_text(text, encoding="utf-8")
    print(f"Create {item_name_under}", uuid)

def create_creativetab():
    path = main_dir / "java" / "net" / "hollow" / "otherworld_artifact" / "otherworld_artifact" / "ModCreativeTab.java"
    text = path.read_text(encoding="utf-8")
    if item_name_upper not in text:
        text = text.replace("//TEMP", f"pOutput.accept(AddItems.{item_name_upper}.get());\n                        //TEMP")
        path.write_text(text, encoding="utf-8")
        print("Added to ModCreativeTab.java")

def create_additem(item_stack=1):
    path = main_dir / "java" / "net" / "hollow" / "otherworld_artifact" / "otherworld_artifact" / "AddItems.java"
    text = path.read_text(encoding="utf-8")
    if item_name_upper not in text:
        text = text.replace("//TEMP", f'public static final RegistryObject<Item> {item_name_upper} = ITEMS.register("{item_name_lower}",\n            () -> new {item_name_under}(new Item.Properties().stacksTo({item_stack})));\n    //TEMP')
        path.write_text(text, encoding="utf-8")
    print("Added to AddItems.java")

def add_loot():
    path = main_dir / "java" / "net" / "hollow" / "otherworld_artifact" / "otherworld_artifact" / "loot" /"CharmLootModifier.java"
    text = path.read_text(encoding="utf-8")
    if item_name_upper not in text:
        text = text.replace("\n            //TEMP", f",\n            AddItems.{item_name_upper}\n            //TEMP")
        path.write_text(text, encoding="utf-8")
        print("Added to ModCreativeTab.java")


if item_name != "":
    get_lol_image()
    create_lol_craft()
    create_lang()
    create_model()
    create_curio("lol_item")
    create_java_charm([[apothic.ARROW_DAMAGE, 0.4, operation.MULTIPLY_BASE],[apothic.ARROW_DAMAGE, 0.2, operation.MULTIPLY_TOTAL]])
    create_creativetab()
    create_additem()
    # add_loot()
    pass



