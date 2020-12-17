import collections
from typing import DefaultDict

universe = DefaultDict(bool)

with open("day17.txt", "r") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == "#":
                universe[(j,i,0,0)] = True

print(universe)

def findminmax(universe):
    minx, miny, minz, minw = 9999999,9999999,9999999,9999999
    maxx, maxy, maxz, maxw = -9999999,-9999999,-9999999,-9999999
    for (i,j,k,l) in universe.keys():
        if i < minx:
            minx = i
        if j < miny:
            miny = j
        if k < minz:
            minz = k
        if l < minw:
            minw = l
        if i > maxx:
            maxx = i
        if j > maxy:
            maxy = j
        if k > maxz:
            maxz = k
        if l > maxw:
            maxw = l

    return (minx, miny, minz, minw, maxx, maxy, maxz, maxw)

def shuffle(universe, iteration):
    newuniverse = DefaultDict(bool)

    (minx,miny,minz,minw,maxx,maxy,maxz,maxw) = findminmax(universe)

    for a in range(minx-1,maxx+2):
        for b in range(miny-1,maxy+2):
            for c in range(minz-1,maxz+2):
                for d in range(minw-1,maxw+2):
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

    (minx,miny,minz,minw,maxx,maxy,maxz,maxw) = findminmax(universe)

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