n,d = map(int, input().split())
hotels = list(map(int, input().split()))

count = 0

for i in range(1,n):
    back = hotels[i-1] + d
    front = hotels[i] - d
    if front > back :
        count += 2
    elif front == back:
        count += 1

print(count + 2)
