# http://codeforces.com/contest/892/problem/A
n=int(raw_input())
rem=list(map(int, raw_input().split()))
limit=list(map(int, raw_input().split()))
limit.sort(reverse=True)
poss=limit[0] + limit[1]
if(sum(rem) <= poss):
	print "YES"
else:
	print "NO"