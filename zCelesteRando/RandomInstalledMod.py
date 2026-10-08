import random

preset = r"./zCelesteRando/data/preset.txt"
blacklist = r"C:\Program Files (x86)\Steam\steamapps\common\Celeste\Mods\blacklist.txt"
depencies = r"./zCelesteRando/data/depencies.txt"
with open(preset, "r", encoding="utf-8") as f:
    preset_data =  f.read().split("\n")
with open(blacklist, "r", encoding="utf-8") as f:
    blacklist_data =  f.read().split("\n")[3:][:-1]

text = ""
while text == "":
    zip_name = random.choice([mod for mod in blacklist_data if not mod.startswith("# ")])[:-4]
    print(zip_name)
    text = input("continue ?:")

#////////////////////////#

preset = r"./zCelesteRando/data/preset.txt"
with open(preset, "r", encoding="utf-8") as f:
    preset_data =  f.read().split("\n")

def get_depencies(zip_name):
    import zipfile
    zip_path = r"C:\Program Files (x86)\Steam\steamapps\common\Celeste\Mods" + "\\" + zip_name + ".zip"
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        with zip_ref.open("everest.yaml") as f:
            data = f.read().decode("utf-8")
        
    print(data)

    data_split = data.split("\n")
    prefix = [line for line in data_split if "Name" in line][1].split(": ")
    depencies = [line[len(prefix[0])+2:] for line in data_split if line.startswith(prefix[0])]
    
    # FIX 'Everest\r'
    if depencies[0].endswith("\r"):
        depencies = [mod[:-1] for mod in depencies]

    error_depencies = [i for i in depencies if " " in i or "_" in i]
    for i in error_depencies:
        if " " in i: depencies.append(i.replace(" ", "_"))
        if "_" in i: depencies.append(i.replace("_", " "))
    
    return depencies

def write_depencies(depencies, mod_name=""):
    text = ""
    if zip_name != "": text = f"{zip_name}.zip\n"
    for i in depencies: text += str(i) + ".zip\n"
        
    with open("./zCelesteRando/data/depencies.txt", "w", encoding="utf-8") as f:
        f.write(text)

depencies = get_depencies(zip_name)
print(depencies)

write_depencies(depencies, mod_name=zip_name)

#////////////////////////#

blacklist = r"C:\Program Files (x86)\Steam\steamapps\common\Celeste\Mods\blacklist.txt"
depencies = r"./zCelesteRando/data/depencies.txt"

reset = False


with open(blacklist, "r", encoding="utf-8") as f:
    blacklist_data =  f.read().split("\n")[3:][:-1]
with open(depencies, "r", encoding="utf-8") as f:
    depencies_data =  f.read().split("\n")[:-1]

mods_list = preset_data + depencies_data #[2:]
    
def activate_mods():
    for i, v in enumerate(blacklist_data):
        if v.startswith("# ") and reset:
            blacklist_data[i] = v[2:]
            print("Remove " + v[i])
        if v in mods_list:
            print("Enable " + v)
            blacklist_data[i] = "# " + v

activate_mods()

print(f"# {depencies_data[0]}")
if f"# {depencies_data[0]}" not in blacklist_data  and f"{depencies_data[0]}" not in blacklist_data:
    blacklist_data.insert(0, f"# {depencies_data[0]}")
    # text += f"# {depencies_data[0]}\n"
elif f"{depencies_data[0]}" in blacklist_data:
    index = blacklist_data.index(f"{depencies_data[0]}")
    blacklist_data[index] = "# " + blacklist_data[index]
    print(f"changed the index: {index}")    

text = """# This is the blacklist. Lines starting with # are ignored.
# File generated through the "Manage Installed Mods" screen in Olympus

"""
for i in blacklist_data:
    text += i + "\n"

path = blacklist
with open(path, "w", encoding="utf-8") as f:
    f.write(text)
