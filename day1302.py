
with open("day13test.txt", "r") as f:
    starttime = int(f.readline())
    buses = f.readline().split(',')

times = {}
for i, b in enumerate(buses):
    if b != 'x':
        times[int(b)] = i

# print(times)

found = False
starttime = 0
while found == False:

    found = True
    # print(starttime)
    for time, delay in times.items():
        if (starttime + delay) % time != 0:
            found = False
            starttime += 17
            break

with open("day13solution.txt", "w") as f:
    if found == True:
        f.write(str(starttime))
    else:
        f.write("how did I get here?")