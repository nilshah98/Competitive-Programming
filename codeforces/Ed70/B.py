s = input()

singledigits = [[0 for _ in range(10)]]
for i in range(1,20):
    singledigits.append([])
    for j in range(10):
        
        if j == 0:
            singledigits[i].append(-1)        
        
        else:
            mod = i%j
            ten = 10%j

            if(mod):
                if ten == 0 or ((i-mod)%ten):
                    singledigits[i].append(-1)
                else:
                    needed = (10*((i-mod)//ten)+i)//j
                    singledigits[i].append(needed)    
            else:
                singledigits[i].append(i//j)

for i in range(20):
    print(i)
    print(*singledigits[i])
    print("================================")

dif = [[[0 for _ in range(10)] * 10]]
for i in range(1,20):
    dif.append([])
    for j in range(10):
        dif[i].append([])
    
        for k in range(j):
            dif[i][j].append(dif[i][k][j])

        for k in range(j,10):
            if k == 0:
                dif[i][j].append(-1)

            if j == k and k>0:
                dif[i][j].append(singledigits[i][j])

            elif k>0:

                mod = i%k
                ten = 10%k

                if(mod):
                    rem = -1
                    if dif[mod][j][j] != -1:
                        rem = singledigits[mod][j]
                    if singledigits[mod][k] != -1:
                        if rem > -1:
                            rem = min(singledigits[mod][k],rem)
                        else:
                            rem = singledigits[mod][k]
                    
                    if(rem == -1):
                        dif[i][j].append(-1)
                    else:
                        dif[i][j].append(i//k + rem)
                else:
                    dif[i][j].append(i//k)

for i in range(20):
    print(i)
    print("======================================")
    print (*dif[i])
    print("======================================")
s = "0"+s
ans = [[0 for _ in range(10)] for _ in range(10)]

for i in range(1,len(s)):
    if int(s[i]) > int(s[i-1]):
        curr = int(s[i]) - int(s[i-1])
    else:
        curr = 10 + int(s[i]) - int(s[i-1])

    for j in range(10):
        for k in range(10):
            ans[j][k] += (dif[curr][j][k])

for row in ans:
    print(*row)

