n,k = map(int, input().split())

grid = []
for _ in range(n):
	grid.append(list(input()))

count = [[0 for _ in range(n)] for _ in range(n)]

row = 0
while row < n:
	col = 0
	curr_count = 0
	buffer_cells = []
	while col < n:
		if grid[row][col] == "#":
			if curr_count >= k:
				for cell in buffer_cells:
					count[cell[0]][cell[1]] += 1
				col = buffer_cells[0][1]
			buffer_cells = []
			curr_count = 0
		else:
			curr_count += 1
			buffer_cells.append([row,col])
		col += 1
	if curr_count >= k:
		diff = curr_count - k
		offset = 0
		left = 0
		right = len(buffer_cells)-1
		while left <= right:
			count[buffer_cells[left][0]][buffer_cells[left][1]] += 1
			count[buffer_cells[left][0]][buffer_cells[left][1]] += offset
			count[buffer_cells[right][0]][buffer_cells[right][1]] += 1
			count[buffer_cells[right][0]][buffer_cells[right][1]] += offset
			if offset < diff:
				offset += 1
			left += 1
			right -= 1
	row += 1

col = 0
while col < n:
	row = 0
	curr_count = 0
	buffer_cells = []
	while row < n:
		if grid[row][col] == "#":
			if curr_count >= k:
				for cell in buffer_cells:
					count[cell[0]][cell[1]] += 1
				row = buffer_cells[0][0]
			buffer_cells = []
			curr_count = 0
		else:
			curr_count += 1
			buffer_cells.append([row,col])
		row += 1
	if curr_count >= k:
		diff = curr_count - k
		offset = 0
		left = 0
		right = len(buffer_cells)-1
		while left <= right:
			count[buffer_cells[left][0]][buffer_cells[left][1]] += 1
			count[buffer_cells[left][0]][buffer_cells[left][1]] += offset
			count[buffer_cells[right][0]][buffer_cells[right][1]] += 1
			count[buffer_cells[right][0]][buffer_cells[right][1]] += offset
			if offset < diff:
				offset += 1
			left += 1
			right -= 1
	col += 1

max = 0
ans = []
for row in range(n):
	for col in range(n):
		if count[row][col] > max:
			ans = [row+1,col+1]
			max = count[row][col]

if len(ans) > 0:
	print(" ".join(map(str, ans)))
else:
	print(1,1)

# for row in count:
# 	print(*row)