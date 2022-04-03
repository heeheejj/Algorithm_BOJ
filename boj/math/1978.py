# 소수 찾기
# 9:56~9:58

def isPrimeNumber(x):
  if x == 1:
    return 0
  
  for i in range(2, x):  # x == 2이면 for문 안돌고 바로 return True
    if x % i == 0:
      return 0
  return 1

n = int(input())
inputs = list(map(int, input().split()))
count = 0

for i in inputs:
  if isPrimeNumber(i) == 1:
    count += 1
    
print(count)