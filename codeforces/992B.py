def fact(n):
	factors = []
	while n>1:
		for i in range(2,n+1):
			if n%i==0:
				n//=i
				factors.append(i)
				break
	return factors

l,r,gcd,lcm = map(int, input().split())
if lcm%gcd == 0:
	diff = lcm//gcd
	factors = fact(diff)
	distinct = set(factors)
	ans = 2**len(distinct)
	print(ans)
else:
	print(0)