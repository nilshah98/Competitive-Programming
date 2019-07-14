def getsumDigits(n):
    sumOfdigits = 0
    for i in str(n):
        sumOfdigits += int(i)
    return sumOfdigits

n = int(input())

x = getsumDigits(n)
while(x % 4 !=0 ):
    n += 1
    x = getsumDigits(n)

print(n)