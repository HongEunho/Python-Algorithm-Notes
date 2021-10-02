from itertools import combinations_with_replacement


def solution(n, info):
    answer = []
    saveScore = []

    if info[0] == n:
        answer.append(-1)
        return answer

    scoreList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    allCombi = list(combinations_with_replacement(scoreList, n))

    for i in range(len(allCombi)):
        tmpScore = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(n):
            if allCombi[i][j] >= 0:
                tmpScore[10 - allCombi[i][j]] += 1

        aScore, bScore = 0, 0

        for j in range(len(info)):
            if info[j] >= tmpScore[j]:
                if info[j] != 0:
                    aScore += (10 - j)
            elif info[j] < tmpScore[j]:
                if tmpScore[j] != 0:
                    bScore += (10 - j)

        if bScore > aScore:
            if sum(tmpScore) == n:
                saveScore.append([tmpScore, bScore - aScore])

    if len(saveScore) == 0:
        answer.append(-1)
        return answer

    saveScore.sort(key=lambda x: x[0], reverse=True)
    saveScore.sort(key=lambda x: x[1])

    answer = saveScore[-1][0]

    return answer


print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
