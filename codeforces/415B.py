n,f=map(int, raw_input().split())
sold=0
shortage=[]
for i in range(n):
	k,l=map(int, raw_input().split())
	if k>=l:
		sold+=l
	else:
		if 2*k<l:
			poss=2*k
		else:
			poss=l
		shortage.append([poss,k,l])
shortage.sort(reverse=True)
# print shortage
for i in range(min(f,len(shortage))):
	# print i
	sold+=shortage[i][0]
# print i
if f>0:
	i+=1
else:
	i=0
while(i<len(shortage)):
	sold+=shortage[i][1]
	i+=1
print sold