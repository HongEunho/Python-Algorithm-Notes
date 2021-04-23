from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in range(len(course)):
        order_list = []
        for j in range(len(orders)):
            for comb in combinations(sorted(orders[j]), course[i]):
                order_list.append("".join(comb))

        if order_list:
            order_list = Counter(order_list).most_common()
            maxCnt = order_list[0][1]

            for order in order_list:
                if order[1] == maxCnt and order[1] > 1:
                    answer.append(order[0])
                else:
                    break

        answer.sort()
    return answer
