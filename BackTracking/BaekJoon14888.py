n = int(input())
number = list(map(int, input().split()))
op = list(map(int, input().split()))
minR = int(1e9)
maxR = -int(1e9)

answer = number[0]

def dfs(idx):
    global answer
    global minR, maxR

    if idx == n:
        if answer > maxR:
            maxR = answer
        if answer < minR:
            minR = answer
        return

    for i in range(4):
        tmp = answer
        if op[i] > 0:
            if i == 0:
                answer += number[idx]
            elif i == 1:
                answer -= number[idx]
            elif i == 2:
                answer *= number[idx]
            else:
                if answer >= 0:
                    answer //= number[idx]
                else:
                    answer = (-answer // number[idx]) * -1

            op[i] -= 1
            dfs(idx+1)
            answer = tmp
            op[i] += 1


dfs(1)
print(maxR)
print(minR)