import sys
sys.setrecursionlimit(10000)

def allotRoom(num, roomDict):
    if num not in roomDict:
        roomDict[num] = num + 1
        return num

    emptyNum = allotRoom(roomDict[num], roomDict)
    roomDict[num] = roomDict[emptyNum]
    return emptyNum


def solution(k, room_number):
    answer = []
    roomDict = {}

    for num in room_number:
        allotRoom(num, roomDict)

    return list(roomDict.keys())