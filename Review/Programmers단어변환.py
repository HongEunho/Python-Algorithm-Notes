def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    visited = [0] * len(words)

    def bfs():
        count = 0
        stack = [begin]

        while stack:
            cur = stack.pop()
            if cur == target:
                return count

            for i in range(len(words)):
                if visited[i] == 1:
                    continue

                cnt = 0
                for a, b in zip(cur, words[i]):
                    if a != b:
                        cnt += 1

                if cnt == 1:
                    visited[i] = 1
                    stack.append(words[i])

            count += 1


    return bfs()


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
