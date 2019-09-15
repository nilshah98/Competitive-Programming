n = int(input())
s = list(input())
t = list(input())

counta = 0
countb = 0
for i in range(n):
    if s[i] == "a":
        counta += 1
    else:
        countb += 1
    
    if t[i] == "a":
        counta += 1
    else:
        countb += 1

if counta%2 or countb%2:
    print(-1)
else:
    ab = []
    ba = []
    for i in range(n):
        if s[i] != t[i]:
            if s[i] == "a" and t[i] == "b":
                ab.append(i+1)
            else:
                ba.append(i+1)

    ans = []
    for i in range(0,len(ab),2):
        if i+1 < len(ab):
            ans.append([ab[i],ab[i+1]])
    for i in range(0,len(ba),2):
        if i+1 < len(ba):
            ans.append([ba[i],ba[i+1]])
    if len(ab)%2 and len(ba)%2:
        ans.append([ba[len(ba)-1],ba[len(ba)-1]])
        ans.append([ab[len(ab)-1],ba[len(ba)-1]])
    
    print(len(ans))
    for i in ans:
        print(*i)
