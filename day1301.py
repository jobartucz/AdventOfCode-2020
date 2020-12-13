
with open("day13.txt", "r") as f:
    starttime = int(f.readline())
    buses = [int(x) for x in f.readline().split(',') if x != 'x']

# print(starttime, buses)

times = [x - (starttime % x) for x in buses]
mindex = times.index(min(times))

print(times[mindex] * buses[mindex])
