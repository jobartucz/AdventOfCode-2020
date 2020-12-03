
x = 0
trees = 0
with open("day03.txt", "r") as f:
    for line in f:
        line = line.strip()
        # print(line, x, line[x])
        if line[x] == '#':
            trees += 1
        x = (x + 3) % len(line)

print(trees)