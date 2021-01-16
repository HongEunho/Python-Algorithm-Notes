# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
# 호어 분할 방식을 기준으로 피봇 설정 ( 리스트의 첫 번째 데이터)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 부분은 정렬이 완료되었으므로 종료
        return
    pivot = start  # 첫 번째 원소를 피봇으로 설정
    left = start + 1  # 피벗 다음 칸 부터 왼쪽시작
    right = end  # 마지막 원소부터 오른쪽 시작
    while left <= right:  # 엇갈리기 전까지
        while left <= end and array[left] <= array[pivot]:  # 피봇보다 큰 데이터를 찾기 까지
            left += 1
        while right > start and array[right] >= array[pivot]:  # 피봇보다 작은 데이터를 찾기 까지
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피봇을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
