nums="1234567890"
t=int(raw_input())
for _ in range(t):
	seq=raw_input()
	sum=0
	for i in seq:
		if i in nums:
			sum+=int(i)
	print sum