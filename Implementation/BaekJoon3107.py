ip = list(input().split(":"))

index = 0
ans = ['' for _ in range(8)]
flag = 0

for i in range(len(ip)):
    if len(ip[i]) == 4:
        ans[index] = ip[i]
        index += 1

    elif len(ip[i]) > 0:
        ans[index] = '0' * (4 - len(ip[i])) + ip[i]
        index += 1

    else: # len(ip[i]) == 0
        if flag == 0:
            for j in range(8 - len(ip) + 1):
                ans[index] = '0000'
                index += 1
            flag = 1
        else:
            ans[index] = '0000'
            index += 1

for i in range(len(ans)-1):
    print(ans[i], end=':')

print(ans[-1])