# 1. 문자열에 따옴표 포함
food = "Python's favorite food is perl" # 반드시 큰따옴표로 감싸기. 반대로 큰따옴표는 작은따옴표로 감싸기
# 혹은 역슬래시 이용
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

# 2. 여러 줄의 문자열을 한 변수에 입력
# 2-1) \n을 이용해 줄바꿈
multiline = "Life is too short\nYou need python"
# 2-2) 작은따옴표 나 큰따옴표 3개 이용 ( 보기 쉬움 )
multiline = '''
Life is too short
You need python
'''
print(multiline)

# 3. 문자열 더하기
head = "Python"
tail = " is fun!"
print(head + tail)

# 4. 문자열 곱하기
a = "python"
print(a*2)

# 5. 문자열 슬라이싱
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

# 6. 문자열 편집
a = "Pithon"
print(a[:1] + 'y' + a[2:]) #P + y + thon

# 7. 문자열 포매팅 (C의 %d, %s와 개념 비슷)
eat = "I eat %d apples." % 3
eat2 = "I eat %s apples." % "five"
eat3 = "I eat %s apples." % 5 # %s를 붙이면 뒤에 정수나 실수가 오더라도 자동으로 문자열로 치환
print(eat3)

