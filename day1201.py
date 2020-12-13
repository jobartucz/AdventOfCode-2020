lines = []
with open("day12.txt", "r") as f:
    for line in f:
        inst = line[0:1]
        amt = int(line[1:])
        lines.append((inst,amt))

position = (0,0)
heading = 90

for inst, amt in lines:

    newpos = position
    if inst == 'E' or (heading == 90 and inst == 'F'):
        newpos = (position[0]+amt,position[1])
    if inst == 'W' or (heading == 270 and inst == 'F'):
        newpos = (position[0]-amt,position[1])
    if inst == 'N' or (heading == 0 and inst == 'F'):
        newpos = (position[0],position[1]+amt)
    if inst == 'S' or (heading == 180 and inst == 'F'):
        newpos = (position[0],position[1]-amt)
    if inst == 'L':
        heading = (heading - amt) % 360
    if inst == 'R':
        heading = (heading + amt) % 360

    position = newpos
    # print(position, heading)

print(abs(position[0])+abs(position[1]))
