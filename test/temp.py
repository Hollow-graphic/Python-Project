Options = open("Options.txt", "r").read().splitlines()
Values = open("Values.txt", "r").read().splitlines()

for i in range(len(Options)):
    print(Options[i]+"|"+Values[i])
