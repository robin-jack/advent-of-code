# --- Day 3: Lobby ---
# Robin Jack

def jolter():
	with open("2025/inputs/day3.txt", "r") as file:
		jolts = 0
		for bank in file:
			lg = largest_pair(bank.strip())
			# print(lg)
			jolts += int(lg)
	return jolts


def largest_pair(bank):
	dec = 0 # index of biggest decimal
	for i in range(len(bank)-2):
		a = bank[dec]
		b = bank[i+1]
		if b > a:
			dec = i+1

	uni = dec+1 # index of biggest unit
	for j in range(dec+1, len(bank)-1):
		a = bank[uni]
		b = bank[j+1]
		if b > a:
			uni = j+1

	# print(bank[dec]+bank[uni])
	return bank[dec]+bank[uni]

# --- Part Two ---

def super_jolter():
	with open("2025/inputs/day3.txt", "r") as file:
		jolts = 0
		for bank in file:
			ld = dozen(bank.strip())
			# print(ld)
			jolts += int(ld)
	return jolts

def dozen(bank):
	d = 12
	doz = "" # formed number
	last = 0 # index of last picked number
	for n in range(d):
		upto = len(bank)-(d-(len(doz)+1)+1) # look up to here
		for i in range(last, upto):
			a = bank[last]
			b = bank[i+1]
			if b > a:
				last = i+1
		doz += bank[last]
		last += 1
	# print(doz)
	return doz


if __name__ == "__main__":
	jolts = jolter()
	print(jolts)

	print("---")

	sjolts = super_jolter()
	print(sjolts)
	
	# b = "818181911112111"
	# dozen(b)