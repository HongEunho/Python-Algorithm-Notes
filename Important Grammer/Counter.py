from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

a = ['a', 'b', 'c', 'd', 'a', 'a', 'b']
counter2 = Counter(a)

print(counter['blue'])  # 'blue'가 등장한 횟수
print(counter['green']) # 'green'
print(dict(counter)) # 사전 자료형으로 변환
print(counter)
print(counter2['a']) # Counter의 기능을 사용하고 싶으면 []를 이용하여 []안에 요소 입력. ()가 아님