
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
loopc = 1
while trans(subc, loopc) != ck:
    loopc += 1

print(f"ck loop: {loopc}")

subd = 7
loopd = 1
while trans(subd, loopd) != dk:
    loopd += 1

print(f"dk loop: {loopd}")

secret = trans(trans(subd,loopd),loopc)

print(f"secret: {secret}")