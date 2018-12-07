names=[]
characters=list("abcdefghijklmnopqrstuvwxyz")
for i in characters:
	newstr=["A"]
	newstr.append(i)
	names.append("".join(newstr))
for i in characters:
	newstr=["B"]
	newstr.append(i)
	names.append("".join(newstr))
for i in characters:
	newstr=["C"]
	newstr.append(i)
	names.append("".join(newstr))
n,k=map(int, raw_input().split())
answer=[]
curr=0
order=list(raw_input().split())
if k>2:
	if order[0]=="NO":
		for i in range(k):
			if i<2:
				answer.append(names[curr])
			else:
				curr+=1
				answer.append(names[curr])
	else:
		for i in range(k):
			answer.append(names[curr])
			curr+=1
	for i in range(1,len(order)):
		if order[i]=="NO":
			answer.append(answer[-(k-1)])
		else:
			curr+=1
			answer.append(names[curr])
else:
	if order[0]=="NO":
		for i in range(k):
			answer.append(names[curr])
	else:
		for i in range(k):
			answer.append(names[curr])
			curr+=1
	for i in range(1,len(order)):
		if order[i]=="NO":
			answer.append(answer[-1])
		else:
			curr+=1
			answer.append(names[curr])
print " ".join(answer)