n,s=map(int, raw_input().split())
currmax=0
poss=False
for i in range(n):
	dollar,cents=map(int, raw_input().split())
	if(dollar<s):
		poss=True
		if(cents!=0):
			if((100-cents)>currmax):
				currmax=100-cents
	elif(dollar==s and cents==0):
		poss=True
if(poss):
	print currmax
else:
	print -1