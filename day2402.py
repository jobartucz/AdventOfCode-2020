
with open ("day24.txt", "r") as f:
    lines = [x.strip() for x in list(f)]

blacks = set()

for l in lines:
    i = 0
    x, y = 0, 0
    while i < len(l):
        if l[i] == 'e':
            x += 1
            i += 1
        elif l[i] == 'w':
            x -= 1
            i += 1
        elif l[i] == 's':
            y -= 1
            if l[i+1] == 'e':
                x += 1
            else:
                x -= 0
            i += 2
        elif l[i] == 'n':
            y += 1
            if l[i+1] == 'w':
                x -= 1
            else:
                x -= 0
            i += 2
    if (x,y) in blacks:
        blacks.remove((x,y))
    else:
        blacks.add((x,y))

newblacks = set()
def checkwhite(x,y):
    global blacks, newblacks
    sum = 0
    if (x,y) in newblacks:
        return
    for (a,b) in [(x-1,y),(x+1,y),(x,y-1),(x+1,y-1),(x-1,y+1),(x,y+1)]:
        if (a,b) in blacks:
            sum += 1
    if sum == 2:
        newblacks.add((x,y))

def checkblack(x,y):
    global blacks, newblacks
    sum = 0
    for (a,b) in [(x-1,y),(x+1,y),(x,y-1),(x+1,y-1),(x-1,y+1),(x,y+1)]:
        if (a,b) in blacks:
            sum += 1
        else:
            checkwhite(a,b)
    if sum == 0 or sum > 2:
        newblacks.remove((x,y))


for i in range(101):
    print(f"{i}: {len(blacks)}")
    newblacks = set(blacks)
    for (x,y) in blacks:
        checkblack(x,y)
    blacks = newblacks
