n=int(raw_input())
flowers=list(map(int, raw_input().split()))
maxcount=flowers.count(max(flowers))
mincount=flowers.count(min(flowers))
maxbeaut=max(flowers)-min(flowers)
if(max(flowers)!=min(flowers)):
	combinations=maxcount*mincount
else:
	combinations=n*(n-1)//2
print maxbeaut, combinations