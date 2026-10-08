from PIL import Image

im = Image.open(r"data\img\lol\items.png")
size = 900

new_im = Image.new('RGB', (64*size, 64))
temp_im = Image.new('RGB', (64, 64))

hash_list = []

x_offset = 0
for i in range(size):
    
    box = (i * 64, 0, (i + 1) * 64, 64)
    region = im.crop(box)
    
    temp_im.paste(region, (0, 0))
    temp = str(new_im.tobytes())
    if temp in hash_list: 
        x_offset += 1
        continue
    hash_list.append(temp)
    
    new_im.paste(region, (x_offset*64, 0))
    x_offset += 1

new_im.save('./data/img/lol/items_full_alt_alt_alt.png')