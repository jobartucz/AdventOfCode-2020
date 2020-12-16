
nums = set()
bads = 0
with open("day16.txt", "r") as f:
    for line in f:

        if line[0:4] == "your":
            yourticket = f.readline()
            continue

        if ":" in line and line[-2] != ':':
            type, ranges = line.split(': ')
            r1, r2 = ranges.split(' or ')
            r11, r12 = r1.split('-')
            r21, r22 = r2.split('-')
            for i in range(int(r11),int(r12) + 1):
                nums.add(i)
            for i in range(int(r21),int(r22) + 1):
                nums.add(i)

        if "," in line:
            fields = [int(x) for x in line.split(",")]
            for i in fields:
                if i not in nums:
                    bads += i

print(bads)