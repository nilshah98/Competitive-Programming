t = int(input())
for _ in range(t):
	n = int(input())
	dirs = []
	for _ in range(n):
		cmd = input().split()
		if len(cmd) == 1:
			if len(dirs):
				print("/" + "/".join(dirs)+"/")
			else:
				print("/")
		else:
			for i in cmd[1].split("/"):
				if i == "":
					dirs.clear()
				elif i == "..":
					dirs.pop()
				else:
					dirs.append(i)
