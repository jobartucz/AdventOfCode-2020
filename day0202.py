
numvalid = 0

with open("day0201.txt", "r") as f:
    for line in f:
        (nums, letter, pw) = line.split()
        mn,mx = nums.split('-')
        letter = letter[:-1]
        mn = int(mn) - 1 # using 1 index :(
        mx = int(mx) - 1 # using 1 index :(
        if mx < len(pw):
            if pw[mn] == letter and pw[mx] != letter:
                numvalid += 1
                print(f"{mn}, {mx}, {letter}, {pw}")

            if pw[mn] != letter and pw[mx] == letter:
                numvalid += 1
                print(f"{mn}, {mx}, {letter}, {pw}")


print(f"numvalid: {numvalid}")
