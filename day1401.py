
numlist = {}

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
            bval = bin(val)[2:]

            for i in range(36-len(bval)):
                bval = '0' + bval

            newbval = ''
            for i, c in enumerate(bval):
                if mask[i] == '0':
                    newbval += '0'
                elif mask[i] == '1':
                    newbval += '1'
                else:
                    newbval += c
            numlist[addr] = newbval

sum = 0
for i in numlist.values():
    print(i)
    sum += int(i,2)

print(sum)
