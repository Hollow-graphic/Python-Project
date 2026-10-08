import zipfile

zip_name = "Vithelpery"
zip_path = r"C:\Program Files (x86)\Steam\steamapps\common\Celeste\Mods" + "\\" + zip_name + ".zip"

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    with zip_ref.open("everest.yaml") as f:
        contenu = f.read().decode("utf-8")
        data = contenu
    
print(data)

data_split = data.split("\n")
prefix = [line for line in data_split if "Name" in line][1].split(": ")
depencies = [line[len(prefix[0])+2:] for line in data_split if line.startswith(prefix[0])]

print(depencies)