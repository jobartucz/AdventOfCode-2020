
numlist = {}

def writemem(addr, mask, start, val):
    global numlist

    newbval = addr[0:start]

    for i in range(start, 36):
        a = addr[i]
        m = mask[i]

        if m == '0':
            newbval += a
        elif m == '1':
            newbval += '1'
        else:
            writemem(newbval + '0' + addr[i+1:], mask, i + 1, val)
            writemem(newbval + '1' + addr[i+1:], mask, i + 1, val)
            return

    numlist[int(newbval,2)] = val

    return

with open("day14.txt", "r") as f:
    mask = ''
    for line in f:
        if line[:4] == 'mask':
                blah, mask = line.split(' = ')
        else:
            addr, val = line.split(' = ')
            addr = int(addr[addr.index('[') + 1 : addr.index(']')])
            val = int(val)

            # print(line, addr, val)
            baddr = bin(addr)[2:]

            for i in range(36-len(baddr)):
                baddr = '0' + baddr

            writemem(baddr, mask, 0, val)

sum = 0
for i in numlist.values():
    # print(i)
    sum += i

print(sum)
