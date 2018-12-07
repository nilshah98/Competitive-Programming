n,m,k=map(int, raw_input().split())
seats=[]
for i in range(n):
	seats.append(list(raw_input()))
rows=[]
for i in seats:
	freq=0
	for j in i:
		if j==".":
			freq+=1
		else:
			if freq>=k:
				rows.append(freq)
			freq=0
	if i[-1]!="*":
		if freq>=k:
			rows.append(freq)
cols=[]
for i in range(m):
	freq=0
	for j in range(n):
		if seats[j][i]==".":
			freq+=1
		else:
			if freq>=k:
				cols.append(freq)
			freq=0
	if seats[n-1][i]!="*":
		if freq>=k:
			cols.append(freq)
total=0
if k>1:	
	for i in rows:
		total+=(i-k+1)
	for i in cols:
		total+=(i-k+1)
if k==1:
	total=sum(rows)
print total