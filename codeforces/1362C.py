import math
t = int(input())
for _ in range(t):
    n = int(input())
    n += 1
    ans = 0
    digits = math.ceil(math.log(n, 2))
    for i in range(digits):
        ans += n//(2**i)
        if(n % 2**i == 0):
            ans -= 1
    print(ans)
