n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort()

maxWeight = rope[0]*n

for i in range(1, n):
    if maxWeight < rope[i] * (n-i) :
        maxWeight = rope[i] * (n-i)

print(maxWeight)
