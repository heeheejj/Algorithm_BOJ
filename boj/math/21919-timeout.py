# 소수 최소 공배수
# 9: 39~9:48 -> 시간 초과
# 에라토스테네스의 체 사용

def isPrimeNumber(x):
  if x == 1:
    return 0
  
  for i in range(2, x):  # x == 2이면 for문 안돌고 바로 return True
    if x % i == 0:
      return 0
  return 1

n = int(input())
inputs = list(map(int, input().split()))
result = 1
for i in inputs:
  if isPrimeNumber(i) == 1:
    result *= i

if result == 1:
  print(-1)
else:
  print(result)