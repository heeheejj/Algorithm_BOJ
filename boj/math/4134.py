# 다음 소수

import sys
import math

def isPrimeNumber(x):
  if x == 1 or x == 0:
    return False
  
  for i in range(2, int(math.sqrt(x)) + 1):  # x == 2이면 for문 안돌고 바로 return True
    if x % i == 0:
      return False
  return True

tc_count = int(input())
result = list()

for i in range(tc_count):
  j = int(sys.stdin.readline().rstrip())
  
  while 1:
    if isPrimeNumber(j):
      result.append(j)
      break
    else:
      j += 1
    

for i in range(len(result)):
  print(result[i])