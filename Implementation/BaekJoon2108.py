import math
from collections import Counter
n = int(input())

numList = []
for i in range(n):
    numList.append(int(input()))


print(round(sum(numList) / n))
numList.sort()
print(numList[n//2])
cnt = Counter(numList)
tmp = cnt.most_common()

if len(tmp) > 1:
    if tmp[0][1] == tmp[1][1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
else:
    print(tmp[0][0])

print(max(numList) - min(numList))
