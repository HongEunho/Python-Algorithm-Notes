import sys
while True:
    sen = sys.stdin.readline().rstrip()
    flag = 0
    stack = []
    if sen == '.':
        break
    for i in sen:
        if i == "(" or i == "[": #열린 괄호면 스택에 넣어준다.
            stack.append(i)
        elif i == ")": #닫는 소괄호가 등장했을 때
            if not stack or stack[-1] == "[": #열린 괄호가 없거나 열린 대괄호가 나오면
                print("no")
                flag = 1
                break
            else:
                stack.pop()
        elif i == "]": # 닫는 대괄호가 등장했을 때
            if not stack or stack[-1] == "(": #열린 괄호가 없거나 열린 소괄호가 나오면
                print("no")
                flag = 1
                break
            else:
                stack.pop()
    if flag == 0:   #앞서 no가 등장하지 않았을 때
        if not stack :  #스택이 비어있다 = 모든 괄호가 짝을 맞췄다
            print("yes")
        else:
            print("no")

