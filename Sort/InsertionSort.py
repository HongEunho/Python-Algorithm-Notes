# 삽입 정렬은 특정한 데이터를 적절한 위치에 삽입하는 개념인데
# 자신의 위치를 찾았다면 그 위치보다 앞에 있는 원소들은 이미 정렬되어 있다고 가정한다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 두 번째 원소부터 자신의 앞칸 원소와 비교하며 자리를 찾아간다.
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)

# 선택 정렬과 마찬가지로 시간복잡도는 O(N^2)이다.
# 하지만 리스트의 데이터가 거의 정렬되어 있는 상태라면 거의 O(N)에 가까울 정도로 매우 빠르게 동작한다.
