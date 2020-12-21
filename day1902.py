
rules = {}
lines = []
dones = set()
maxlen = 0
with open("day1902.txt", "r") as f:
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
            line = line.strip()
            lines.append(line)
            if len(line) > maxlen:
                maxlen = len(line)

print(rules)
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
        third = ""
        if len(r) > 2:
            third = expand_rule(r[2])

        tmp = ""
        for g in first:
            tmp = g
            if second:
                for h in second:
                    if len(tmp + h) > maxlen:
                        continue
                    tmp += h
                    if third:
                        for i in third:
                            if len(tmp + i) > maxlen:
                                continue
                            tmp += i
                            newrules.append(tmp)
                            tmp = g + h
                    else:
                        newrules.append(tmp)
                    tmp = g
            else:
                newrules.append(tmp)

    rules[num] = newrules

    dones.add(num)
    return rules[num]


for i,r in enumerate(rules):
    expand_rule(i)

# print(rules)

num0 = 0
for l in lines:
    if l in rules[0]:
        num0 += 1

print(num0)