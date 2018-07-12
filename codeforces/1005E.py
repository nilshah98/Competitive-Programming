n,m=map(int, input().split())
nums = list(map(int, input().split()))

left = {}
right = {}

leftl = 0
leftm = 0

rightl = 0
rightm = 0

start = nums.index(m)

ans = 1

#for left side
for i in range(start-1,-1,-1):
    if nums[i]>m:
        leftm += 1
    else:
        leftl += 1

    if leftl == leftm:
        ans += 1
    elif leftl+1 == leftm:
        ans += 1

    temp = leftm - leftl
    if temp in left.keys():
        left[temp] += 1
    else:
        left[temp] = 1

for i in range(start+1,n,1):
    if nums[i]>m:
        rightm += 1
    else:
        rightl += 1

    if rightl == rightm:
        ans += 1
    elif rightl+1 == rightm:
        ans += 1

    temp = rightm-rightl
    if temp in right.keys():
        right[temp] += 1
    else:
        right[temp] = 1
for i in left.keys():
    poss = (-1)*i
    if poss in right.keys():
        ans += right[poss]*left[i]

    if poss+1 in right.keys():
        ans += right[poss+1]*left[i]



print(ans)

