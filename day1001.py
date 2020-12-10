lines = [0]
with open("day10.txt", "r") as f:
    for line in f:
        lines.append(int(line))
    lines.sort()

ones, threes = 0,1
for i in range(len(lines) - 1):
    if lines[i+1] - lines[i] == 1:
        ones += 1
    if lines[i+1] - lines[i] == 3:
        threes += 1


print(lines)
print(ones, threes, ones*threes)