while True:
    length = list(map(int, input().split()))
    if length[0] == 0 and length[1] == 0 and length[2] == 0:
        break
    length.sort()
    if length[2]*length[2] == length[1]*length[1] + length[0]*length[0]:
        print("right")
    else:
        print("wrong")