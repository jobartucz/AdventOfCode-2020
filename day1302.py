
with open("day13.txt", "r") as f:
    starttime = int(f.readline())
    buses = [x for x in f.readline().split(',')]

times = {}
for i, b in enumerate(buses):
    if b != 'x':
        times[int(b)] = i

print(times)

found = False
starttime = 0
while found == False:

    found = True
    for time, delay in times.items():
        if (starttime + delay) % time != 0:
            found = False
            starttime += int(buses[0])
            break

if found == True:
    print(starttime)
else:
    print("how did I get here?")