# 서로소 평균
# 서로소 = 최대공약수가 1인 두 자연수

import sys
import math

def isCoprime(x, y):
  if math.gcd(x, y) == 1:
    return True
  else:
    return False

n = int(input())
inputs = list(map(int, sys.stdin.readline().rstrip().split()))
x = int(input())

sum = 0
count = 0
for i in range(n):
  num = inputs[i]
  if isCoprime(x, num):
    sum += num
    count += 1

avg = sum / count
print(avg)