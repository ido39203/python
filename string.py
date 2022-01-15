str=input("문자열을 입력하시오: ")  #문자열 입력
a=0  #알파벳 개수
d=0  #숫자 개수
s=0  #스페이스(공백) 개수

for c in str:  #문자열 str의 각 문자 중에서
  if c.isalpha():  #알파벳인 경우
    a=a+1  #알파벳 추가
  elif c.isdigit():  #숫자인 경우
    d=d+1  #숫자 추가
  elif c.isspace():  #스페이스인 경우
    s=s+1  #스페이스 추가

print("알파벳 문자의 개수=%d"%a)  #알파벳 개수 출력
print("숫자 문자의 개수=%d"%d)  #숫자 개수 출력 
print("스페이스 문자의 개수=%d"%s)  #스페이스 개수 출력    