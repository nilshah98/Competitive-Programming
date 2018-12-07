t=int(raw_input())
for _ in range(t):
	row,col=map(int, raw_input().split())
	seq=[]
	for i in range(row):
		seq.append(raw_input())
	row1=[]
	row2=[]
	for i in range(col):
		if i%2:
			row1.append("R")
			row2.append("G")
		else:
			row1.append("G")
			row2.append("R")
	poss1=[]
	poss2=[]
	for i in range(row):
		if i%2:
			poss1.append(row1)
			poss2.append(row2)
		else:
			poss1.append(row2)
			poss2.append(row1)
	cost1=0
	cost2=0
	for i in range(row):
		for j in range(col):
			if poss1[i][j]=="R" and seq[i][j]!=poss1[i][j]:
				cost1+=5
			elif poss1[i][j]=="G" and seq[i][j]!=poss1[i][j]:
				cost1+=3
			if poss2[i][j]=="R" and seq[i][j]!=poss2[i][j]:
				cost2+=5
			elif poss2[i][j]=="G" and seq[i][j]!=poss2[i][j]:
				cost2+=3
	print min(cost1,cost2)