mod=10**9+7
n=int(raw_input())
seq=list(map(int, raw_input().split()))
seq.sort(reverse=True)
ans=0
for i in range(n):
	ans-=(seq[i]*pow(2,i,mod))
	ans+=(seq[i]*pow(2,n-1-i,mod))
	ans=ans%mod
print ans%mod