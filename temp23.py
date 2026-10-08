# clay_stack = input()
# clay = input() + 64 * clay_stack

# each = 23

# print(clay/each)

import math

num = 2.66
count = 1

while num * count != math.floor(num * count):
    count += 1
    print(count)
    
print(count)