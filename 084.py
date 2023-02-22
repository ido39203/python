t1='A' # 알파벳
t2='안녕' # 한글
t3='War Craft' # 공백이 포함된 알파벳, 공백은 문자가 아니다!
t4='3PO' # 숫자와 알파벳, 숫자 역시 문자가 아니다.
t5='369' # 숫자
r1=t1.isalpha() # isalpha: 문자열이 알파벳, 한글 같은 언어문자인지 체크하는 메소드
r2=t2.isalpha()
r3=t3.isalpha()
r4=t4.isalpha()
r5=t5.isdigit() # isdigit: 문자열이 숫자인지 체크하는 메소드
print(r1)  # False 혹은 True로 출력한다.
print(r2)
print(r3)
print(r4)
print(r5)