grade=int(input("이수한 학점수를 입력하시오: "))  # 학점수 입력
score=float(input("평점을 입력하시오: "))  # 평점 입력
if (grade>=140 and score>=2.0):  # 학점수가 140학점 이상이고(and) 평점이 2.0이상일 때
  print("졸업 조건을 만족합니다!")  
else:  # 그렇지 않으면
  print("졸업이 힘듭니다!")