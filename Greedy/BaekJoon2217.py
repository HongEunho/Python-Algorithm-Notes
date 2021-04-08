n = int(input())
rope = []

for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)

for i in range(n):
    rope[i] = rope[i] * (i+1)

print(max(rope))