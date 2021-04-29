n = int(input())
num = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

mymax = int(1e9)
mymin = int(-1e9)

def dfs(index, result):
    global mymax, mymin
    if index == n:
        mymax = max(mymax, result)
        mymin = min(mymin, result)

    

dfs(1, num[0])




