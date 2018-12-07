def findSum(arr, n):
     
    # Sum all array elements
    sum = []
    for i in range(n):
        sum.append(arr[i]+sum[-1])
  
    # Result is sum * 2^(n-1)
    return sum * (1 << (n - 1))
  
# Driver program to test findSum()
arr = [1, 2]
n = len(arr)
print findSum(arr, n)