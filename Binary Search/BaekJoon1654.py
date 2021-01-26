k, n = map(int, input().split())
lan = []

maxcm = 0


def binary_search(array, target, start, end):
    while start <= end:
        moksum = 0
        mid = (start + end) // 2
        if mid == 0:
            return start        # 0값을 나누는 예외상황 처리
        for i in array:
            mok = i // mid
            moksum += mok
        if moksum < target:  # 개수를 더 늘려야 하므로 길이를 줄이자
            end = mid - 1
        elif moksum >= target:  # 개수를 더 줄일 수 있으므로 길이를 늘리자
            start = mid + 1

    return end


for i in range(k):
    lan.append(int(input()))

lansum = sum(lan)  # 입력받은 모든 랜선 길이의 합


result = binary_search(lan, n, 0, lansum) # 길이 배열, 만들어야 하는 랜선수, 시작값, 끝값
print(result)
