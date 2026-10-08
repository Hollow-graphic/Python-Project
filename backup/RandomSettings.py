import xml.etree.ElementTree as ET
import random

file = r"C:\Program Files (x86)\Steam\steamapps\common\Celeste\Saves\settings.celeste"

Keys = [
    "A","Z","E","R","T","Y","U","I","O","P",
    "Q","S","D","F","G","H","J","K","L","M",
    "W","X","C","V","B","N"
]
settings_list = [
    "Left", "Right", "Up", "Down",
    "Jump", "Grab", "Dash", "DemoDash",
]

tree = ET.parse(file)
root = tree.getroot()

random.shuffle(Keys)

for i in range(len(settings_list)):
    root.find(settings_list[i]+"/Keyboard/Keys").text = Keys[i]
    
print(f"Left: {Keys[0]}   Right: {Keys[1]}")
print(f"Up:   {Keys[2]}   Down: {Keys[3]}")
print(f"Jump: {Keys[4]}   Grab: {Keys[5]}")
print(f"Dash: {Keys[6]}   DemoDash: {Keys[7]}")

ET.indent(tree, space="  ")
tree.write(
    file,
    encoding="utf-8",
    xml_declaration=True
)

while True:
    pass
    