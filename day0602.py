
letters = set()
count = 0
start = True
with open("day06.txt", "r") as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            count += len(letters)
            letters = set()
            start = True
        else:
            newletters = set()
            for l in line:
                newletters.add(l)

            if start == True:
                letters = set(newletters)
                start = False
            else:
                letters.intersection_update(newletters)

print(count)