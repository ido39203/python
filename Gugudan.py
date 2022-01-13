#// 2단부터 9단까지 for문을 활용하여 구구단을 출력 #//

for a in range(2,10): #2단부터 9단까지
  print("%d단"%a)  #단수 출력
  for b in range(1,10):  #1부터 9까지 변함
    print("%d*%d=%d"%(a,b,a*b))  #결과 출력