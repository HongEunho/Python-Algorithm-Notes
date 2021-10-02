x, y, w, h = map(int, input().split())

a = min(w-x, x)
b = min(h-y, y)

print(min(a, b))