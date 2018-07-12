n,v = map(int, input().split())
visitors = []
for i in range(v):
    l,r = map(int, input().split())
    visitors.append([r-l+1,l,r])

dist = []

for i in range(n):
    if i%2:
        dist.append("0")
    else:
        dist.append("1")

print("".join(dist))
