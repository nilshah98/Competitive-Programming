n,m = map(int, input().split())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append([])
    for i in row:
        if i == 1:
            matrix[-1].append([1,0])
        else:
            matrix[-1].append([0,1])

sequence = []
for i in range(n-1):
    for j in range(m-1):
        if matrix[i][j][0] == 1 and matrix[i+1][j][0] == 1 and matrix[i][j+1][0] == 1 and matrix[i+1][j+1][0] == 1:
            sequence.append([i+1,j+1])
            matrix[i][j][1] = 1
            matrix[i+1][j][1] = 1
            matrix[i][j+1][1] = 1
            matrix[i+1][j+1][1] = 1

flag = False
for i in range(n):
    if flag:
        break
    for j in range(m):
        if matrix[i][j][1] == 0:
            flag = True
            break

if flag:
    print(-1)
else:
    print(len(sequence))
    for i in sequence:
        print(*i)    