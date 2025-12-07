# --- Day 1: Secret Entrance ---
# Robin Jack

def crack_code():

	dial = 50
	psw = 0
	with open("2025/inputs/day1.txt", "r") as file:
		for line in file:

			turn = line[0]
			amnt = int(line[1:])
			if amnt >= 100:
				amnt = amnt % 100

			if turn == "R":
				if (dial + amnt) > 99:
					dial += (amnt-100)
				else:
					dial += amnt
			else:
				if (dial - amnt) < 0:
					dial += (100-amnt)
				else:
					dial -= amnt

			if dial == 0:
				psw += 1


			#print(f"turn: {turn} - amount: {amnt}")
			#print(f"dial at: {dial} - password: {psw}")

	return psw

# --- Part Two ---

def second_half():

	dial = 50
	psw = 0
	with open("2025/inputs/day1.txt", "r") as file:
		for line in file:

			turn = line[0]
			amnt = int(line[1:])
			if amnt >= 100:
				psw += amnt // 100
				amnt = amnt % 100

			if turn == "R":
				if (dial + amnt) > 99:
					dial += (amnt-100)
					psw += 1
				else:
					dial += amnt
			else:
				if (dial - amnt) < 0:
					if dial != 0:
						psw += 1
					dial += (100-amnt)
				else:
					dial -= amnt
					if dial == 0:
						psw += 1

			# print(f"turn: {turn} - amount: {amnt}")
			# print(f"dial at: {dial} - password: {psw}")

	return psw

def mini_test():
	dial = 0
	psw = 0
	amnt = 5
	if amnt >= 100:
		psw += amnt // 100
		amnt = amnt % 100
	# L
	if (dial - amnt) < 0:
		dial += (100-amnt)
		psw += 1
	else:
		dial -= amnt
	if dial == 0:
		psw += 1
	print(dial)
	print(amnt)
	print(psw)

if __name__ == "__main__":
	cc = crack_code()
	print("code =", cc)

	print("---")

	sh = second_half()
	print("code =", sh)

	# mini_test()
