def d(n):
    return n + sum(map(int, str(n)))

# 셀프 넘버란 어떤 수가 그 수 자신의 각 자리수를 더한 값과 같지 않은 수를 말합니다. 예를 들어 1, 3, 5, 7, 9, 20, 31은 셀프 넘버입니다.
numbers = set(range(1, 10001)) # 1부터 10000까지의 수 중 셀프 넘버를 찾아라
self_numbers = numbers - {d(n) for n in numbers}
for self_number in sorted(self_numbers):
    print(self_number)
# d(n) 함수를 정의하여 어떤 수 n의 각 자리의 숫자들과 자기 자신을 더한 값을 계산. 
# 이후 1부터 10000까지의 숫자 집합을 만들고, 이 중에서 d(n) 함수를 이용해 얻은 결과를 제외한 셀프 넘버만을 구한 뒤, 오름차순으로 정렬하여 출력
