def step2(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            return p[:i+1], p[i+1:]

def step3(u):
    stack = []
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    answer = ''
    #step1
    if not p:
        return ''

    #step2
    u, v = step2(p)

    #step3
    if step3(u):
        return u+solution(v)

    #step4
    #4-1
    answer += "("

    #4-2
    answer += solution(v)

    #4-3
    answer += ")"

    #4-4
    for i in u[1:-1]:
        if i == "(":
            answer += ")"
        else:
            answer += "("
    #4-5
    return answer

print(solution("(()())()"))
