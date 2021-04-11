n = int(input())
answer = 0

if n < 100:
    answer = n
else:
    cnt = 0
    for i in range(101, n+1):
        flag = 0
        strn = str(i)
        tmp = int(strn[0]) - int(strn[1])
        for j in range(1, len(strn) - 1):
            if (int(strn[j]) - int(strn[j+1])) != tmp:
                flag = 1
                break
        if flag == 0:
            cnt += 1
    answer = cnt + 99

print(answer)
