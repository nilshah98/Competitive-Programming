n = int(input())
queue = list(map(int, input().split()))
rem = 0
moves = []
i = 0
for i in range(n):
    temp = queue[i] - i
    j = temp//n
    if temp%n:
        j += 1
    moves.append(j)

print(moves.index(min(moves))+1)
