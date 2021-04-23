from itertools import combinations


def solution(orders, course):
    answer = []
    order_dict = {}

    for i in range(len(course)):
        for j in range(len(orders)):
            for c in combinations(orders[j], course[i]):
                cc = list(c)
                cc.sort()
                tmp = ''.join(cc)
                if tmp in order_dict:
                    order_dict[tmp] += 1
                else:
                    order_dict[tmp] = 1

    print(order_dict)
    for c in course:
        arr = []
        maxNum = 2
        for k, v in order_dict.items():
            if len(k) == c:
                if maxNum < v:
                    arr = [k]
                    maxNum = v
                elif maxNum == v:
                    arr.append(k)
        for i in range(len(arr)):
            answer.append(arr[i])

    answer.sort()

    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))