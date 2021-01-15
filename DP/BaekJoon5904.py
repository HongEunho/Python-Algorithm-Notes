n = int(input())

k = 1 # k번째 인덱스
s = 3 # 전체 문자열의 길이(시작은 "moo"이므로 3)

while n > s: # 목표 인덱스가 전체 문자열의 길이보다 긴 경우는 계속해서 늘려줘야 한다.
    s = s * 2 + (k + 3) # S(k) = S(k-1) + "m"+(k+2)*o + S(k-1) 이므로
    k += 1

k = k-1 # 마지막 k += 1을 취소하기 위해

while True:
    pre_len = (s - (k + 3)) / 2
    if n <= pre_len: # 본 문자열 앞에 위치한 경우. 즉, 위 식에서 앞의 S(k-1)에 해당
        k -= 1
        s = pre_len

    elif n > pre_len + ( k + 3 ): # 본 문자열 뒤에 위치한 경우. 즉, 위 식에서 뒤의 S(k-1)에 해당
        n = n - (pre_len + (k + 3)) # 이전 문자열들은 싹 다 지워준다. 즉 하나의 S(k-1)의 길이만 남겨둠
        k -= 1
        s = pre_len

    else: # 본 문자열 사이에 있는 경우. 즉 "m"+(k+2)*o 라는 문자열 사이에 위치한 경우
        n = n - pre_len
        break

if n == 1:
    print('m')
else:
    print('o')

