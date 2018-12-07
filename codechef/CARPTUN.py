t=int(raw_input())
for _ in range(t):
	n=int(raw_input())
	times=list(map(int, raw_input().split()))
	c,d,s=map(int, raw_input().split())
	print (c-1)*max(times)