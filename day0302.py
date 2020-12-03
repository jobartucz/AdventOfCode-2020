
a,b,c,d,e=0,0,0,0,0
trees = {'a':0,'b':0,'c':0,'d':0,'e':0}
counter = 0
with open("day03.txt", "r") as f:
    for line in f:
        line = line.strip()
        # print(line, x, line[x])
        if line[a] == '#':
            trees['a'] += 1
        a = (a + 1) % len(line)
        if line[b] == '#':
            trees['b'] += 1
        b = (b + 3) % len(line)
        if line[c] == '#':
            trees['c'] += 1
        c = (c + 5) % len(line)
        if line[d] == '#':
            trees['d'] += 1
        d = (d + 7) % len(line)
        if counter % 2 == 0:
            if line[e] == '#':
                trees['e'] += 1
            e = (e + 1) % len(line)
        counter += 1


print(trees['a'],trees['b'],trees['c'],trees['d'],trees['e'])
print(trees['a']*trees['b']*trees['c']*trees['d']*trees['e'])