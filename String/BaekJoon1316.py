n = int(input())

cnt = 0
for i in range(n):
    tmp = input()
    alpha = []
    flag = 0
    for j in tmp:
        if j not in alpha:
            alpha.append(j)
        else:
            if alpha[-1] == j:
                flag = 0
            else:
                flag = 1
                break
    if flag == 0:
        cnt += 1

print(cnt)