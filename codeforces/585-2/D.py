n = int(input())
s = list(input())
 
sum_start = 0
sum_end = 0
miss_start = 0
miss_end = 0
 
for i in range(n):
    if i+1 > n//2:
        if s[i] == "?":
            miss_end += 1
        else:
            sum_end += int(s[i])
 
    else:
        if s[i] == "?":
            miss_start += 1
        else:
            sum_start += int(s[i])

# Case1 Monocarp fills everything with 9 from start
diff_start = (sum_start - sum_end) + (9 * (miss_start // 2))
if miss_start % 2:
    diff_start += 9
 
diff_end = (sum_end - sum_start) + (9 * (miss_end // 2))
if miss_end % 2:
    diff_end += 9

negotiate_end = 9 * (miss_end // 2)
if miss_end % 2:
    negotiate_end += 9

negotiate_start = 9 * (miss_start // 2)
if miss_start % 2:
    negotiate_start += 9

if diff_start > negotiate_end or diff_end > negotiate_start:
    print("Monocarp")
else:
    print("Bicarp")