
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

print(len(blacks))