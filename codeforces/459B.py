names={}
commands=[]
n,m=map(int, raw_input().split())
for i in range(n):
	name,ip=map(str, raw_input().split())
	names[ip]=name
for i in range(m):
	cmd,ip=map(str, raw_input().split())
	commands.append([cmd,ip])
for i in commands:
	print i[0]+" "+i[1]+" #"+names[i[1][:-1]]
