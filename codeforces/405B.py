n,k=map(int, raw_input().split())
freq={}
for i in range(k):
	x,y=map(int, raw_input().split())
	if x in freq.keys():
		freq[x]+=1
	else:
		freq[x]=1
	if y in freq.keys():
		freq[y]+=1
	else:
		freq[y]=1
check={}
for i in freq.keys():
	if freq[i] in check:
		check[freq[i]]+=1
	else:
		check[freq[i]]=1
poss=True
for i in check.keys():
	if check[i]%(i+1)==0:
		continue
	else:
		poss=False
		break
# print check
# print freq
if poss:
	print "YES"
else:
	print "NO"