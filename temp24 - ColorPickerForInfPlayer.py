import math

color = [0, 240, 120, 60, 180, 300]

def getColor(id):
    if id <= 6:
        return color[id-1]
    else:
        angle = 0
        sphere = ((id-1)//6).bit_length()
        index = ((id-3*(1<<sphere)+1)>>1) + (((3*(1<<sphere))>>1) if (id&1==0) else 0)
        for i in range(sphere):
            angle += (1 if (index&1==0) else -1) * 30/(1<<(sphere-i-1))
            index = (index+1)>>1
        return angle+color[2+index]

def angle(id):
    if id <= 6:
        return color[id-1]
    else:
        angle = 0
        sphere = ((id-1)//6).bit_length()
        index = ((id-3*(1<<sphere)+1)>>1) + (((3*(1<<sphere))>>1) if (id&1==0) else 0)
        for i in range(sphere):
            angle += (1 if (index&1==0) else -1) * 30/(1<<(sphere-i-1))
            index = (index+(index&1))>>1
        return angle+color[2+index]

count = 0
for i in range(1,20):
    print(angle(i), getColor(i))
    count += (angle(i) == getColor(i))
print(count==len(range(1,20)))