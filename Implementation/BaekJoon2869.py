import math
a, b, v = map(int, input().split())

answer = math.ceil((v-b) / (a-b))

print(answer)

