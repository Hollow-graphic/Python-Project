import json

with open("./data/temp.txt", "r", encoding="utf-8") as f:
    data = f.read().split("\n")

name = [line[21:][:-2].replace("\"","") for line in data if line.startswith("            name_set(")]
text = [line[17:][:-2].replace("\"","") for line in data if line.startswith("            text(")]

for i in range(len(name)):
    if name[i] == "":
        name[i] = "narrator"

messages = []
for i in range(len(name)):
    _ = f"{name[i]}: {text[i]}"
    print(_)
    messages.append({"role": "assistant", "content": _})

with open("./data/vivid.json", "w", encoding="utf-8") as f:
    json.dump(messages, f, ensure_ascii=False, indent=2)
