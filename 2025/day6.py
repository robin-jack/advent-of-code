# --- Day 6: Trash Compactor ---
# Robin Jack

path = "inputs/day6.txt"

def operations():
    ops = None
    with open(path, "r") as file:
        for line in file:
            ops = line

    # print(ops.split())
    return ops.split()

def mathy():
    total = 0

    ops = operations()
    for i in range(len(ops)):
        with open(path, "r") as file:
            subto = 1
            for line in file:
                if "*" in line:
                    break
                num = int(line.split()[i])
                subto = do_ope(subto, num, ops[i])
            total += subto

    # subtract 1 for each ops sum to offset subto = 1
    total -= ops.count("+")
    # print(total)
    return total

def do_ope(subto, num, ope):
    if ope == "+":
        subto += num
    else:
        subto *= num
    return subto


if __name__ == "__main__":
    t = mathy()
    print(t)