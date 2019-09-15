t = int(input())
for _ in range(t):
    b,h,c = map(int, input().split())
    x,y = map(int, input().split())
    profit = 0

    if x > y:
        hb = min(h,b//2)
        b -= hb*2
        profit += hb*x
        profit += min(c,b//2)*y
    else:
        cb = min(c,b//2)
        b -= cb*2    
        profit += cb*y
        profit += min(h,b//2)*x
    
    print(profit)