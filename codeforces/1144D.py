n = int(input())
nums = list(map(int, input().split()))

count = dict()

# [count,0 based indices]
for i in range(n):
    if nums[i] in count.keys():
        count[nums[i]][0] += 1
        count[nums[i]].append(i)
    else:
        count[nums[i]] = [1]
        count[nums[i]].append(i)

# Initialise values
currCount = 1
currElem = nums[0]
currInd = [0]

for key in count.keys():
    if count[key][0] > currCount:
        currCount = count[key][0]
        currElem = key
        currInd = count[key][1:]

currInd.sort()
steps = n - len(currInd)
print(steps)

# covering left hand side of leftmost
if currInd[0] != 0:
    for i in range(currInd[0]-1,-1,-1):
        if nums[i] > currElem:
            print(2,i+1,i+2)
        elif nums[i] < currElem:
            print(1,i+1,i+2)

# covering right of every other element
for i in range(len(currInd)):
    if i == len(currInd)-1:
        if currInd[i] < n-1:
            for j in range(currInd[i]+1,n):
                if nums[j] > currElem:
                    print(2,j+1,j)
                elif nums[j] < currElem:
                    print(1,j+1,j)
    else:
        left = currInd[i]
        right = currInd[i+1]
        for j in range(left+1,right):
            if nums[j] > currElem:
                print(2,j+1,j)
            elif nums[j] < currElem:
                print(1,j+1,j)