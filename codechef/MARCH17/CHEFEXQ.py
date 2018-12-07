n,q=map(int, raw_input().split())
init=list(map(int, raw_input().split()))
for i in range(q):
	poss=0
  	op,index,k=raw_input().split()
  	index=int(index)
  	k=int(k)
  	index-=1
  	if op=="1":
  		init[index]=k
  	else:
  		lastxor=0
		for j in range(index+1):
			lastxor^=init[j]
			if lastxor==k:
				poss+=1
  		print poss