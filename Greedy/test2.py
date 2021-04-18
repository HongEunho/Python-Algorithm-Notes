from collections import deque
import sys

arr = sys.stdin.readline().rstrip()[1:-1].split(",")
queue = deque(arr)
print(queue)
