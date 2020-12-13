lines = []
with open("day12.txt", "r") as f:
    for line in f:
        inst = line[0:1]
        amt = int(line[1:])
        lines.append((inst,amt))

position = (0,0)
waypoint = (10,1)
heading = 90

for inst, amt in lines:

    newpos = position
    if inst == 'E':
        newpos = (waypoint[0]+amt,waypoint[1])
        waypoint = newpos
    if inst == 'W':
        newpos = (waypoint[0]-amt,waypoint[1])
        waypoint = newpos
    if inst == 'N':
        newpos = (waypoint[0],waypoint[1]+amt)
        waypoint = newpos
    if inst == 'S':
        newpos = (waypoint[0],waypoint[1]-amt)
        waypoint = newpos
    if (inst == 'L' and amt == 90) or (inst == 'R' and amt == 270):
        newpos = (-1 * waypoint[1], waypoint[0])
        waypoint = newpos
    if (inst == 'R' and amt == 90) or (inst == 'L' and amt == 270):
        newpos = (waypoint[1], -1 * waypoint[0])
        waypoint = newpos
    if (inst == 'L' or inst == 'R') and amt == 180:
        newpos = (-1 * waypoint[0], -1 * waypoint[1])
        waypoint = newpos
    if inst == 'F':
        newpos = (position[0] + (waypoint[0] * amt),position[1] + (waypoint[1] * amt))
        position = newpos

    print(position, waypoint)

print(abs(position[0])+abs(position[1]))
