
container = {}
with open("day07.txt", "r") as f:
    for line in f:
        words = line.split()
        container[words[0]+words[1]] = {}
        for i in range (4, len(words), 4):
            # print(f"container[{words[0]+words[1]}][{words[i+1]+words[i+2]}] = {words[i]}")
            if words[i] == 'no':
                container[words[0]+words[1]][words[i+1]+words[i+2]] = 0
            else:
                container[words[0]+words[1]][words[i+1]+words[i+2]] = int(words[i])



def checkcolor(color):

    bags = 0
    if color not in container:
        # print(f"{color} not in container")
        return 0

    for k in container[color].keys():
        bags += container[color][k] + (container[color][k] * checkcolor(k))

    return bags


print(checkcolor("shinygold"))
