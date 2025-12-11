# --- Day 6: Trash Compactor ---
# Robin Jack

path = "tests/day6.txt"

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

def create_num_list():
    ops = None
    with open(path, "r") as file:
        for line in file:
            ops = list(line)

    # +  *  +    *
    # -----------
    for i in range(len(ops)):
        if i == 0:
            pass
        else:
            try:
                if (ops[i-1] != " " and ops[i+1] == " "):
                    ops[i] = ops[i-1]
            except IndexError:
                ops[i] = ops[i-1]
    # -----------
    num_list = []
    with open(path, "r") as file:
        for line in file:
            if "*" in line:
                break
            num_list.append(list(line.strip("\n")))
    num_list = num_list_zerofier(num_list, ops)
    # print(num_list)
    for x in num_list:
        for y in x:
            if y == " ":
                x.remove(" ")
    for z in ops:
        if z == " ":
            ops.remove(z)
    print("ops:\n", ops)
    print("num_list:")
    for n in num_list:
        print(n)
    # -----------
    total = []
    for j in range(len(ops)):
        if ops[j] == "+":
            total.append(0)
        elif ops[j] == "*":
            total.append(1)
    print("total:\n", total)

    return total, num_list, ops

def num_list_zerofier(nums, ops):
    for sub in nums:
        for i in range(len(sub)):
            if sub[i] == " " and ops[i] != " ":
                if ops[i]:
                    sub[i] = '0'
    return nums

def manipulator():
    total, num_list, ops = create_num_list()

    for i in range(len(num_list)):
        for j in range(len(num_list[i])):
            total[j] = calcolo(total[j], num_list[i][j], ops[j])

    print(total)


def calcolo(subto, n, ope):
    if n != " ":
        if ope == "+":
            subto += int(n)
        else:
            subto *= int(n)
        return subto
    else:
        return 0


if __name__ == "__main__":
    # t = mathy()
    # print(t)

    print("---")

    manipulator()