from bisect import *
n,q = map(int, input().split())
weights = list(map(int, input().split()))
queries = []
for i in range(q):
	queries.append(int(input()))

weights.sort()

weightsSum = [weights[0]]

for i in weights[1::]:
	weightsSum.append(weightsSum[-1] + i)

for i in queries:
	index = bisect_left(weightsSum,i)
	if index == n:
		print(index)
	elif weightsSum[index] > i:
		print(index)
	else:
		print(index+1)
	
