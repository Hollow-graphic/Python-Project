import glob
from pathlib import Path
import os

dir = r"C:\Users\Adam\Desktop\Shortcut\Game\_Other"

data = [
    nom for nom in os.listdir(dir)
    if nom.endswith(".exe")
]
for i in data:
    os.removedirs(dir + r"\\" + i)
    print(i)

# import os

# dir = r"C:\Users\Adam\Desktop\Shortcut\Game\_Other"

# ban_file = ["UnityCrashHandler64.exe", 'handler.exe']

# data = [
#     nom for nom in os.listdir(dir)
#     if os.path.isdir(os.path.join(dir, nom))
# ]

# for i in data:
#     path = dir + "\\" + i
#     exe = [file for file in os.listdir(path) if file.endswith(".exe") and file not in ban_file]
#     if exe:
#         lien = path + ".exe"
#         cible = dir + r"\\" + i + r"\\" + exe[0]
#         command ="mklink /H \"" + lien + "\" \"" + cible + "\""
#         print(command)
#         os.system(command)