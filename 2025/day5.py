# --- Day 5: Cafeteria ---

def fresher():
	fresh = 0
	ranges = []
	with open("inputs/day5.txt", "r") as file:
		# get ranges
		for line in file:
			if line.strip() == "":
				break
			ranges.append([int(n) for n in line.strip().split("-")])

		# get id's
		for line in file:
			i = int(line.strip())
			for r in ranges:
				if r[0] <= i <= r[1]:
					fresh += 1
					break

	# print(fresh)
	return fresh

# --- Part Two ---

def get_ranges():
	ranges = []
	with open("inputs/day5.txt", "r") as file:
		# get ranges
		for line in file:
			if line.strip() == "":
				break
			ranges.append([int(n) for n in line.strip().split("-")])
	return ranges

def fresherizer(sm):
	smallest = float('inf')
	base = [0, 0]
	nex = 0
	# bingo bongo bango sequence
	ranges = get_ranges()
	for k in ranges:
		if sm < k[0] < smallest:
			smallest = k[0]
			base = k

	# me quiero pegar un tiro 3 horas pa esto
	for j in ranges:
		for i in ranges:
			# print(f"{smallest} <= {i[0]} <= {base[1]} and {i[0]} >= {base[0]} and {i[1]} > {base[1]}")
			if smallest <= i[0] <= base[1] and i[0] >= base[0] and i[1] > base[1]:
				base = i
	# print("####################", smallest, base[1])
	return smallest, base[1]

def freshino():
	fresh = 0
	sm = 0
	for i in range(len(get_ranges())):
		sm, bg = fresherizer(sm)
		if sm == float('inf'):
			break
		fresh += ((bg+1) - sm)
		sm = bg
	return fresh


if __name__ == "__main__":
	f = fresher()
	print(f)

	print("---")

	i = freshino()
	print(i)