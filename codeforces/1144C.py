n = int(input())
nums = list(map(int, input().split()))

incr = []
decr = []

nums.sort()

flag = True

for i in nums:
    if len(incr) > 0:
        if incr[-1] == i:
            if len(decr) > 0:
                if decr[-1] == i:
                    flag = False
                    print("NO")
                    break
                else:
                    decr.append(i)
            else:
                decr.append(i)
        else:
            incr.append(i)
    else:
        incr.append(i)

if flag:
    print("YES")
    print(len(incr))
    print(*incr)
    print(len(decr))
    print(*decr[::-1])