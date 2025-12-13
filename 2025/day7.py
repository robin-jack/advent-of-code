# --- Day 7: Laboratories ---
# Robin Jack

path = "inputs/day7.txt"


def beamer():
	diag = []
	with open(path) as file:
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

	# for l in diag:
	# 	print("".join(l)) 
	# print("---")
	# print(split)

	return(split)

# --- Part Two ---

def quantum_beam():
	_, lws = get_diag()
	posi = to_bin(lws)
	good = (2**lws) - 1

	split = 0
	control = []
	for k in range(len(posi)):
		c = 0
		test = 0
		diag, _ = get_diag()
		for i in range(1, len(diag)):
			for j in range(len(diag[i])):
				if diag[i-1][j] == "S":
					diag[i][j] = "|"
				elif diag[i-1][j] == "|" and diag[i][j] != "^":
					diag[i][j] = "|"
				elif diag[i-1][j] == "|" and diag[i][j] == "^":
					path = get_path(posi[k][c])
					diag[i][j+path] = "|"
					c+=1
					test +=1
		v = repeater(lws, test, posi[k])
		if v == good or v not in control:
			control.append(v)

		print(test)
		print(posi[k])
		for l in diag:
			print("".join(l))
		print(" ")


	# print(control)
	result = len(control)
	return(result)

def repeater(lws, test, posi):
	seg = posi[:test]

	pad = seg + [0] * (lws-len(seg))

	b = "".join(str(x) for x in pad)

	value = int(b, 2)

	return value

def get_diag():
	diag = []
	lws = 0
	with open(path) as file:
		for line in file:
			if "^" in line:
				lws += 1
			diag.append([s for s in line.strip()])
	return diag, lws

def get_path(n):
	if n:
		return n
	else:
		return -1

def to_bin(lb):
	posibili = []
	mb = "".join("1" for i in range(lb))

	m = int(mb, 2)
	for i in range(m+1):
		b = bin(i)[2:].zfill(lb)
		posibili.append([int(j) for j in b])
	
	# print(posibili)
	return posibili

# --- cocktastic ---
import numpy as np

def counter():
	diag = []
	with open(path) as file:
		for line in file:
			if "^" in line:
				line = line.replace("^", "1")
				line = line.replace(".", "0")
				diag.append([int(s) for s in line.strip()])

	total = 2**len(diag)
	for i in range(len(diag)-1):
		for j in range(len(diag[i])):
			if diag[i][j]:
				if not diag[i+1][j-1]:
					total -= 2 * (len(diag)-i)
				elif not diag[i+1][j+1]:
					total -= 2 * (len(diag)-i)

	print(total)


def sadge():
	diag = []
	with open(path) as file:
		for line in file:
			lz = line.replace(".", "0")
			diag.append([s for s in lz.strip()])

	# for i in diag:
	# 	print(i)

	for i in range(1, len(diag)):
		for j in range(len(diag[i])):
			if diag[i-1][j] == "S":
				diag[i][j] = "1"
			elif diag[i-1][j].isdigit() and diag[i-1][j] != "0" and diag[i][j] != "^":
				diag[i][j] = str(int(diag[i][j]) + int(diag[i-1][j]))
			elif diag[i-1][j].isdigit() and diag[i-1][j] != "0" and diag[i][j] == "^":
				diag[i][j-1] = str(int(diag[i-1][j]) + int(diag[i][j-1]))
				diag[i][j+1] = str(int(diag[i-1][j]) + int(diag[i][j+1]))
	
	return sum(int(i) for i in diag[-1])

if __name__ == "__main__":
	s = beamer()
	print(s)

	# print("---")

	# q = quantum_beam()
	# print(q)

	print("---")

	s = sadge()
	print(s)