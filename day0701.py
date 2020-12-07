
container = {}
with open("day07.txt", "r") as f:
    for line in f:
        words = line.split()
        container[words[0]+words[1]] = {}
        for i in range (4, len(words), 4):
            # print(f"container[{words[0]+words[1]}][{words[i+1]+words[i+2]}] = {words[i]}")
            container[words[0]+words[1]][words[i+1]+words[i+2]] = words[i]
            if words[i] == 'no':
                container[words[0]+words[1]][words[i+1]+words[i+2]] = 0

numcolors = 0
donecolors = {}
def checkcolor(color):
    global numcolors, container
    # print(f"checking {color}")
    if color == "shinygold":
        # print("\n")
        return 1
    
    if color in donecolors:
        return donecolors[color]

    if color in container:
        for k in container[color].keys():
            if checkcolor(k) == 1:
                donecolors[color] = 1
                numcolors += 1
                return 1

    donecolors[color] = 0
    return 0


for k in container.keys():
    checkcolor(k)

print(numcolors)