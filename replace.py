n=" hong gil dong "
res1=n.replace(" ","")           # 왼쪽의 문자를 오른쪽의 문자꼴로 바꾸는 함수(replace)->replace(" ","")꼴로 모든 공백을 제거   
res2=n.strip()                   # 양 끝쪽 공백을 제거하는 함수
res3=n.lstrip()                  # 맨 왼쪽 공백을 제거하는 함수
res4=n.rstrip()                  # 맨 오른쪽 공백을 제거하는 함수

print("공백 o:",n)
print("공백 x:",res1)
print(f"/{res2}/")
print(f"/{res3}/")
print(f"/{res4}/")
