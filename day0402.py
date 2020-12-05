
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
    # print(pp)
    fields = pp.split()
    valid = 1
    if len(fields) < 7:
        valid = 0
    elif len(fields) < 8:
        for field in fields:
            if field[:4] == 'cid:':
                valid = 0
    if valid == 0:
        continue

    for field in fields:
        key, val = field.split(":")
        # print(key, val)

        if key == "byr" and (int(val) < 1920 or int(val) > 2002):
            valid = 0
        if key == "iyr" and (int(val) < 2010 or int(val) > 2020):
            valid = 0
        if key == "eyr" and (int(val) < 2020 or int(val) > 2030):
            valid = 0
        if key == "hgt":
            if val[-2:] == "cm":
                if int(val[:-2]) < 150 or int(val[:-2]) > 193:
                    valid = 0
            elif val[-2:] == "in":
                if int(val[:-2]) < 59 or int(val[:-2]) > 76:
                    valid = 0
            else:
                valid = 0
        if key == "hcl":
            if val[0] != '#':
                valid = 0
            for l in val[1:]:
                if l not in '0123456789abcdef':
                    valid = 0
        if key == "ecl":
            if val not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                valid = 0
        if key == "pid":
            if len(val) != 9:
                valid = 0
            else:
                for l in val:
                    if l not in '0123456789':
                        valid = 0

    if valid == 1:
        print(pp)
    numvalid += valid


print(numvalid)

