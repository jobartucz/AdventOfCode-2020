lines = [0]
with open("day10.txt", "r") as f:
    for line in f:
        lines.append(int(line))
    lines.sort()

lines.append(lines[-1] + 3)

numways = 1 #have to be able to do it using all

numwayswith = []
numwayswithout = []
for i in range(len(lines) + 2):
    numwayswith.append(1)
    numwayswithout.append(0)
numwayswith[len(lines) - 1] = 1

def checkways(nums):
    for i in range(len(lines) - 2, 0, -1):
        numwayswith[i] = numwayswith[i+1] + numwayswithout[i+1]
        if lines[i+1] - lines[i-1] < 4: # if it's possible to take this one out
            print(f"remove {lines[i]}")
            numwayswithout[i] += numwayswith[i+1]
            if lines[i+2] - lines[i-1] < 4: # if it's possible to take the next one out as well
                print(f"*** and {lines[i+1]}")
                numwayswithout[i] += numwayswithout[i+1] - numwayswithout[i+2]

    return numwayswith[1] + numwayswithout[1]

print(checkways(lines))
