# --- Day 8: Playground ---
# --- with DSU ---
# Robin Jack

from collections import defaultdict

path = "inputs/day8.txt"

connections_to_make = 1000

def parse():
	boxes = []
	with open(path, "r") as file:
		for i, line in enumerate(file):
			b = Box([int(p) for p in line.split(",")], i)
			boxes.append(b)
	return boxes

class Box:
	def __init__(self, box, index):
		self.x, self.y, self.z = box
		self.index = index

	# distance    
	def __sub__(self, other):
		return (
			(self.x - other.x)**2 +
			(self.y - other.y)**2 +
			(self.z - other.z)**2
		)

	def __repr__(self):
		return f"Box{self.index} [{self.x, self.y, self.z}]"

class DSU:
	def __init__(self, n):
		self.parent = list(range(n))
		self.size = [1] * n

	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, a, b):
		ra = self.find(a)
		rb = self.find(b)

		if ra == rb:
			return False  # already connected

		# attach smaller to larger
		if self.size[ra] < self.size[rb]:
			ra, rb = rb, ra

		self.parent[rb] = ra
		self.size[ra] += self.size[rb]
		return True

# --- --- ---

def kruskal(boxes, n):
	edges = []
	for i in range(n):
		for j in range(i+1, n):
			d = boxes[i] - boxes[j]
			edges.append((d, i, j))
	edges.sort()
	return edges

def connect_closest(dsu, n, edges):
	for d, i, j in edges[:connections_to_make]:
		dsu.union(i, j)

	return dsu

def get_components(dsu, n):
	groups = defaultdict(list)

	for i in range(n):
		root = dsu.find(i)
		groups[root].append(i)

	multi = 1
	for i in range(3):
		key, lg = max(groups.items(), key=lambda item: len(item[1]))
		multi *= len(lg)
		groups.pop(key)

	# print(multi, list(groups.values()))
	return multi

def connect_closest_all(dsu, n, edges):
	merges = 0
	for d, i, j in edges:
		if dsu.union(i, j):
			merges += 1
			if merges == n-1:
				break

	# print(boxes[i].x, boxes[j].x)
	x_last_two = boxes[i].x * boxes[j].x
	return x_last_two

if __name__ == "__main__":
	boxes = parse()
	n = len(boxes)
	dsu = DSU(n)
	edges = kruskal(boxes, n)

	# -- results --
	dsu = connect_closest(dsu, n, edges)
	re = get_components(dsu, n)
	print(re)

	print("---")

	ndsu = DSU(n)
	x = connect_closest_all(ndsu, n, edges)
	print(x)
