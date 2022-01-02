def swap(x,y): 
  temp=x  # 변수 temp에 x값 10을 저장
  x=y     # x에 y값 20을 저장
  y=temp  # y에 temp값 10을 저장
  return (x,y)
a=10
b=20
print(a,b)
swap(a,b)