def sumdigits(n):
	sum=0
	while n>0:
		sum+=n%10
		n=n/10
	return sum
n=int(raw_input())
tot=0
curr=0
while(tot!=n):
	if sumdigits(curr)==10:
		tot+=1
	curr+=1
print curr-1