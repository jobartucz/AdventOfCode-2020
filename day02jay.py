#start timer
import time
start_time = time.time()
#open up dataset
passdataunread = open('day0201.txt', 'r')
passdata = passdataunread.readlines()
passdataunread.close()
#dataset closed after reading to a list
#declare passlist so it is not a local variable
passlist = []
#append the line split out of data
for line in passdata:
    if line[-1] == '\n':
        passlist.append(line[:-1])
    else:
        passlist.append(line)
#split the data to only accesses parts we need
    #parsed data
        #both max an min letters
numlist = []
        #corrrupted passwords
mabypasses = []
        #minnimum amout of letters in pass
minletters = []
minletters1 = []
        #maximum amout of letters
maxletters = []
maxletters1 = []
        #unparsed letter to filter
whatletter1 = []
        #parsed letter to filter
whatletter = []
    #parses into chunks
numberofmatches = 0

for line in passlist:
        splited = line.split()
        numlist.append(splited[0])
        whatletter1.append(splited[1])
        mabypasses.append(splited[2])

    #parses further in
for line in numlist:
    splitednums = line.split('-')
    minletters.append(splitednums[0])
    maxletters.append(splitednums[1])

for line in whatletter1:
    whatletter.append(line[:-1])

for line in minletters:
    minletters1.append(int(line))

for line in maxletters:
    maxletters1.append(int(line))

# print(passlist)
# print(numlist)
# print(whatletter1)
# print(minletters)
# print(minletters1)
# print(mabypasses)

indexofsort = 0
for line in mabypasses:
        # indexofsort = mabypasses.index(line)
        amountof = line.count(whatletter[indexofsort])
        if amountof >= minletters1[indexofsort]:
            if amountof <= maxletters1[indexofsort]:
                numberofmatches = numberofmatches + 1
        indexofsort += 1


print(len(passlist))
print(numberofmatches)

print("\nMy program took", time.time() - start_time, "to run")