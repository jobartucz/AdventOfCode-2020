
numvalid = 0

with open("day0201.txt", "r") as f:
    for line in f:
        (nums, letter, pw) = line.split()
        mn,mx = nums.split('-')
        letter = letter[:-1]
        print(f"{mn}, {mx}, {letter}, {pw}")
        cnt = pw.count(letter)
        mn = int(mn)
        mx = int(mx)
        if cnt >= mn and cnt <= mx:
            numvalid += 1

print(f"numvalid: {numvalid}")
