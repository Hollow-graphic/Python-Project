from PIL import Image
images = [f"./data/img/lol/champion/{i}.png" for i in range(173)]
images = [Image.open(x) for x in images]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGBA', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset, 0))
  x_offset += im.size[0]

new_im.save('./data/img/lol/champion_full.png')