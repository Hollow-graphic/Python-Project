
preset = r"./zCelesteRando/data/preset.txt"
blacklist = r"C:\Program Files (x86)\Steam\steamapps\common\Celeste\Mods\blacklist.txt"
depencies = r"./zCelesteRando/data/depencies.txt"

reset = False

with open(preset, "r", encoding="utf-8") as f:
    preset_data =  f.read().split("\n")
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











# blacklist_index_list = [index+4 for index, line in enumerate(blacklist_data_split) if line.startswith("#")]
# for i in blacklist_index_list: print(i)
# print(len(mods_list))

# last = 0
# for i in range(len(mods_list)):
#     if mods_list[i] not in (preset_data + depencies_data):
#         print(f"{blacklist_index_list[i]}: {mods_list[i]}")
#         previous = blacklist_index_list[i-1] if i > 0 else 0
#         start = sum(len(ligne) + 1 for ligne in blacklist_data_split[:blacklist_index_list[i] + previous - 1])
#         last = start - 2
#         blacklist_data = blacklist_data[:start] + blacklist_data[start + 2:]