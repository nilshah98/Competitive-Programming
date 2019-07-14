q = int(raw_input())

for _ in range(q):
    n,k = map(int, raw_input().split())
    nums = list(map(int, raw_input().split()))
    maxi = max(nums)
    mini = min(nums)
    minreq = (maxi-mini)//2
    if((maxi-mini)%2):
        minreq += 1
    if k >= minreq:
        print(mini + k)
    else:
        print(-1)
