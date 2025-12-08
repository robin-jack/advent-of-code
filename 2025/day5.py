# --- Day 5: Cafeteria ---

def fresher():
	fresh = 0
	ranges = []
	with open("inputs/day5.txt", "r") as file:
		smol = 999999999999999999
		big = 1
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



if __name__ == "__main__":
	f = fresher()
	print(f)