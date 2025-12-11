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

# --- Part Two ---

def get_nums():
    num_list = []
    with open(path, "r") as file:
        for line in file:
            if "*" in line:
                break
            num_list.append(list(line.strip("\n")))
    # for i in num_list:
    #   print(i)
    
    fil = len(num_list)
    col = len(num_list[0])
    transpuesta = []
    # print("---")
    for i in range(col):
        concat = "" # [ [], [], [], []]
        for j in range(fil):
            #print(f"{transpuesta[j]} = {transpuesta[j][0]} + {num_list[j][i]}")
            concat += num_list[j][i].strip()
        transpuesta.append(concat)
    
    # print(transpuesta)
    # print("---")

    ops = operations()
    total = []
    for j in range(len(ops)):
        if ops[j] == "+":
            total.append([0])
        elif ops[j] == "*":
            total.append([1])
    # print(total)

    o = 0
    while (o < len(ops)-1):
        for n in transpuesta:
            if n == "":
                o += 1
            elif ops[o] == "*":
                # print(f"{total[o]} = [{int(n)} * {total[o][0]}]")
                total[o] = [int(n) * total[o][0]]
            else:
                # print(f"{total[o]} = [{int(n)} + {total[o][0]}]")
                total[o] = [int(n) + total[o][0]]

    # print(total)
    total_sum = sum(i[0] for i in total)
    # print(total_sum)
    return total_sum


if __name__ == "__main__":
    t = mathy()
    print(t)

    print("---")

    n = get_nums()
    print(n)