
letters = set()
count = 0

with open("day06.txt", "r") as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            count += len(letters)
            letters = set()
        else:
            for l in line:
                letters.add(l)

print(count)