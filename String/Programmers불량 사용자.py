from itertools import permutations


def check(candidates, banned_id):
    for i in range(len(banned_id)):
        if len(candidates[i]) != len(banned_id[i]):
            return False
        for a, b in zip(candidates[i], banned_id[i]):
            if b == "*":
                continue
            if a != b:
                return False
    return True


def solution(user_id, banned_id):
    answer = []

    for candidates in permutations(user_id, len(banned_id)):
        if check(candidates, banned_id):
            candidates = set(candidates)
            if candidates not in answer:
                answer.append(candidates)

    return len(answer)

