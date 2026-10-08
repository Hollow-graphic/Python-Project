import random

item_shop = ["check" + str(i+1) for i in range(10)]
buy_shop = [False for i in range(10)]
item_list = ["Bomb", "Heart+1", "2Heart Part"]

for i in range(4):  
    buy_shop[random.randint(0, 9)] = True

def gen_oBuble(arg0, nb):
    bool_list = [False for i in range(arg0)]
    for i in range(nb):
        a = random.randint(0, arg0-1)
        while bool_list[a]:
            a = random.randint(0, arg0-1)
        bool_list[a] = True
    
    items = []
    for i in range(arg0):
        if bool_list[i] and sum(buy_shop)!=len(buy_shop):
            a = random.randint(0, 9)
            while buy_shop[a]:
                a = random.randint(0, 9)
            items.append(item_shop[a])
        else:
            pass
    
    return items

for i in range(10):
    print(gen_oBuble(4, 2))