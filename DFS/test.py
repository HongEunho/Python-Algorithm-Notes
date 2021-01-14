from collections import deque
import copy

queue = deque()
queue.append((1,2))
queue2 = copy.deepcopy(queue)
print(queue)
print(queue2)