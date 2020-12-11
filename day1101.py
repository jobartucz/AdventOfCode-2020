
lines = []
with open("day11.txt", "r") as f:
    for line in f:
        lines.append(line)

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
            if i > 0:
                if j > 0:
                    if chart[i-1][j-1] == '#':
                        numoccupied += 1
                if chart[i-1][j] == '#':
                        numoccupied += 1
                if j < len(chart[0]) - 1:
                    if chart[i-1][j+1] == '#':
                        numoccupied += 1
            if i < len(chart)-1:
                if j > 0:
                    if chart[i+1][j-1] == '#':
                        numoccupied += 1
                if chart[i+1][j] == '#':
                        numoccupied += 1
                if j < len(chart[0]) - 1:
                    if chart[i+1][j+1] == '#':
                        numoccupied += 1
            if j > 0:
                if chart[i][j-1] == '#':
                    numoccupied += 1
            if j < len(chart[0]) - 1:
                if chart[i][j+1] == '#':
                    numoccupied += 1

            if chart[i][j] == 'L':
                if numoccupied == 0:
                    newchart[i] += '#'
                    changed = True
                else:
                    newchart[i] += 'L'

            if chart[i][j] == '#':
                if numoccupied >= 4:
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
