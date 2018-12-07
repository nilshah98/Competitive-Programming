n=int(raw_input())
heights=list(map(int, raw_input().split()))
distinctheights=set(heights).length()
vals=list(map(int, raw_input().split()))
legs=[]
for i in range(n):
	legs.append([heights[i],vals[i]])
legs.sort()
totsum=sum(vals)
print legs