# --- Day 2: Gift Shop ---
# Robin Jack

def sum_invalids():
	ids_sum = 0
	with open("inputs/day2_input.txt", "r") as file:
		line = file.read()
		ids = line.split(",")
		for i in ids:
			a = int(i.split("-")[0])
			b = int(i.split("-")[1])
			
			for n in range(a, b+1):
				nlen = len(str(n))
				if (nlen % 2 == 0):
					h = nlen//2
					l, r = str(n)[:h], str(n)[h:]
					if (l == r):
						ids_sum += n
	return ids_sum



if __name__ == "__main__":
	si = sum_invalids()
	print(si)