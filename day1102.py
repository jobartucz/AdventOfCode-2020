
lines = []
with open("day11.txt", "r") as f:
    for line in f:
        lines.append(line)

def checkdirection(x,y,x1,y1):
    global lines
    if x1 == -1:
        endx = -1
    else:
        endx = len(lines[0])
    if y1 == -1:
        endy = -1
    else:
        endy = len(lines)


    x += x1
    y += y1
    while x != endx and y != endy:
        if lines[y][x] != '.':
            return lines[y][x]
        x += x1
        y += y1

    return '.'


changed = True
def fillseats(chart):
    global changed
    changed = False
    newchart = []
    for i in range(len(chart)):
        newchart.append("")
        for j in range(len(chart[0])):
            numoccupied = 0
            if chart[i][j] == '.':
                newchart[i] += '.'
                continue

            for r in [-1,0,1]:
                for s in [-1, 0, 1]:
                    if r == 0 and s == 0:
                        continue
                    if checkdirection(j,i,r,s) == '#':
                        numoccupied += 1


            if chart[i][j] == 'L':
                if numoccupied == 0:
                    newchart[i] += '#'
                    changed = True
                else:
                    newchart[i] += 'L'

            if chart[i][j] == '#':
                if numoccupied >= 5:
                    newchart[i] += 'L'
                    changed = True
                else:
                    newchart[i] += '#'

    return newchart

while (changed == True):
    lines = fillseats(lines)

counter = 0
for l in lines:
    counter += l.count('#')

print(counter)
