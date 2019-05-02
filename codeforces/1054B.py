n = int(input())
nums = list(map(int, input().split()))

ans = -1
curr = -1
for i in range(n):
    if nums[i] <= curr:
        pass
    elif nums[i] == curr + 1:
        curr = nums[i]
    else:
        ans = i+1
        break

print(ans)

'''
Mistakes =>
1.  Did not consider the fact that it is not necessary for it to grow linearly
    Since can pick an empty subarray, or the lowest element, and the array max remains same
'''