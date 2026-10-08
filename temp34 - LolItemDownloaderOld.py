import requests

for i in range(20):
    data = requests.get(f"https://static-cdn.leagueofgraphs.com/www/img/d/sprites/16.17/small_items{i}.png?v=1787858543")
    data.raise_for_status()
    with open(f"./data/img/lol/arena_augment_{i}.png", "wb") as f:
        f.write(data.content)

print(data)