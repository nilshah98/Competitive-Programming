t=input()
for i in range(int(t)):
  c=int(input())
  newlist = []
  while len(newlist)<=20 and c>0:
    for a in range(1,c):
      if ((c**2 - a**2)**0.5)%1 == 0:
        b = ((c**2 - a**2)**0.5)
        newlist.append(int(a+b+c))
    c-=1
  if newlist:
    print(max(newlist))
  else:
    print(0)