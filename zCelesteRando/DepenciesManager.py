zip_name = "TempleOfTomorrow"

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
