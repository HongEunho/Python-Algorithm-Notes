import math

def distance(pt1, pt2):
    dist = abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])
    return dist


def solution(numbers, hand):
    answer = ''
    pad = [[3,1], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2], [3,0], [3,2]]
    myLeft = pad[10]
    myRight = pad[11]

    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            myLeft = pad[num]
        elif num in [3,6,9]:
            answer += 'R'
            myRight = pad[num]
        else:
            if distance(myLeft, pad[num]) < distance(myRight, pad[num]):
                answer += 'L'
                myLeft = pad[num]
            elif distance(myLeft, pad[num]) > distance(myRight, pad[num]):
                answer += 'R'
                myRight = pad[num]
            else:
                if hand == "left":
                    answer += 'L'
                    myLeft = pad[num]
                else:
                    answer += 'R'
                    myRight = pad[num]


    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))