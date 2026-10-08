def printDir(dir):
    from pathlib import Path
    files = [file.name for file in Path(dir).glob("*")]
    char_list = ["├" for _ in range(len(files))]
    char_list[0] = "┬"
    char_list[-1] = "└"
    for i, value in enumerate(files):
        print(f"{char_list[i]}─{value}")

dir = r"C:\Users\Adam\AppData\Local\Microsoft\Windows\INetCache\IE\DZM1MZ1G"
printDir(dir)