
ins = [] # instructions
ams = [] # amounts
dones = [] # whether we've run this instruction before

with open("day08.txt", "r") as f:
    for line in f:
        instruction, amount = line.split()
        ins.append(instruction)
        ams.append(int(amount))
        dones.append(False)
    ins.append("don")
    ams.append(0)
    dones.append(False)

# print(ins, ams)

def runit(ins, ams, dones):
    accumulator = 0
    for i in range(len(dones)):
        dones[i] = False

    i = 0
    while(True):
        if ins[i] == "don":
            print(f"done with accumulator: {accumulator}")
            return True
        if dones[i]:
            # print(f"loop at {i}")
            return False
        dones[i] = True
        if ins[i] == "nop":
            i += 1
            continue
        elif ins[i] == "acc":
            accumulator += ams[i]
        elif ins[i] == "jmp":
            i += ams[i]
            continue
        else:
            print("oh crap")

        i += 1

    print("nothing")
    return False

for i in range(len(ins)):

    if ins[i] == "jmp":
        ins[i] = "nop"
        if runit(ins, ams, dones):
            break
        ins[i] = "jmp"

    if ins[i] == "nop":
        ins[i] = "jmp"
        if runit(ins, ams, dones):
            break
        ins[i] = "nop"
