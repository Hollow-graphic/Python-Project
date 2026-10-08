import requests
from PIL import Image

data = requests.get(f"https://static-cdn.leagueofgraphs.com/www/img/d/sprites/16.17/small_items0.png?v=1787858543")

new_im = Image.new('RGB', (480, 480))

new_im.paste(data, (0, 0))

new_im.save('./data/img/lol/temp.png')
