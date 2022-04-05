# 소수 최소 공배수
# isPrimeNumber의 for문 최적화 (제곱근까지로 변경)
# 백준에서 출력 초과가 뜸 -> 소수가 중복일 수 있다는 것 고려안해서 리스트를 set으로 감싸고 다시 list로 바꿔줘서 정답!

import math

def isPrimeNumber(x):
  if x == 1 or x == 0:
    return False
  
  for i in range(2, int(math.sqrt(x)) + 1):  # x == 2이면 for문 안돌고 바로 return True
    if x % i == 0:
      return False
  return True

n = int(input())
inputs = list(set(list(map(int, input().split()))))
result = 1
for i in inputs:
  if isPrimeNumber(i):
    result *= i

if result == 1:
  print(-1)
else:
  print(result)