import math
x,y = map(int, input().split())
xInTermsY = math.log(x,y)
if xInTermsY*y > x:
	print(">")
elif xInTermsY*y < x:
	print("<")
else:
	print("=")
