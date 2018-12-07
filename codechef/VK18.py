vals=[0 for i in range(2*(10**6)+1)]
for i in range(1,2*(10**6)+1):
	evensum=0
	oddsum=0
	for j in str(i):
		digit=int(j)
		if digit%2:
			evensum+=digit
		else:
			oddsum+=digit
	vals[i]=abs(evensum-oddsum)
prefixsum=[0 for i in range(2*(10**6)+1)]
sumx=0
for i in range(2*(10**6)+1):
	sumx+=vals[i]
	prefixsum[i]=sumx
diamonds=[0 for i in range(10**6+1)]
diamonds[1]=2
for i in range(2,10**6+1):
	diamonds[i]= diamonds[i-1] + 2*(prefixsum[(2*i)-1] - prefixsum[i]) + vals[2*i]

t=int(raw_input())
for _ in range(t):
	n=int(raw_input())
	print diamonds[n]