
maxid = 0

seatids = set()

with open("day05.txt", "r") as f:
    for line in f:
        fb = 64
        row = 0
        rl = 4
        col = 0

        for c in line[0:7]:
            if c == "B":
                row += fb
            fb = fb // 2
        for c in line[7:]:
            if c == "R":
                col += rl
            rl = rl // 2

        id = row * 8 + col
        seatids.add(id)
        # print(f"{row} {col}")
        if id > maxid:
            maxid = id

print(maxid)
for id in seatids:
    if id + 2 in seatids and id + 1 not in seatids:
        print(id + 1)

