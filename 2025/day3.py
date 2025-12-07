# --- Day 3: Lobby ---
# Robin Jack

def jolter():
	with open("inputs/day3.txt", "r") as file:
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


if __name__ == "__main__":
	jolts = jolter()
	print(jolts)
	
    # b = "987654321111111"
    # largest_pair(b)