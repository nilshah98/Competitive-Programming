n,k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

totalbacteria = n
dupcount = 1
for i in range(1,n):
	if nums[i]>nums[i-1] and nums[i]<=nums[i-1] + k:
		totalbacteria -= dupcount

	if nums[i]==nums[i-1]:
		dupcount += 1
	else:
		dupcount = 1
print(totalbacteria)