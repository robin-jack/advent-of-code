# --- Day 4: Printing Department ---
# Robin Jack

def get_grid():
	grid = []
	with open("inputs/day4.txt", "r") as file:
		for line in file:
			row = []
			for c in line.strip():
				if c == "@":
					row.append(1)
				else:
					row.append(0)
			grid.append(row)
	return grid

def roller():
	accessible = 0
	grid = get_grid()
	for x in range(len(grid)):
		bef = grid[x-1] if x != 0 else [0]
		row = grid[x]
		nex = grid[x+1] if x < len(grid)-1 else [0]
		for y in range(len(row)):
			if row[y]:
				a = get(bef, y-1)
				b = get(bef, y)
				c = get(bef, y+1)

				d = get(row, y-1)
				e = get(row, y+1)

				f = get(nex, y-1)
				g = get(nex, y)
				h = get(nex, y+1)

				if (a+b+c+d+e+f+g+h) < 4:
					accessible += 1
	# print(accessible)
	return accessible

def get(row, i):
	return row[i] if 0 <= i < len(row) else 0
				
def gri():
	g = get_grid()
	for r in g:
		print(r)
	print("---")

# --- Part Two ---

def rollit():
	total = 0
	grid = get_grid()
	while True:
		access, to_remove = rollerblade(grid)
		total += access
		if access == 0:
			break
		for i, j in to_remove:
			grid[i][j] = 0
	return total
			

def rollerblade(grid):
	access = 0
	to_remove = []

	for row in range(len(grid)):
		for c in range(len(grid[row])):
			if grid[row][c]:
				suma = -1 # so it doesnt count itself
				for i in range(-1, 2):
					for j in range(-1, 2):
						suma += rget(grid, row+i, c+j)
				# print(row, c, "=", suma)
				if suma < 4:
					access += 1
					to_remove.append([row, c])
	# print(access)
	return access, to_remove

def rget(grid, i, j):
	cell = 0
	if 0 <= i < len(grid):
		if 0 <= j < len(grid[i]):
			cell = grid[i][j]
	return cell

if __name__ == "__main__":
	a = roller()
	print(a)

	print("---")

	t = rollit()
	print(t)