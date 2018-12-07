n=int(raw_input())
seq=list(map(int, raw_input().split()))
freq=[0 for i in range(10**6+1)]
startindex=[-1 for i in range(10**6+1)]
endindex=[-1 for i in range(10**6+1)]
maxfreq=0
maxelem=[]
for i in range(n):
	freq[seq[i]]+=1
	if(freq[seq[i]]>maxfreq):
		maxfreq=freq[seq[i]]
	if startindex[seq[i]]==-1:
		startindex[seq[i]]=i+1
	else:
		endindex[seq[i]]=i+1
for i in range(10**6+1):
	if(freq[i]==maxfreq):
		maxelem.append(i)
start=0
fin=0
mindist=10**9
for i in maxelem:
	if(endindex[i]==-1):
		endindex[i]=startindex[i]
	if((endindex[i]-startindex[i])<mindist):
		mindist=(endindex[i]-startindex[i])
		start=startindex[i]
		fin=endindex[i]
print start,fin