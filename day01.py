

def find2020():

    nums = []

    with open("day0101.txt", "r") as f:
        for line in f:
            nums.append(int(line))

    nums.sort()
    print(nums)

    # part 1:
    for i in nums:
        for j in nums:
            if i + j == 2020:
                print(i*j)
                # return

    # part 2:
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == 2020:
                    print(i*j*k)
                    # return

    if True == True:
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == 2020:
                print(nums[i]*nums[j])
                return
            if nums[i] + nums[j] < 2020:
                i += 1
            else:
                j -= 1
    
    print("No answer")

find2020()