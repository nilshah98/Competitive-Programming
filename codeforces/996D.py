n = int(input())
n = 2*n
couples = list(map(int, input().split()))

moves = 0
for i in range(0,n,2):
    curr = couples[i]
    #print(curr)
    for j in range(i+1,n):
        if couples[j] == curr:
            for k in range(j-1,i,-1):
                couples[k+1] = couples[k]
                moves += 1
                #print(*couples)
            couples[i+1] = couples[i]
            break
        else:
            #print("xXXX",j)
            continue
#print(*couples)
print(moves)

