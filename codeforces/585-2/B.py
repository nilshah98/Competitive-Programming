n = int(input())
nums = list(map(int, input().split()))

revmark = [0 for i in range(n)]
revcount = [[0,0] for i in range(n)]

# revmark = []
# revcount = []

curr = 0

for i in range(n-1,-1,-1):
    if nums[i] < 0:
        curr += 1
    
    if curr%2:
        revmark[i] = -1
    else:
        revmark[i] = 1

count = [0,0]
# [neg,pos]
for i in range(n):
    if revmark[i] < 0:
        count[0] += 1
    else:
        count[1] += 1
    
    if nums[i] < 0:
        if revmark[i] < 0:
            revcount[i] = count[:]
        else:
            revcount[i] = count[::-1]
    else:
        if revmark[i] < 0:
            revcount[i] = count[::-1]
        else:
            revcount[i] = count[:]

ans = [0,0]
for i in range(n):
    if i == 0:
        if nums[i] > 0:
            ans[1] += 1
        else:
            ans[0] += 1
    else:
        if nums[i] > 0:
            ans[1] += revcount[i-1][1]
            ans[1] += 1
            ans[0] += revcount[i-1][0]
        else:
            ans[1] += revcount[i-1][0]
            ans[0] += 1
            ans[0] += revcount[i-1][1]

print(*ans)
# print(revmark)
# print(*revcount)