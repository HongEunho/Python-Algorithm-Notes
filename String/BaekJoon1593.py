import sys
from itertools import permutations
n, m = map(int, input().split())
w = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

wl = [0] * 52
sl = [0] * 52

# w의 각 알파벳마다 등장하는 부분 +1
for i in range(n):
    if 'a' <= w[i] <= 'z':
        wl[ord(w[i]) - ord('a')] += 1
    else:
        wl[ord(w[i]) - ord('A') + 26] += 1

start, length, count = 0, 0, 0
for i in range(m-n+1):
    if 'a' <= s[i] <= 'z':
        sl[ord(s[i]) - ord('a')] += 1
    else:
        sl[ord(s[i]) - ord('A') + 26] += 1
    length += 1

    if length == n:
        if wl == sl:
            count+=1




count = 0

for per in permutations(w, len(w)):
    pers = "".join(per)
    for j in range(len(s)-len(w)):
        if s[j:j+len(w)] == pers:
            count+=1
            break

print(count)