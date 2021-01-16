array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나의 원소만을 가지고 있으면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))