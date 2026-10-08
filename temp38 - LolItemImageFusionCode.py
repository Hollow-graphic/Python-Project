import requests
from PIL import Image

# for i in range(15):
#     data = requests.get(f"https://static-cdn.leagueofgraphs.com/www/img/d/sprites/16.17/item{i}.png?v=1787858543")
#     data.raise_for_status()
#     with open(f"./data/img/lol/items_{i}.png", "wb") as f:
#         f.write(data.content)

#////////////////////////#

images = [f"./data/img/lol/items_{i}.png" for i in range(15)]
images = [Image.open(x) for x in images]
widths, heights = zip(*(i.size for i in images))

total_width = max(widths)
max_height = sum(heights)

new_im = Image.new('RGB', (total_width, max_height))

y_offset = 0
for im in images:
  new_im.paste(im, (0, y_offset))
  y_offset += im.size[1]
  print("- paste image")

new_im.save('./data/img/lol/items_full.png')

print("Finish Vertical Image")
#////////////////////////#

im = new_im
#bool = "11111111111011100111111111110000001110111000000000000000001110000000000000000000000000100001111110010101111100000000000011111111000000000000000000111111111111011111010111111111111111111111111111111111111111111111111111111111101111101111111111111111111011111111111101111111111111111111111011110011010110000000100011101111101100010111111101111111111111111111111111111111111111111111111011111001111111111111111111111111111011110111111111111111111111111111110100110000110001111110000000000000111111100011111100000010100000000000010100011101111100100000001000000000101111100001111110000000000111111110000001100000011011111111000111100001111111101000000000000000000000000000000000000000000011000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
check_list = []

new_im = Image.new('RGB', (48*max_height, 48))
temp_im = Image.new('RGB', (48, 48))

x_offset = 0
for i in range(int(max_height/4.8)):
    print(f"- start {i}")
    #if bool[i] == "0": continue
    
    y_offset = 48*(i//10)
    box = (x_offset%10*48, y_offset, 48*(x_offset+1), 48 + y_offset)
    region = im.crop(box)
    
    temp_im = region.convert("RGB")
    if temp_im in check_list: 
        x_offset += 1
        print("- removed")
        continue
    check_list.append(temp_im)
    print("- pasted")
    
    new_im.paste(region, (x_offset*48, 0))
    x_offset += 1

new_im.save('./data/img/lol/items_full_ultra.png')