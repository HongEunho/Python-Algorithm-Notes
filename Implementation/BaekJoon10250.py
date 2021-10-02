t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    floor = n % h
    if floor == 0:
        floor = h
    hosu = (n - 1) // h + 1
    if hosu < 10:
        hosu = "0" + str(hosu)

    answer = str(floor) + str(hosu)
    print(answer)