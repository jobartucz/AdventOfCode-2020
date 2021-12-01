lines = []
prev = 99999999999999999999
num = 0
with open("day0101.txt", "r") as f:
    for line in f:
        line = int(line)
        if line > prev:
            num+=1
        prev = line

print(num)