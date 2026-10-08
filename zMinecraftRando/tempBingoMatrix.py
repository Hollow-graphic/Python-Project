import random


matrix = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

for i in range(5):
    for j in range(5):
        matrix[i][j] = random.randint(0,1)



def verify(m):
    # X axis
    for i in range(5):
        if m[i][0] and m[i][1] and m[i][2] and m[i][3] and m[i][4]:
            return True
    # Y Axis
    for i in range(5):
        if m[0][i] and m[1][i] and m[2][i] and m[3][i] and m[4][i]:
            return True
    # Diagonal
    if m[0][0] and m[1][1] and m[2][2] and m[3][3] and m[4][4]:
            return True
    if m[0][4] and m[1][3] and m[2][2] and m[3][1] and m[4][0]:
            return True
        
    return False

for i in range(5):
    print(matrix[i])
print(verify(matrix))