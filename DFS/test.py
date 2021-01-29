trace = []
trace.append((2,3))
trace.append((3,4))
trace.append((5,2))
trace.append((1,6))
result = (min(trace, key = lambda x: x[0]))[1]
print(result)

new_graph = [1,2,'X']
tmp = [i for i, value in enumerate(new_graph) if value == 'X']

print(min(tmp))