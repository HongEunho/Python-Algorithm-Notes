import re

def solution(new_id):
    answer = ''
    answer = new_id.lower()
    answer = re.sub('[^a-z0-9\-\_\.]', '', answer)
    answer = re.sub('\.{2,}', '.', answer)
    answer = re.sub('^\.|\.$', '', answer)
    answer = "a" if answer== '' else answer
    answer = answer[:15] if len(answer) >= 16 else answer
    answer = re.sub('\.$', '', answer)

    while len(answer) < 3:
        answer+=answer[-1]
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))