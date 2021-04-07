exp = input()
ans = ''

flag = 0 # 괄호 열기전
for i in range(len(exp)):
    if exp[i] == '-':
        if flag == 0:
            ans += exp[i]
            ans += "("
            flag = 1
        else:
            ans += ")"
            ans += exp[i]
            ans += "("
    else:
        ans += exp[i]

if flag == 1:
    ans += ")"
print(ans)
print(eval(ans))