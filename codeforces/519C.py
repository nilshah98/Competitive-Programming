x,n = map(int, input().split())

# Each experienced takes 2 noobs
if 2*x <= n:
    print(x)
# Each noob takes 2 experienced
elif 2*n <= x:
    print(n)
# Mixed scenes, take care of even odd
else:
    diff = abs(x - n)
    equ = min(x,n) - diff
    if equ%3 == 2:
        rem = 1
    else:
        rem = 0
    print(diff + (2*(equ//3)) + rem)
