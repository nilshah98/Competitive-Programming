l = int(input())
nums = map(int, input().split())
nums = set(nums)
if 0 in nums:
	print(len(nums) - 1)
else:
	print(len(nums))