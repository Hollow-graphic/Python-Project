def array_push(a, b):
    return a.append(b)

def array_length(a):
    return len(a)

def floor(a):
    return a.__int__()

def random_range(a, b):
    import random
    return random.randrange(a, b)

def split_string(a, b):
    return a.split(b)

#----

def isc(arg0, arg1, arg2):
    if (arg2 < arg1):
        temp = arg2
        arg2 = arg1
        arg1 = temp
    return arg0 >= arg1 and arg0 <= arg2

def zis(arg0, arg1):
    return arg0 in arg1

def wrap(arg0, arg1, arg2, arg3 = 1):
    diff = (arg2 - arg1) + arg3
    
    while (arg0 > arg2):
        arg0 -= diff
    
    while (arg0 < arg1):
        arg0 += diff
    
    return arg0

