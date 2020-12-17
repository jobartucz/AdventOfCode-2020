import collections
from typing import DefaultDict

universe = DefaultDict(bool)

with open("day17.txt", "r") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == "#":
                universe[(j,i,0,0)] = True

print(universe)

def shuffle(universe, iteration):
    newuniverse = DefaultDict(bool)

    for a in range(0-iteration,8+iteration):
        for b in range(0-iteration,8+iteration):
            for c in range(0-iteration,8+iteration):
                for d in range(0-iteration,8+iteration):
                    numtrue = 0
                    for i in range(-1,2):
                        for j in range(-1,2):
                            for k in range(-1,2):
                                for l in range(-1,2):
                                    if i == 0 and j == 0 and k == 0 and l == 0:
                                        continue
                                    if universe[(a+i,b+j,c+k,d+l)]:
                                        numtrue += 1
                    if universe[(a,b,c,d)]:
                        if numtrue == 2 or numtrue == 3:
                            newuniverse[(a,b,c,d)] = True
                    else:
                        if numtrue == 3:
                            newuniverse[(a,b,c,d)] = True

    return newuniverse

def printu(universe, extracounter):
    minx, miny, minz = 9999999,9999999,9999999
    maxx, maxy, maxz = -9999999,-9999999,-9999999
    for (i,j,k,l) in universe.keys():
        if i < minx:
            minx = i
        if j < miny:
            miny = j
        if k < minz:
            minz = k
        if i > maxx:
            maxx = i
        if j > maxy:
            maxy = j
        if k > maxz:
            maxz = k

    print('')
    print(minx,miny,minz,maxx,maxy,maxz)
    for z in range(minz,maxz+1):
        print(f"z: {z}")
        for y in range(miny,maxy+1):
            for x in range(minx,maxx+1):
                if universe[(x,y,z,0)]:
                    print("#", end='')
                else:
                    print('.',end='')
            print('')

printu(universe,0)
for mycounter in range(1,7):
    universe = shuffle(universe,mycounter)
    #printu(universe,mycounter)

starcounter = 0
for k in universe.keys():
    if universe[k]:
        starcounter += 1
print(starcounter)