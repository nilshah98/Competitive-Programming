m,s=map(int, raw_input().split())
if s==0 and m==1:
	print 0,0
elif s==0:
	print -1,-1
else:
	maxnum=[]
	while(s>0):
		for i in range(9,0,-1):
			s-=i
			if(s<0):
				s+=i
				continue
			else:
				maxnum.append(str(i))
				break
	if len(maxnum)<m:
		for i in range(m-len(maxnum)):
			maxnum.append("0")
	maxstr="".join(maxnum)
	if s==1:
		minstr=maxstr
	elif maxnum[-1]=="0":
		lastindex=maxnum.index("0")
		lastindex-=1
		temp=int(maxnum[lastindex])
		temp-=1
		maxnum[lastindex]=str(temp)
		maxnum[-1]="1"
		minstr="".join(maxnum[::-1])
	else:
		minstr="".join(maxnum[::-1])
	if(len(maxnum)==m):
		print minstr,maxstr
	else:
		print -1,-1