def solution(k, room_number):
    answer = []
    roomDict = {}

    for num in room_number:
        visited = [num]
        while num in roomDict:
            num = roomDict[num]
            visited.append(num)

        answer.append(num)
        for i in visited:
            roomDict[i] = num + 1

    return list(answer)