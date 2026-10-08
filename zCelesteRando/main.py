import zipfile

zip_name = "♠AutumnFalls"
zip_path = r"C:\Program Files (x86)\Steam\steamapps\common\Celeste\Mods" + "\\" + zip_name + ".zip"
preset = r"./zCelesteRando/data/preset.txt"
blacklist = r"C:\Program Files (x86)\Steam\steamapps\common\Celeste\Mods\blacklist.txt"

reset = False

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    with zip_ref.open("everest.yaml") as f:
        data = f.read().decode("utf-8")
with open(preset, "r", encoding="utf-8") as f:
    preset_data =  f.read().split("\n")
with open(blacklist, "r", encoding="utf-8") as f:
    blacklist_data =  f.read().split("\n")[3:][:-1]
    
print(data)

depencies = []
        
depencies = [f"{line[12:]}.zip" for line in data.split("\n") if line.startswith("    - Name: ")]
        
print(depencies)
    
#-----------------------

mods_list = preset_data + depencies

for i in range(len(blacklist_data)):
    if blacklist_data[i].startswith("# ") and reset:
        blacklist_data[i] = blacklist_data[i][2:]
        print("Remove " + blacklist_data[i])
    if blacklist_data[i] in mods_list:
        blacklist_data[i] = "# " + blacklist_data[i]
        print("Enable " + blacklist_data[i])

text = """# This is the blacklist. Lines starting with # are ignored.
# File generated through the "Manage Installed Mods" screen in Olympus

"""

if f"# {zip_name}.zip" not in blacklist_data and f"{zip_name}.zip" not in blacklist_data:
    blacklist_data.insert(0, f"# {zip_name}.zip")
elif f"{zip_name}.zip" in blacklist_data:
    index = blacklist_data.index(f"{zip_name}.zip")
    blacklist_data[index] = "# " + blacklist_data[index]
    print(f"changed the index: {index}")

for i in blacklist_data:
    text += i + "\n"

path = blacklist
with open(path, "w", encoding="utf-8") as f:
    f.write(text)