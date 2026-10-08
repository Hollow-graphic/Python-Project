from pathlib import Path
import shutil

dir = r"\\169.254.148.143\Mods"
    
list_mod = [file.name for file in Path(dir).glob("*.zip")]
        
print(list_mod)
while True:
    input()
    for file in [file.name for file in Path(dir).glob("*.zip")]:
        if file not in list_mod:
            shutil.copy2(file, Path(r"C:\Program Files (x86)\Steam\steamapps\common\Celeste\Mods") / file)
            print(f"Added mod: {file}")