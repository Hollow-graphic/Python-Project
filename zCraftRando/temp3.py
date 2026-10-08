import json

content = str(b'{\n  "type": "minecraft:crafting_shaped",\n  "category": "building",\n  "group": "stained_terracotta",\n  "key": {\n    "#": {\n      "item": "minecraft:terracotta"\n    },\n    "X": {\n      "item": "minecraft:yellow_dye"\n    }\n  },\n  "pattern": [\n    "###",\n    "#X#",\n    "###"\n  ],\n  "result": {\n    "count": 8,\n    "item": "minecraft:yellow_terracotta"\n  },\n  "show_notification": true\n}')

items = [i.split('"\\n')[0] for i in content.split('    "item": "')][1:]
ingredients = items[:-1]
result = items[-1]

print(ingredients)
print(result)
