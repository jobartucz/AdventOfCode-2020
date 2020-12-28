
ck = 15628416
dk = 11161639

if False:
    ck = 5764801
    dk = 17807724

def trans(sub, loop):

    ans = 1
    for i in range(loop):
        ans = (ans * sub) % 20201227

    return ans


subc = 7
ans = 1
loopc = 0
while ans != ck:
    loopc += 1
    ans = (ans * subc) % 20201227

print(f"ck loop: {loopc}")

subd = 7
loopd = 0
ans = 1
while ans != dk:
    loopd += 1
    ans = (ans * subd) % 20201227

print(f"dk loop: {loopd}")

secret = trans(trans(subd,loopd),loopc)

print(f"secret: {secret}")