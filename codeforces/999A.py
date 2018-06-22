n,k = map(int, input().split())
problems = list(map(int, input().split()))

# starting from left part
lindex = 0
while lindex < n and problems[lindex] <= k:
    lindex += 1

# starting from right side
rindex = n-1
while rindex >= 0 and problems[rindex] <= k:
    rindex -= 1

if lindex == n or rindex == -1:
    print(n)
else:
    print(n-(rindex-lindex+1))

