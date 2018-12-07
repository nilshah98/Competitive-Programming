t=input()
for i in range(int(t)):
	soldier=list(map(int, list(input())))
	one=[]
	zero=[]
	k1=0
	k0=0
	for i in range(len(soldier)):
		if soldier[i]:
			k1+=1
			if k0>0:
				zero.append(k0)
				k0=0
		else:
			k0+=1
			if k1>0:
				one.append(k1)
				k1=0
	zero.append(k0)
	if soldier[0]==0:
		del zero[0]
	k=len(one)
	answer=0
	for i in range(len(one)):
		answer+=one[i]*(k-i)
		answer+=sum(zero)*one[i]
		del zero[0]
	print(answer) 