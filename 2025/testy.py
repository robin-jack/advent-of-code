# x = 1
# for i in range(-1, 2):
# 	row = x+i
# 	print(row)

# grid = [[0, 0, 1, 1, 0, 1, 1, 1, 1, 0], [1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 1, 0, 1, 1]]
# for x in range(len(grid)):
# 	for i in range(-1, 2):
# 		row = grid[x+i] if 0 <= x+i < len(grid) else [0]
# 		print(row)
# 		print("---")

# print(grid[1][3])

# a = [[1, 2], [3, 4]]
# for i, j in a:
# 	print(i, j)


# x = "3-5"
# r = [int(n) for n in x.split("-")]
# w = (3, 5)
# for i in range(w[0], w[1]+1):
# 	print(i)

# |------
# 54-88
# 335-520
# 18-33
# 1-6
# 220-370
# 31-58
# 3-5
# 122-275
# 14-25
# 4-5
# 96-195
# 2-5
# 14-25
# 3-6
# 14-14
# 96-195
# -------
# 10 < n < 33
# -------
# = 506
# ------|
# #315756831755628
# #328555103327415

# a = "* +  +   * *    +    *"

# b = a.split()

# print(b)
# print(b.count("*"))

# a = [[1], [2], [3], [4], [5], [6], [7], [8]]

# b = "2"
# a[0] = 3
# print(a[0])

# if int("1"):
# 	print("aaa")

# print("011213331311110")
# x = "011213331311110"
# print(sum(int(i) for i in x))


a = [[2, 3], [4, 5], [5, 7]]

x = [5 in x for x in a]

mom = []
b = [2, 3]
mom.append(b)
print(mom)

s = 0
for i in range(20):
	s += i
print(s)