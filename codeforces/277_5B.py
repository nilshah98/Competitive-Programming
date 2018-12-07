n=int(raw_input())
boys=list(map(int, raw_input().split()))
boyskillz={}
for i in boys:
	if i in boyskillz.keys():
		boyskillz[i]+=1
	else:
		boyskillz[i]=1
m=int(raw_input())
girls=list(map(int, raw_input().split()))
girls.sort()
pairs=0
for i in girls:
	if i-1 in boyskillz.keys():
		pairs+=1
		boyskillz[i-1]-=1
		if boyskillz[i-1]==0:
			boyskillz.pop(i-1, None)
	elif i in boyskillz.keys():
		pairs+=1
		boyskillz[i]-=1
		if boyskillz[i]==0:
			boyskillz.pop(i, None)
	elif i+1 in boyskillz.keys():
		pairs+=1
		boyskillz[i+1]-=1
		if boyskillz[i+1]==0:
			boyskillz.pop(i+1, None)
print pairs	