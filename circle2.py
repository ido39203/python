def circle(r):  #원의 넓이와 둘레를 계산하여 반환하는 함수
  PI=3.1415
  area=r*r*PI  #원의 넓이 계산
  length=2*PI*r  #원의 둘레 계산
  return(area,length)  #넓이, 둘레 반환

r=float(input("반지름: "))  #반지름 입력
(area,length)=circle(r)  # circle 함수 호출
print("원의 넓이는 %f이고 원의 둘레는 %f이다."%(area,length))  