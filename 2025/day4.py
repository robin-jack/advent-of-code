# --- Day 4: Printing Department ---
# Robin Jack

global grid

def get_grid():
	grid = []
	with open("tests/day4.txt", "r") as file:
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

if __name__ == "__main__":
	# gri()
	a = roller()
	print(a)