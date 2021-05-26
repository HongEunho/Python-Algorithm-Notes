def solution(logs):
    answer = []
    logs.sort()
    length = len(logs)
    answer.append(9999)

    for i in logs:
        if i != answer[-1]:
            answer.append(i)
        else:
            answer.pop()
    answer.remove(9999)
    return answer

print(solution([23160, 23240, 23173, 23243, 23173, 23243]))
## 23160 23173 23173 23240 23243 23243