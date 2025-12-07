# --- Day 2: Gift Shop ---
# Robin Jack

def sum_invalids():
	ids_sum = 0
	with open("2025/inputs/day2.txt", "r") as file:
		line = file.read()
		ids = line.split(",")
		for ide in ids:
			a = int(ide.split("-")[0])
			b = int(ide.split("-")[1])
			
			for n in range(a, b+1):
				nlen = len(str(n))
				if (nlen % 2 == 0):
					h = nlen//2
					l, r = str(n)[:h], str(n)[h:]
					if (l == r):
						ids_sum += n
	return ids_sum

# --- Part Two ---

def second_half():
	ids_sum = 0
	with open("2025/inputs/day2.txt", "r") as file:
		line = file.read()
		ids = line.split(",")
		for ide in ids:
			a = int(ide.split("-")[0])
			b = int(ide.split("-")[1])
			for n in range(a, b+1):
				nlen = len(str(n))
				h = nlen//2
				for i in range(h, 0, -1):
					if (nlen % i == 0):
						num = str(n)[:i]
						imas = i
						grugu = (nlen//i)-1 # divisiones iguales del numero menos uno -> 24|24|24 -> 3 divisiones - 1 = 2
						for j in range(grugu):
							eq = True
							siguiente = str(n)[imas:imas+i]
							if (num == siguiente):
								imas += i
							else:
								eq = False
								break
						if eq:
							#print(n)
							ids_sum += n
							break
	return ids_sum



if __name__ == "__main__":
	si = sum_invalids()
	print(si)

	print("---")

	sh = second_half()
	print(sh)