n=int(raw_input())
seq=list(map(int, raw_input().split()))
currenergy=0
currmin=0
currmin=0
curr=seq[0]
for i in seq[1::]:
	currenergy+=curr-i
	curr=i
	if(currenergy<currmin):
		currmin=currenergy
ans = seq[0] + abs(currmin)
print ans