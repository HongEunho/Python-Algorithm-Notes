
x2List = [0,1,0,1]
x1List = [0,0,1,1]

countList = [0]*(d+1)
countList[d] = k

answer1, answer2 = 1,1

flag = 0

for i in range(4, d+1):
    x2List.append(x2List[i-1]+x1List[i-1])
    x1List.append(x2List[i-1])

for i in range(1, int(k/2)):
    for j in range(i+1, int(k/2)):
        if k == (x2List[-1]*j + x1List[-1]*i):
            flag = 1
            break
    answer2 = j
    answer1 = i
    if flag == 1:
        break

print(answer1)
print(answer2)

