t = int(input())
ans = 0
for _ in range(t):
    x,y = map(int, input().split())
    if x+y > ans:
        ans = x+y

print(ans)
