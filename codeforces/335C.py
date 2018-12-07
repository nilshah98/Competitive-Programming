n=int(raw_input())
pos=[-1 for i in range(n+1)]
train=list(map(int, raw_input().split()))
for i in range(n):
	pos[train[i]]=i

maxfreq=1
currfreq=1
currpos=pos[1]
for i in range(2,n+1):
	if(pos[i]>currpos):
		currfreq+=1
		currpos=pos[i]
	else:
		currfreq=1
		currpos=pos[i]
	if(currfreq>maxfreq):
		maxfreq=currfreq
if(currfreq>maxfreq):
	maxfreq=currfreq
print n-maxfreq