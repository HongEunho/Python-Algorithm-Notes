def solution(name):
    answer = 0
    diff = [min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1) for i in range(len(name))]
    i = 0

    while True:
        answer += diff[i]
        diff[i] = 0

        if sum(diff) == 0:
            return answer

        left, right = 1, 1

        for j in range(1, len(name)):
            if diff[i + j] == 0:
                right += 1
            else:
                break

        for j in range(1, len(name)):
            if diff[i - j] == 0:
                left += 1
            else:
                break

        if left >= right:
            answer += right
            i += right
        else:
            answer += left
            i -= left

    return answer

print(solution("ABC"))