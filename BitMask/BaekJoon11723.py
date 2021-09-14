import sys

m = int(sys.stdin.readline())

bit = 0
for i in range(m):
    comm = sys.stdin.readline().rstrip().split()

    if comm[0] == "all":
        bit = (1 << 20) - 1
    elif comm[0] == "empty":
        bit = 0
    else:
        op = comm[0]
        num = int(comm[1]) - 1

        if op == "add":
            bit |= (1 << num)
        elif op == "remove":
            bit &= ~(1 << num)
        elif op == "check":
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)

        elif op == "toggle":
            bit = bit ^ (1 << num)
