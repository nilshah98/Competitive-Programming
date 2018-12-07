homex,homey=map(int, raw_input().split())
unix,uniy=map(int, raw_input().split())
n=int(raw_input())
lines=0
for i in range(n):
	a,b,c=map(int, raw_input().split())
	if((a*homex + b*homey + c > 0) and (a*unix + b*uniy + c < 0)):
		lines+=1
	elif((a*homex + b*homey + c < 0) and (a*unix + b*uniy + c > 0)):
		lines+=1
print lines