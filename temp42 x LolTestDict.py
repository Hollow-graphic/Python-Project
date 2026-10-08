function_list = {"getNewMatch":0, "getCurrentMatchStat":0, "getMatchStat":1}

while True:
    for i, function in enumerate(function_list): print(f"{i}: {function}")
    a = int(input())
    
    input_list = [input(f"{i}: ") for i in range(function_list[str(list(function_list)[a])])]
    eval(f"{list(function_list)[a]}({",".join(input_list)})")
