# 문자열 형태로 수식을 입력하면 자동 계산해주는 eval 함수
result = eval(" ( 3 + 5 ) * 7 ")
print(result)

# iterable 객체가 들어왔을 때, 정렬된 결과를 반환해주는 sorted 함수
result = sorted([9, 1, 8, 5, 4])  # result.sort()와 같은 효과
print(result)
result = sorted([9, 1, 8, 5, 4], reverse=True)  # 역순으로
print(result)

# key값을 이용하여 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x: x[1], reverse=True)
