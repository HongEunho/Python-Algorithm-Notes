def solution(n, k, cmd):
    answer = ''

    linkedList = {i: [i-1, i+1] for i in range(1, n+1)}
    OX = ["O" for i in range(1, n+1)]

    stack = []

    k += 1

    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = linkedList[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = linkedList[k][0]
        elif c[0] == 'C':
            prev, next = linkedList[k]
            stack.append([prev, next, k])
            OX[k-1] = "X"

            if next == n+1:
                k = linkedList[k][0]
            else:
                k = linkedList[k][1]

            if prev == 0:
                linkedList[next][0] = prev
            elif next == n+1:
                linkedList[prev][1] = next
            else:
                linkedList[prev][1] = next
                linkedList[next][0] = prev

        elif c[0] == 'Z':
            prev, next, now = stack.pop()
            OX[now-1] = 'O'

            if prev == 0:
                linkedList[next][0] = now
            elif next == n+1:
                linkedList[prev][1] = now
            else:
                linkedList[prev][1] = now
                linkedList[next][0] = now

    return "".join(OX)

    return answer