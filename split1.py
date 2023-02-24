s1 = "a b c d"
s2 = "a:b:c:d"
s3 = "abcd"

print(s1)
print(s1.split())           # 가장 기본적인 문자열 분할 방법
print(s1.split(maxsplit=1)) # maxsplit이 가리키는 횟수 만큼 분할횟수 제한 가능
print(s2.split(':'))        # 특정 문자열 ':'를 기준으로 문자열을 분할한다
print(list(s3))             # 문자열을 리스트 자료형으로 변환하여 개발 알파벳으로 분리