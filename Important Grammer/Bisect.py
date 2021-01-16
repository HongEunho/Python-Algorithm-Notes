from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))  # 정렬된 리스트에서 데이터 x를 삽입할 가장 왼쪽 인덱스
print(bisect_right(a, x))  # 정렬된 리스트에서 데이터 x를 삽입할 가장 오른쪽 인덱스


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(whole_range, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


whole_range = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(whole_range, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(whole_range, -1, 3))
