from collections import defaultdict
q = int(input())

for _ in range(q):
    n = int(input())
    candies = list(map(int, input().split()))

    count = defaultdict(int)

    for i in candies:
        count[i] += 1
    
    vals = []

    for i in count.keys():
        vals.append(count[i])

    vals.sort(reverse=True)

    curr = vals[0]
    ans = 0

    for i in vals:
        if curr <= 0:
            break
        else:
            if i < curr:
                curr = i
            ans += curr
            curr -= 1    
    print(ans)