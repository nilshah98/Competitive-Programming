n = int(input())
ogStringFront = ""
ogStringBack = ""
totalSP = (2*n)-2
SPs = []
for i in range(totalSP):
  SPs.append(input())
SPs = list(enumerate(SPs))
SPs.sort(key=lambda s: len(s[1]))
# print(SPs)
ans = ["" for i in range(totalSP)]
flag = False
for i in range(totalSP):
  if i==0:
    ogStringFront = SPs[i][1]
    ans[SPs[i][0]] = "P"
  elif i==1:
    ogStringBack = SPs[i][1]
    ans[SPs[i][0]] = "S"
  else:
    if ogStringFront == SPs[i][1][0:i//2]:
      ogStringFront = SPs[i][1]
      ans[SPs[i][0]] = "P"
    elif ogStringBack == SPs[i][1][::-1][0:i//2][::-1]:
      ogStringBack = SPs[i][1]
      ans[SPs[i][0]] = "S"
    else:
      flag = not flag
      temp = ogStringFront
      ogStringFront = ogStringBack
      ogStringBack = temp
      if ogStringFront == SPs[i][1][0:i//2]:
        ogStringFront = SPs[i][1]
        ans[SPs[i][0]] = "P"
      elif ogStringBack == SPs[i][1][::-1][0:i//2][::-1]:
        ogStringBack = SPs[i][1]
        ans[SPs[i][0]] = "S"
# print("".join(ans))
# print(flag)
if flag:
  for i in range(len(ans)):
    if ans[i] == "S":
      ans[i] = "P"
    else:
      ans[i] = "S"
print("".join(ans))
