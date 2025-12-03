# advent of code - day 1
# Robin Jack

def crack_code():

	dial = 50
	psw = 0
	with open("inputs/day1_input.txt", "r") as file:
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

if __name__ == "__main__":
	p = crack_code()
	print("code =", p)