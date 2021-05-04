def solution(gems):
    answer = []
    setlen = len(set(gems)) # 보석의 종류수
    gemdict = {} # 보석 종류별로 개수를 셀 딕셔너리

    start = 0 # 투 포인터의 시작점
    end = 0 # 끝점
    sect = len(gems)+1

    while end < len(gems): # 끝점이 범위안에 있을 때만 검사

        if gems[end] not in gemdict: # 새로 발견한 보석
            gemdict[gems[end]] = 1
        else: # 기존에 존재하는 보석
            gemdict[gems[end]] += 1

        end += 1 #보석을 새로 추가했으니 end칸 한 칸 뒤로

        if len(gemdict) == setlen: # 범위안에 모든 보석이 존재할 때
            while start < end:
                if gemdict[gems[start]] > 1:  # 하나 이상 존재하면 뒤에도 더 존재한다는 뜻이므로
                    gemdict[gems[start]] -= 1  # 하나를 제거해주고
                    start += 1  # start칸을 뒤로 한칸 이동
                elif end-start < sect: # 지정한 구간보다 현재 구간이 짧으면
                    sect = end-start # 지정한 구간 바꿔주기
                    answer = [start+1, end]
                    break
                else:
                    break

    return answer

print(solution(["XYZ", "XYZ", "XYZ"]))