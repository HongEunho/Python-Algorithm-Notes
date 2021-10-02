import sys
n = int(input())

word = []
for i in range(n):
    a = sys.stdin.readline().rstrip()

    if a not in word:
        word.append(a)

word.sort()
word.sort(key=lambda x:len(x))

for i in word:
    print(i)