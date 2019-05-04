n = int(input())
number = input()

num8 = number[:-10].count("8")

if num8 > (n-11)//2:
    print("YES")
else:
    print("NO")