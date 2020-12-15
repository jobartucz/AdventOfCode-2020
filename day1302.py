
with open("day13test.txt", "r") as f:
    starttime = int(f.readline())
    buses = f.readline().split(',')

times = {}
for i, b in enumerate(buses):
    if b != 'x':
        times[int(b)] = i

print(times)

found = False
starttime = 0
adder = 0
for time, delay in times.items():
    adder += time
    while starttime + :

    found = True
    # print(starttime)
        if (starttime + delay) % time != 0:
            found = False
            starttime += 17
            break

if found == True:
    print(starttime)
else:
    print("how did I get here?")