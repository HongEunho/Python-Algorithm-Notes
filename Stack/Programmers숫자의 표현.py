def solution(n):
    answer = 0
    for i in range(1, n + 1):
        stack = []
        for j in range(i, n + 1):
            stack.append(j)
            if sum(stack) >= n:
                break
        if sum(stack) == n:
            answer += 1

    return answer

print(solution(15))