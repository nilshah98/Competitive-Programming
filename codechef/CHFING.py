t = int(input())
mod = (10**9) + 7
for _ in range(t):
    n,k = map(int, input().split())
    start = k-1
    a = max(0,(2*k - (n+k)))
    num = (a//(n-1)) + 1
    end = (num*((2*a) - (num-1)*(n-1)))//2
    # print(a,n-1,num)
    print((start + end)%mod)