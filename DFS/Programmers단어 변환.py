def bfs(begin, target, words, visited):
    count = 0
    stack = [begin]
    while stack:
        cur = stack.pop()
        if cur == target:
            return count

        for i in range(len(words)):
            if visited[i] == True:
                continue
            cnt = 0
            for a, b in zip(cur, words[i]):
                if a != b:
                    cnt += 1
            if cnt == 1:
                visited[i] = True
                stack.append(words[i])
        count += 1


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    visited = [False] * (len(words))

    answer = bfs(begin, target, words, visited)

    return answer