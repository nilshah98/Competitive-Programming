b = int(input())
g = int(input())
n = int(input())

if n < g and n < b:
    print(n+1)
elif n > g and n < b:
    print(g+1)
elif n > b and n < g:
    print(b+1)
else:
    print(max(b,g) - (n - min(b,g)) + 1)