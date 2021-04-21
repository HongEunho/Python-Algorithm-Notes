def solution(user_id, banned_id):
    answer = []
    candidates = [[]]
    for ban in banned_id:
        tmp_can=[]
        for user in user_id:
            flag = True
            if len(ban) != len(user):
                continue
            for i in range(user):
                if ban[i] == "*":
                    continue
                if ban[i] != user[i]:
                    flag = False
                    break
            if flag:
                for can in candidates:
                    if user not in can:
                        tmp_can.append(can+[user])

        candidates = tmp_can

    for i in candidates:
        if set(i) not in answer:
            answer.append(set(i))

    return len(answer)