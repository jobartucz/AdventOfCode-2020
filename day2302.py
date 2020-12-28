
cups = []
for c in "739862541":
    cups.append(int(c))
for c in range(8,1000001):
    cups.append(c)

current = 0
for i in range(10000):

    curr = cups[current]

    three = []
    for i in range(3):
        three.append(cups[(current + 1 + i)%len(cups)])
    for n in three:
        cups.remove(n)

    destination = curr - 1
    while destination not in cups:
        if destination == 0:
            destination = 1000000
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
        cups.append(cups.pop(0))
        tmp = cups[current]

    current = (current + 1) % 1000000

s = ""
print(cups[cups.index(1) + 1], cups[cups.index(1) + 2])