def solution(new_id):
    answer = ''
    answer = new_id.lower();
    answer = "asd"
    answer2 = ''
    for i in answer:
        if i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.':
            answer2 += i

    return answer