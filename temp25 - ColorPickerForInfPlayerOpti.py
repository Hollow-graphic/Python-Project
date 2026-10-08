import math

sphere = 1

for index in range(12,24):
    a = index
    for i in range(3):
        a = (a+1)>>1
    b = (index+1)>>1
    print(index, a, b)
    
    
    
def getColor(id):
    if id <= 6:
        return color[id-1]
    else:
        angle = 0
        sphere = ((id-1)//6).bit_length()
        index = math.floor((id - 3*2**sphere)/2 + 0.5) + (3*2**sphere)/2 * (not id % 2)
        
        for i in range(sphere):
            angle += (2*(index%2 == 0)-1) * 30/(2**(sphere-i-1))
            index = (math.floor(index + 1 * (index % 2)))/2
        return angle+color[3+index.__round__()-1]