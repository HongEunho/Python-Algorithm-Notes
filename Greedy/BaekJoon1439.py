import sys
a = sys.stdin.readline().rstrip()

b = a.split("0")
c = a.split("1")

b2 = b.count('')
c2 = c.count('')


print(min(len(b)-b2, len(c)-c2))