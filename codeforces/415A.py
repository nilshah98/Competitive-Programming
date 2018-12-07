def average(n,k):
	return int(round(n/(k*1.0)))
n,k=map(int, raw_input().split())
obt=list(map(int, raw_input().split()))
marks=sum(obt)
tot=n
added=0
while(average(marks,tot)<k):
	# print average(marks,tot)
	added+=1
	marks+=k
	tot+=1
print added