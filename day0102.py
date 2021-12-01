lines = []
num = 0
with open("day0100.txt", "r") as f:
    for line in f:
        lines.append(int(line))


prev = 99999999999999999999
for i in range(2, len(lines)):
    sum = lines[i-2] + lines[i-1] + lines[i]
    if (sum > prev):
        num += 1
    prev = sum

print(num)