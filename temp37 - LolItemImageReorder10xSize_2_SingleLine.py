from PIL import Image

im = Image.open(r"data\img\lol\items_full.png")
size = int(480/48 * 4320/48)

new_im = Image.new('RGBA', (48*size, 48))

x_offset = 0
for i in range(size):
    y_offset = 48*(i/10).__int__()
    box = (x_offset%480, y_offset, 48 + x_offset, 48 + y_offset)
    region = im.crop(box)
    new_im.paste(region, (x_offset, 0))
    x_offset += 48

new_im.save('./data/img/lol/items_full_alt.png')