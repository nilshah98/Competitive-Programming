n = int(input())
size = list(map(int, input().split()))
cost = list(map(int, input().split()))

minCost = 10**9

for i in range(n):
	for j in range(i+1,n):
		if size[i]<size[j]:
			for k in range(j+1,n):
				if size[j]<size[k]:
					currCost = cost[i]+cost[j]+cost[k]
					if currCost < minCost:
						minCost = currCost

if minCost == 10**9:
	minCost = -1
print(minCost)
