mine = []
crab = []

with open("day22.txt", "r") as f:
    cards = list(f)
    mine = [int(x) for x in cards[1:26]]
    crab = [int(x) for x in cards[28:53]]

print(mine)
print(crab)

def play_game(mine, crab):

    history_mine = []
    history_crab = []

    while len(mine) > 0 and len(crab) > 0:

        for i, l in enumerate(history_mine):
            if mine == l and history_crab[i] == crab:

                return 1

        history_crab.append(crab[:])
        history_mine.append(mine[:])

        m = mine.pop(0)
        c = crab.pop(0)

        if m <= len(mine) and c <= len(crab):
            winner = play_game(mine[:m], crab[:c])
            if winner == 1:
                mine.append(m)
                mine.append(c)
            else:
                crab.append(c)
                crab.append(m)

        else:
            if m > c:
                mine.append(m)
                mine.append(c)
            else:
                crab.append(c)
                crab.append(m)

    #print(mine)
    #print(crab)

    if len(mine) == 0:
        return 2
    else:
        return 1

winner = []
if play_game(mine,crab) == 1:
    winner = mine
else:
    winner = crab

sum = 0
for i in range(1,len(winner)+1):
    sum += (winner[len(winner) - i]) * i

print(sum)


