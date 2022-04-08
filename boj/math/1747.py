# 소수&팰린드롬

import math
import sys

def isPrimeNumber(x):
  if x == 1 or x == 0:
    return False
  
  for i in range(2, int(math.sqrt(x)) + 1):  # x == 2이면 for문 안돌고 바로 return True
    if x % i == 0:
      return False
  return True

def isPalindrome(x):
  if x == x[::-1]:
    return True

input = sys.stdin.readline

n = int(input())

while 1:
  if isPrimeNumber(n) and isPalindrome(str(n)):
    print(n)
    break
  n += 1