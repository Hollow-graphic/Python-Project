def array_push(a, b):
    return a.append(b)

def array_length(a):
    return len(a)

def floor(a):
    return a.__int__()

def random_range(a, b):
    import random
    return random.randrange(a, b)

def RND_step():
    return random_range(0, 1)

arg0 = [i for i in range(4)]
out = []
set_items = []
    
for i in range(len(arg0)):
    item_list = ["pickup_heart_heal,500,sPickupHeart,+1 HP", "pickup_heart2_heal,900,sPickupHeart2,+2 HP", "pickup_heartmax_heal,1500,sPickupHeartMax,+1 MAX HP", "pickup_heartsmall2_heal,800,sPickupHeartSmall2,+2 HP PARTS"]
    print("----")
    print(item_list)
    items_clean = []
        
    for j in range(len(item_list)):
        non_repeat = True
        
        for k in range(len(set_items)):
            if (item_list[j] == set_items[k]):
                non_repeat = False
        
        if (non_repeat):
            if (len(items_clean) <= 0):
                items_clean = [""]
                items_clean[0] = item_list[j]
            else:
                array_push(items_clean, item_list[j])
    
    total = len(items_clean)
    r = floor(total * RND_step())
    
    if (array_length(items_clean) <= 0):
        try:
            set_items[i] = "pickup_heart_heal,0,sItemError,SPAWN ERROR"
        except IndexError:
            set_items.append("pickup_heart_heal,0,sItemError,SPAWN ERROR")
    else:
        try:
            set_items[i] = items_clean[r]
        except IndexError:
            set_items.append(items_clean[r])

for i in range(len(arg0)):
    print(
        "item", set_items[i],
        "pool", arg0[i],
        "out[i]"
    )