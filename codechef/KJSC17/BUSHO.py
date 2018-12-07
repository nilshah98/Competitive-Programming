t=input()
for i in range(int(t)):
  m,n=(map(int, input().split()))
  x,y=m,n
  while(y):
       x, y = y, x % y
  gcd=x
  
  print(str(int(n/gcd)-1)+' '+str(int(m/gcd)-1))