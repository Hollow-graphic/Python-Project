import os
import shutil
from pathlib import Path

dir = r"C:\\Users\\hollo\\Desktop\\GitHub\\Python-Project\\data\\bingo"

file_list = [file for file in Path(dir).glob("*.json")]

for i in range(len(file_list)):
    print(f"{i}: {file_list[i].name}")

select = file_list[int(input("select: "))]

print("----------")
print(select.name)
print("----------")

shutil.copy2(select, "./data/bingoTask.json")