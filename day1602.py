
goodtickets = []
yourticket = []
types = {}
possibilities = {}
notpossible = {}


def buildtickets():
    nums = set()
    global goodtickets
    global yourticket
    global types
    global possibilities, notpossible

    with open("day16.txt", "r") as f:
        for line in f:

            if line[0:4] == "your":
                yourticket = [int(x) for x in f.readline().split(',')]
                continue

            if ":" in line and line[-2] != ':':
                newset = set()
                type, ranges = line.split(': ')
                possibilities[type] = set()
                notpossible[type] = set()
                r1, r2 = ranges.split(' or ')
                r11, r12 = r1.split('-')
                r21, r22 = r2.split('-')
                for i in range(int(r11),int(r12) + 1):
                    nums.add(i)
                    newset.add(i)
                for i in range(int(r21),int(r22) + 1):
                    nums.add(i)
                    newset.add(i)
                types[type] = newset

            if "," in line:
                fields = [int(x) for x in line.split(",")]
                bad = False
                for i in fields:
                    if i not in nums:
                        bad = True
                        break
                if bad == False:
                    goodtickets.append(fields)

buildtickets()
# print(goodtickets)
# print(yourticket)
# print(types)


# make a list of all possibilities and all notpossibles
for t in goodtickets:
    for num, field in enumerate(t):
        # print(num, field)
        for type, range in types.items():
            if field in range:
                possibilities[type].add(num)
            else:
                notpossible[type].add(num)

# print(possibilities)
# print(notpossible)

# remove notpossibles from the possibilities
for k,v in notpossible.items():
    for n in v:
        possibilities[k].discard(n)

# print(possibilities)


# keep removing the ones that have only 1 possibility from the other sets
dones = {}
while (len(dones) < len(possibilities)):
    todo = []
    for k, v in possibilities.items():
        if k not in dones and len(v) == 1:
            todo.append(k)

    for t in todo:
        dones[t] = possibilities[t].pop()
        for k in possibilities.keys():
            if k != t:
                possibilities[k].discard(dones[t])

print(dones)

# finally, calculate the product
product = 1
for k, v in dones.items():
    if k[:9] == 'departure':
        product *= yourticket[v]
        # print(k, v)

print(product)