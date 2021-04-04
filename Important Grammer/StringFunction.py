a = "hobby"
print(a.count('b')) # 문자의 개수 세는 함수 count

ex1 = "Python is the best choice"
print(ex1.find('b')) # ex1라는 문자열 안에서 'b'의 처음 등장 위치
print(ex1.find('k')) # 없으면 -1 반환

#find와 비슷한 함수로 index가 있는데. index는 없으면 -1 대신 오류를 반환한다.
print(ex1.index('b'))
# print(ex1.index('k')) 오류 반환

print(",".join('abcd')) # abcd 문자열 사이에 , 삽입

hismall = "hi"
print(hismall.upper()) # hi를 대문자로
print(hismall)
hibig = "HI"
print(hibig.lower()) # HI를 소문자로

astrip = "   hi   "
astrip.lstrip() #왼쪽 공백 제거
astrip.rstrip() #오른쪽 공백 제거
astrip.strip() #양쪽 공백 제거

sen = "Life is too short"
sen.replace("Life", "Your leg") #Life문자열을 your leg로 변경

k = "Life is too short"
k.split() # ['Life', 'is', 'too', 'short] Life문자열을 공백을 기준으로 나눠서 리스트로 저장
k2 = "a:b:c:d"
k2.split(":") # ['a', 'b', 'c', 'd'] ":"를 기준으로 나눠 문자열에 저장

k.isspace() # 공백으로만 이루어졌는지
k.isdigit() # 숫자인지
k.isalpha() # 영문자인지
k.isalnum() # 영문자 혹은 숫자인지
k.istitle() # 모든 단어의 첫 글자가 대문자인지

