def check(n,k):
    req = (n//2) + (n%2)
    eat = 0
    while n > 0 and eat < req:
        eat += min(n,k)
        n -= min(n,k)
        n -= n//10
    if eat >= req:
        return True
    else:
        return False

n = int(input())
l = 1
r = n
ans = 0
# l <= r, equal will be there, since you are alloting m-1 and m+1
while l <= r:
    m = (l+r)//2
    if check(n,m):
        r = m-1
    else:
        l = m+1


print(l)





