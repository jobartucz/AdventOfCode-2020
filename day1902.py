
rules = {}
lines = []
dones = set()
with open("day19.txt", "r") as f:
    for line in f:
        if len(line) > 2 and line.find(":") > 0:
            num, rule = line.strip().split(': ')
            if rule == '"a"':
                rules[int(num)] = ['a']
                dones.add(int(num))
            elif rule == '"b"':
                rules[int(num)] = ['b']
                dones.add(int(num))
            else:
                tmp = [x.strip().split(' ') for x in rule.split('|')]
                rules[int(num)] = [[int(x) for x in y] for y in tmp]
        elif len(line) > 1:
            lines.append(line.strip())

# print(rules)
def expand_rule(num):
    global rules

    if num in dones:
        return rules[num]

    newrules = []
    for i, r in enumerate(rules[num]):
        first = expand_rule(r[0])
        second = ""
        if len(r) > 1:
            second = expand_rule(r[1])

        tmp = ""
        for g in first:
            tmp = g
            if second:
                for h in second:
                    tmp += h
                    newrules.append(tmp)
                    tmp = g
            else:
                newrules.append(tmp)

    rules[num] = newrules

    dones.add(num)
    return rules[num]

expand_rule(42)
expand_rule(31)

print(len(lines))
chars = len(rules[42][0])
for l in list(lines):
    if len(l) % chars != 0:
        # print("++++++++++++++++++++++++++++++++++++")
        lines.remove(l)
        continue

    if l[:chars] not in rules[42] or l[chars:chars + chars] not in rules[42] or l[-1*chars:] not in rules[31]:
        # print("-------------------------------------")
        lines.remove(l)
        continue

    num42s = 0
    num31s = 0

    fortytwos = True
    remove = False
    s = ''
    for i in range(0,len(l),chars):
        if fortytwos == True:
            if l[i:i+chars] in rules[42]:
                num42s += 1
                s += "42_"
                continue
            elif l[i:i+chars] in rules[31]:
                s += "31_"
                num31s += 1
                fortytwos = False
            else:
                s += l[i:i+chars] + " not 42 or 31 when it should be"
                remove = True
                break
        elif l[i:i+chars] not in rules[31]:
            s += l[i:i+chars] + " not 31 when it should be"
            remove = True
            break
        else:
            s += "31_"
            num31s += 1

    if remove == True:
        # print(s + " ------------ REMOVED")
        lines.remove(l)
    elif num31s == 0 or num31s >= num42s:
        # print(s + "BAD31REMOVED")
        lines.remove(l)
    # else:
        # print(f"KEPT: {num42s} {num31s}")

print()
#for l in lines:
#    print(l)

print(len(lines))
