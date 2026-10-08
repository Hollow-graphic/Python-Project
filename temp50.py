from pathlib import Path

dir = r"C:\Users\Adam\AppData\Local\Microsoft\Windows\INetCache\IE"

for file in Path(dir).glob("*"):
    print("--: " + file.name)
    for fjle in Path(file).glob("*"):
        print(fjle.name)
        
