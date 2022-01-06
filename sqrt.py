from math import *  # sqrt를 사용하기 위해 import함

a=float(input("A= "))  # a 입력
b=float(input("B= "))  # b 입력
c=float(input("C= "))  # c 입력

d=b*b-4*a*c  # 제곱근 안 계산

if(a==0):  # a가 0-> 1차 방정식
  print("x=",-c/b)
else:
  if(d>0): # 2개의 실근이 존재
    print("x1=",(-b+sqrt(d))/(2*a))
    print("x2=",(-b-sqrt(d))/(2*a))
  elif(d==0): # 하나의 실근이 존재
    print("x=",-b/(2*a))
  else:  # 실근이 존재하지 않음(d<0 일 때)
    print("실근이 존재하지 않음")  