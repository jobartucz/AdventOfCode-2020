
mine = []
crab = []

with open("day22.txt", "r") as f:
    cards = list(f)
    mine = [int(x) for x in cards[1:26]]
    crab = [int(x) for x in cards[28:53]]

print(mine)
print(crab)

while len(mine) > 0 and len(crab) > 0:
    m = mine.pop(0)
    c = crab.pop(0) 

    if m > c:
        mine.append(m)
        mine.append(c)
    else:
        crab.append(c)
        crab.append(m)

print(mine)
print(crab)

winner = []
if len(mine) == 0:
    winner = crab
else:
    winner = mine

sum = 0
for i in range(1,len(winner)+1):
    sum += (winner[len(winner) - i]) * i

print(sum)


