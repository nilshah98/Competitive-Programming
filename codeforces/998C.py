n,x,y = map(int, input().split())
seq = input()

segments = 0

flag = False
for i in seq:
    if i=="0":
        if flag:
            continue
        else:
            flag = True
    else:
        if flag:
            segments += 1
            flag = False
        else:
            continue

if flag:
    segments += 1
    flag = False

cost = segments*y
for i in range(segments):
    currcost = (i*x) + ((segments-i)*y)
    if currcost < cost:
        cost = currcost

print(cost)

