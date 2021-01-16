from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

# 순열(리스트 처럼 iterable 객체에서 r개를 뽑아 일렬로 나열하는 모든 경우를 나열)
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # permutations는 클래스이므로 객체 초기화 이후에 리스트 자료형으로 변환해야 한다.
print(result)


# 조합(combinations)
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

# 중복순열(product)
data = ['A', 'B', 'C']
result = list(product(data, repeat=2)) # 2개를 뽑음(repeat으로 설정)
print(result)

# 중복조합(combinations_with_replacement)
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)

