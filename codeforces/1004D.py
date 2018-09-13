n = int(input())
nums = list(map(int, input().split()))
counter = {}
poss = True

for i in nums:
    if i in counter.keys():
        counter[i] += 1
    else:
        counter[i] = 1

    if counter[i] > i*4 and i!=0:
        poss = False
    if i==0 and counter[i] > 1:
        poss = False

if poss:
    row = 1
    col = 1
    x = 1
    y = 1
    nums = list(set(nums))
    nums.sort()
    for i in nums:
        req = counter[i]

    print(nums)
else:
    print(-1)
