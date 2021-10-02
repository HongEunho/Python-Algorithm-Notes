import sys
n = int(input())

member = []
for i in range(n):
    member.append(sys.stdin.readline().rstrip().split(" "))

member.sort(key=lambda x:int(x[0]))

for i in range(n):
    print("%s %s" %(member[i][0], member[i][1]))
