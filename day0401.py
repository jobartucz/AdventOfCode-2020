
passports = []

with open("day0401.txt", "r") as f:
    thisline = ""
    for line in f:
        line = line.strip()
        if len(line) == 0:
            passports.append(thisline)
            thisline = ""
        else:
            thisline = thisline + ' ' + line

numvalid = 0
for pp in passports:
    print(pp)
    fields = pp.split()
    valid = 1
    if len(fields) < 7:
        valid = 0
    elif len(fields) < 8:
        for field in fields:
            if field[:4] == 'cid:':
                valid = 0
    numvalid += valid

print(numvalid)

