# --- Day 8: Playground ---

import math

path = "inputs/day8.txt"

connections_to_make = 1000

class Box:

	length = 0

	def __init__(self, box, index):
		self.x = box[0]
		self.y = box[1]
		self.z = box[2]
		self.index = index+1
		self.name = f"Box n.{self.index}"
		self.connections = set()
		self.circuit = {self}

	def __sub__(self, other):
		return math.sqrt(
		    (self.x - other.x)**2 +
		    (self.y - other.y)**2 +
		    (self.z - other.z)**2
		)

	def connect(self, other):
		self.connections.add(other)
		other.connections.add(self)

		self.circuit = find_connected(self)
		other.circuit = find_connected(other)

		if len(self.circuit) == self.length:
			answer = self.x * other.x
			return True, answer
		else:
			return False, 0

	def connected(self, other):
		return other in self.connections

	def size(self):
		return len(self.circuit)

	def __lt__(self, other):
		return self.index < other.index

	def __str__(self):
		return self.name

	def __repr__(self):
		conns = " ".join([str(i.index) for i in sorted(self.connections)])
		p = f"{self.name}\n" \
			f"[{self.x}, {self.y}, {self.z}]\n" \
			f"Connected to: {conns}\n" \
			f"Circuit Length: {len(self.circuit)}\n"
		return p

# --- --- ---

def parse():
	positions = []
	with open(path, "r") as file:
		i = 0
		for line in file:
			b = Box([int(p) for p in line.split(",")], i)
			positions.append(b)
			i += 1
	return positions

def find_connected(box, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(box)
    
    neighbors = box.connections
    
    for neighbor in neighbors:
        if neighbor not in visited:
            find_connected(neighbor, visited)
            
    return list(visited)

def closest():
	box = parse()
	for k in range(connections_to_make): 
		closest = float('inf')
		cbox = []
		for i in range(len(box)):
			p1 = box[i]
			for j in range(i+1, len(box)):
				p2 = box[j]
				d = p1 - p2
				if not p1.connected(p2) and d < closest:
					closest = d
					cbox = [p1, p2]
		cbox[0].connect(cbox[1])
		# print(k)

	return box

def circuiter(boxes):
	circuits = []
	for box in boxes:
		# print(repr(box))
		if not any(box in cc for cc in circuits):
			circuit = find_connected(box)
			circuits.append(circuit)
	# print([len(c) for c in circuits])

	multi = 1
	last = float('inf')
	for i in range(3):
		blen = 0
		for cir in circuits:
			if last > len(cir) > blen:
				blen = len(cir)
		last = blen
		multi *= blen

	print(multi)

# --- Part Two ---

def connect_all():
	box = parse()
	Box.length = len(box)
	result = 0
	one_circuit = False
	k = 0
	while(not one_circuit):
		closest = float('inf')
		cbox = []
		for i in range(len(box)):
			p1 = box[i]
			for j in range(i+1, len(box)):
				p2 = box[j]
				d = p1 - p2
				if not p1.connected(p2) and d < closest:
					closest = d
					cbox = [p1, p2]
		one_circuit, result = cbox[0].connect(cbox[1])
		print(k)
		k+=1


	return result


if __name__ == "__main__":
	# boxes = closest()
	# circuiter(boxes)

	# print("---")

	result = connect_all()
	print(result)

