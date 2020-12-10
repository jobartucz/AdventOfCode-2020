
lines = []
with open("day09.txt", "r") as f:
    for line in f:
        lines.append(int(line))

def validate(sum, nums):
    i = 0
    j = len(nums) - 1
    nums.sort()
    while i < j:
        if nums[i] + nums[j] == sum:
            return True
        if nums[i] + nums[j] < sum:
            i += 1
        else:
            j -= 1

    print(f"No answer for {sum}")
    return False

def findsum(num):
    for i in range(len(lines) - 1):
        sum = lines[i]
        smallest = lines[i]
        largest = lines[i]
        for j in range(i+1, len(lines)):
            if lines[j] < smallest:
                smallest = lines[j]
            if lines[j] > largest:
                largest = lines[j]
            sum += lines[j]
            if sum == num:
                print(f"Found: {smallest} {largest} = {smallest + largest}")
                return
            if sum > num:
                break

invalid = 0
for i in range(25, len(lines)):
    if validate(lines[i],lines[i-25:i]) == False:
        invalid = lines[i]
        break

findsum(invalid)

