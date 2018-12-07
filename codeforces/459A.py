n=int(input())
fib=[1,1]
for i in range(n):
	fib.append(fib[-1]+fib[-2])
fib=set(fib)
name=[]
for i in range(n):
	if i+1 in fib:
		name.append("O")
	else:
		name.append("o")
print "".join(name)