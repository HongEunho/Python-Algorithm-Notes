import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<": # 열린 괄호를 만나면
        i += 1 # 다음 칸 부터 닫힌 괄호를 찾는다
        while word[i] != ">": # 닫힌 괄호를 만날 때 까지
            i += 1 # 인덱스를 증가한다.
        i += 1 # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i # 시작점을 기준으로 두고
        while i < len(word) and word[i].isalnum(): # 숫자나 알파벳이 아닐 때 까지
            i+=1 # 인덱스를 계속 증가시킨다
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse() # 뒤집어서
        word[start:i] = tmp # 교체한다
    else: # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1 # 그냥 증가시킨다

print("".join(word))