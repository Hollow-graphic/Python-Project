import colorsys
color = """
#0e0e0e
#0e2453
#0e2f5a
#0e466f
#0e556b
#0e0e0e
"""

color = [i[1:][:-1] for i in color.splitlines("\n") if i != "#000000\n"][1:]

def si(value):
    a = int(value, 16) /255
    return a

def rgb2hsl(value):
    c1 = value[:-4]
    c2 = value[2:][:-2]
    c3 = value[4:]
    hsl = colorsys.rgb_to_hls(si(c1), si(c2), si(c3))
    
    return hsl
    

hsl_color = [rgb2hsl(i) for i in color]

for i in hsl_color:
    c = ["","",""]
    c[0] = str((i[0] * 360).__round__())
    c[2] = str((i[1] * 100).__round__())
    c[1] = str((i[2] * 100).__round__())
    for i in range(len(c)):
        for j in range(3-len(c[i])):
            c[i] = "0" + c[i]
    
    print("          <color>"+c[0]+c[1]+c[2]+"</color>")