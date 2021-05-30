from itertools import combinations


def solution(number, k):
    answer = ''
    length = len(number)

    a = list(combinations(number, length - 2))
    b = []
    for i in range(len(a)):
        b.append("".join(a[i]))

    return max(b)

print(solution("1231234", 3))