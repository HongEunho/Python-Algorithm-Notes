n = int(input())

room = []
for i in range(n):
    start, end = map(int, input().split())
    room.append([start, end])

room.sort(key=lambda x: x[0])
room.sort(key=lambda x: x[1])

result = 1
before_end = room[0][1]

for i in range(1, n):
    if room[i][0] >= before_end:
        result += 1
        before_end = room[i][1]

print(result)