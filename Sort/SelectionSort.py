array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스왑

# 이 선택정렬은 시간복잡도가 O(N^2)이다.
# N - 1 번만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 하고 매 번 가장 작은 수를 찾기 위해 비교 연산이 필요하기 때문이다.

# 선택 정렬은 무작위의 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
# 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하는 과정이다.