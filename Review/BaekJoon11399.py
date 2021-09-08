n = int(input())
people = list(map(int, input().split()))

people.sort()

result = 0
for i in range(n):
    result += sum(people[:i+1])

print(result)