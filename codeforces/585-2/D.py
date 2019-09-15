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


# print(sum_start,sum_end)
# print(miss_start,miss_end)

if sum_end > sum_start:
    diff_sum = sum_end - sum_start
    diff_sum += 9 * (miss_end) // 2
    if miss_end % 2:
        diff_sum += 9

    negotiate_sum = 9 * (miss_start // 2)
    if miss_start % 2:
        negotiate_sum += 9

else:
    diff_sum = sum_start - sum_end
    diff_sum += 9 * (miss_start // 2)
    if miss_start % 2:
        diff_sum += 9

    negotiate_sum = 9 * (miss_end // 2)
    if miss_end % 2:
        negotiate_sum += 9

if negotiate_sum >= diff_sum:
    print("Bicarp")
else:
    print("Monocarp")