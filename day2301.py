
cups = []
for c in "739862541":
    cups.append(int(c))

current = 0
for i in range(100):

    curr = cups[current]

    three = []
    for i in range(3):
        three.append(cups[(current + 1 + i)%len(cups)])
    for n in three:
        cups.remove(n)

    destination = curr - 1
    while destination not in cups:
        if destination == 0:
            destination = 9
        else:
            destination -= 1

    # insert the cups after the destination cup
    i = cups.index(destination)
    for n in three:
        cups.insert((i+1),n)
        i += 1

    # rotate to make sure the current cup is still in the correct position
    tmp = cups[current]
    while curr != tmp:
        cups.insert(0,cups.pop())
        tmp = cups[current]

    current = (current + 1) % 9

s = ""
s = s.join([str(x) for x in cups[cups.index(1)+1:]]) + s.join([str(x) for x in cups[0:cups.index(1)]])
print(s)