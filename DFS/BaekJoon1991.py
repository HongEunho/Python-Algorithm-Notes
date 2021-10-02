n = int(input())

graph = [[[] for _ in range(2)] for _ in range(26)]


def pre_order(root):
    print(chr(root + ord('A')), end='')
    if graph[root][0]:
        pre_order(graph[root][0][0])
    if graph[root][1]:
        pre_order(graph[root][1][0])

def in_order(root):
    if graph[root][0]:
        in_order(graph[root][0][0])
    print(chr(root + ord('A')), end='')
    if graph[root][1]:
        in_order(graph[root][1][0])

def post_order(root):
    if graph[root][0]:
        post_order(graph[root][0][0])
    if graph[root][1]:
        post_order(graph[root][1][0])
    print(chr(root + ord('A')), end='')

for i in range(n):
    a, b, c = input().split()

    if b != ".":
        graph[ord(a) - ord('A')][0].append(ord(b) - ord('A'))
    if c != ".":
        graph[ord(a) - ord('A')][1].append(ord(c) - ord('A'))


pre_order(0)
print()
in_order(0)
print()
post_order(0)
