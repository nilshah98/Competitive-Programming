import math

n,m = map(int, input().split())
alarms = list(map(int, input().split()))
diff = list(map(int, input().split()))

prev = alarms[0]
currGcd = alarms[1] - alarms[0]

for i in alarms[1:]:
    currGcd = math.gcd(currGcd,i - prev)
    prev = i

# print(currGcd)

flag = False
for i in range(m):
    if currGcd % diff[i] == 0:
        flag = True
        print("YES")
        print(alarms[0],i+1)
        break

if not flag:
    print("NO")