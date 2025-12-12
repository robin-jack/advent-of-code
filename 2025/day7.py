# --- Day 7: Laboratories ---
# Robin Jack


def beamer():
	diag = []
	with open("inputs/day7.txt") as file:
		for line in file:
			diag.append([s for s in line.strip()])

	split = 0

	for i in range(1, len(diag)):
		for j in range(len(diag[i])):
			if diag[i-1][j] == "S":
				diag[i][j] = "|"
			elif diag[i-1][j] == "|" and diag[i][j] != "^":
				diag[i][j] = "|"
			elif diag[i-1][j] == "|" and diag[i][j] == "^":
				diag[i][j-1] = "|"
				diag[i][j+1] = "|"
				split+=1

	for l in diag:
		print("".join(l))
	# print(split)

	return(split)




if __name__ == "__main__":
	s = beamer()
	print(s)