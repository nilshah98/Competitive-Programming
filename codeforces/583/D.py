n,m = map(int, input().split())
maze = []

for i in range(n):
    temp = list(input())
    maze.append(temp)

# check each row for blocks from 2nd to 2nd last
currcol = 0
for i in range(n-1):
    while maze[i+1][currcol] == "#" and currcol < m:
        currcol += 1
        if maze[i][currcol] == "#":
            currcol = m
            break
    if currcol == m:
        break

# check second last
if currcol < m:
    secondD = True
    firstD = True
    for i in range(currcol,m):
        if maze[n-2][i] == "#":
            secondD = False
            currcol = i-1

    if secondD:
        if maze[n-1][m-2] == "#":
            firstD = False
    else:
        for i in range(currcol,m):
            if maze[n-1][i] == "#":
                firstD = False
else:
    secondD = False
    firstD = False

# check each col for block from 2nd to 2nd last
currrow = 0
for i in range(m-1):
    while maze[currrow][i+1] == "#" and currrow < n:
        currrow += 1
        if maze[currrow][i] == "#":
            currrow = n
            break
    if currrow == n:
        break

if currrow < n:
    # check second last
    secondR = True
    firstR = True
    for i in range(currrow,n):
        if maze[i][m-2] == "#":
            secondR = False
            currrow = i-1

    if secondR:
        if maze[n-2][m-1] == "#":
            firstR = False
    else:
        for i in range(currrow,n):
            if maze[i][m-1] == "#":
                firstR = False
else:
    secondR = False
    firstR = False

if not firstR and not secondD and not secondR and not firstD:
    ans = 0
elif not firstR and not secondD:
    ans = 1
elif not secondR and not firstD:
    ans = 1
else:
    ans = 2

print(currrow,currcol)
print(firstD,secondD)
print(firstR,secondR)
print(ans)

# temp = []
# for i in maze[::-1]:
#     temp.append(i[::-1])

# maze = temp
# # print(maze)
# # check each row for blocks from 2nd to 2nd last
# currcol = 0
# for i in range(n-1):
#     while maze[i+1][currcol] == "#" and currcol < m:
#         currcol += 1
#         if maze[i][currcol] == "#":
#             currcol = m
#             break
#     if currcol == m:
#         break

# # check second last
# if currcol < m:
#     secondD = True
#     firstD = True
#     for i in range(currcol,m):
#         if maze[n-2][i] == "#":
#             secondD = False
#             currcol = i-1

#     if secondD:
#         if maze[n-1][m-2] == "#":
#             firstD = False
#     else:
#         for i in range(currcol,m):
#             if maze[n-1][i] == "#":
#                 firstD = False
# else:
#     secondD = False
#     firstD = False

# # check each col for block from 2nd to 2nd last
# currrow = 0
# for i in range(m-1):
#     while maze[currrow][i+1] == "#" and currrow < n:
#         currrow += 1
#         if maze[currrow][i] == "#":
#             currrow = n
#             break
#     if currrow == n:
#         break

# if currrow < n:
#     # check second last
#     secondR = True
#     firstR = True
#     for i in range(currrow,n):
#         if maze[i][m-2] == "#":
#             secondR = False
#             currrow = i-1

#     if secondR:
#         if maze[n-2][m-1] == "#":
#             firstR = False
#     else:
#         for i in range(currrow,n):
#             if maze[i][m-1] == "#":
#                 firstR = False
# else:
#     secondR = False
#     firstR = False

# if not firstR and not secondD and not secondR and not firstD:
#     rans = 0
# elif not firstR and not secondD:
#     rans = 1
# elif not secondR and not firstD:
#     rans = 1
# else:
#     rans = 2


# print(min(ans,rans))