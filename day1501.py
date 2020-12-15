pos = {14:0,8:1,16:2,0:3,1:4}
num = 17
for i in range(5,30000000 - 1):
    oldnum = num
    if num in pos:
        num = i - pos[num]
    else:
        num = 0
    pos[oldnum] = i
print(num)
