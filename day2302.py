
def printcups(current, nums):
    print(f"({current}): ", end='')
    for i in range(9):
        print(current, end=' ')
        current = nums[current]
    print()

def printfinalcups(nums):

    current = nums[1]
    s = ""
    for i in range(9):
        s += str(current)
        current = nums[current]

    print(s)

    print(nums[1], nums[nums[1]])
    print(nums[1] * nums[nums[1]])


cups = []
for c in "739862541":
    cups.append(int(c))
for i in range(10,1000001):
    cups.append(i)

print(cups[:15])

nums = []
for i in range(1000001):
    nums.append(0)

for i, n in enumerate(cups):
    if i == 999999:
        nums[n] = cups[0]
    else:
        nums[n] = cups[i+1]

print(nums[0:20])
current = cups[0]
# printcups(current, nums)

for i in range(10000000):

    next = nums[current]
    nextnext = nums[next]
    nextnextnext = nums[nextnext]

    # print(f"pickup: {next}, {nextnext}, {nextnextnext}")

    dest = current - 1
    if dest == 0:
        dest = 1000000
    while dest == next or dest == nextnext or dest == nextnextnext:
        dest -= 1
        if dest == 0:
            dest = 1000000

    # print(f"dest: {dest}")

    # skip the three next cups
    nums[current] = nums[nextnextnext]

    # put the three cups after the destination
    nums[nextnextnext] = nums[dest]
    nums[dest] = next

    # go to the next one
    current = nums[current]

    # printcups(current, nums)

# print(nums)
printfinalcups(nums)