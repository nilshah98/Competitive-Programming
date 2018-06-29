a,b,c,n = map(int, input().split())
a -= c
b -= c
if a<0 or b<0:
    print(-1)
elif (a+b+c) < n:
    print(n - (a+b+c))
else:
    print(-1)
