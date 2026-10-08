# Source - https://stackoverflow.com/a/30228308
# Posted by dting, modified by community. See post 'Timeline' for change history
# Retrieved 2026-08-30, License - CC BY-SA 4.0

# Changed to be vertical and get a automatic list of image from a dir

from PIL import Image
images = [f"./data/img/lol/item/{i}.png" for i in range(15)]
images = [Image.open(x) for x in images]
widths, heights = zip(*(i.size for i in images))

total_width = max(widths)
max_height = sum(heights)

new_im = Image.new('RGBA', (total_width, max_height))

y_offset = 0
for im in images:
  new_im.paste(im, (0, y_offset))
  y_offset += im.size[1]

new_im.save('./data/img/lol/items_full.png')
