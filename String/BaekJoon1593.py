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

for i in range(m):
    if 'a' <= s[i] <= 'z':
        sl[ord(s[i]) - ord('a')] += 1
    else:
        sl[ord(s[i]) - ord('A') + 26] += 1
    length += 1

    if length == n:
        if wl == sl:
            count+=1
        if 'a' <= s[start] <= 'z':
            sl[ord(s[start]) - ord('a')] -= 1
        else:
            sl[ord(s[start]) - ord('A') + 26] -= 1
        start += 1
        length -= 1


print(count)