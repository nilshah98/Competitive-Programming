t=int(raw_input())
for _ in range(t):
	n=int(raw_input())
	seq=list(map(int, raw_input().split()))
	poss=[-1 for i in range(n)]
	for i in range(n):
		if poss[i]==-1:
			curr=seq[i]
			for j in range(i,n):
				if poss[j]==-1:
					if seq[j]!=curr:
						poss[j]=curr
						poss[i]=seq[j]
						break
		if poss[i]==-1:
			poss[i]=seq[i]
	for i in range(n):
		if seq[i]==poss[i]:
			temp=seq[i]
			for j in range(n):
				if(seq[j]!=temp and poss[j]!=temp):
					poss[i]=poss[j]
					poss[j]=temp
					break
	#FML
	hammingdistance=0
	for i in range(n):
		if seq[i]!=poss[i]:
			hammingdistance+=1
	print hammingdistance
	print " ".join(map(str, poss)) 