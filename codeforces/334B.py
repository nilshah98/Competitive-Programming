n,k=map(int, raw_input().split())
sizes=list(map(int, raw_input().split()))
double=n-k
currmax=0
if k<n:
	for i in range(double):
		tempsum=0
		tempsum+=sizes[i]
		tempsum+=sizes[2*double-1-i]
		if(tempsum>currmax):
			currmax=tempsum
	for i in range(double,n):
		if sizes[i]>currmax:
			currmax=sizes[i]
else:
	currmax=sizes[-1]
print currmax