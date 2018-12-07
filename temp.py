q = int(input())
numL = 0
numR = 0
leftId = {}
rightId = {}
for i in range(q):
  pos,id = input().split()
  if pos == "L":
    numL += 1
    leftId[id] = numL
  elif pos == "R":
    numR += 1
    rightId[id] = numR
  else:
    if id in leftId.keys():
      fromLeft = numL - leftId[id]
      fromRight = numR + leftId[id] - 1
      print(min(fromLeft,fromRight))
    else:
      fromLeft = numL + rightId[id] - 1
      fromRight = numR - rightId[id]
      print(min(fromLeft,fromRight))
