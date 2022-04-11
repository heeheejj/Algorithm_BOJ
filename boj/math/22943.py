# 수

import sys
import time

def getPrimeNumbers(k):  # k로 정의되는 범위 내의 모든 소수를 리스트로 반환
  numbers = list(num_range)
  start, end = numbers[0], numbers[-1]+1
  if start == 1:
    start = 2
  primes = list()  # 소수를 따로 저장할 리스트
  sieve = [True] * end
  
  for i in range(start, end):
    if sieve[i] != False:
      primes.append(i)
    for j in range(i * 2, end, i):
        sieve[j] = False
  return primes

input = sys.stdin.readline

k, m = map(int, input().split())

num_range = range(10**(k-1), 10**k)

result = [False for x in range(10**k)]

primes = getPrimeNumbers(k)
# print("primes = ", primes)

def isSumOfDifferentPrimeNumber(x):  # 서로 다른 두 개의 소수의 합인지
  # 이중 for문, x까지 모든 소수
  numbers1 = primes
  for i in numbers1:
    for j in numbers1:
      if i == j:
    
        continue
      if i + j == x:
        # print("True: x = ", x, ", i = ", i, ", j = ", j)
        return True
  # print("False: x = ", x, ", i = ", i, ", j = ", j)
  return False

def isSatisfied2ndCondition(x, m):
  num = x % m
  primes = getPrimeNumbers(x)
  for i in primes:
    for j in primes:
      if num == i * j:
        return True
  return False
# print("result = ", result)

for i in num_range:
  if isSumOfDifferentPrimeNumber(i):
    result[i] = True
    if isSatisfied2ndCondition(i, m) == False:
      result[i] = False
  
# print("조건2 끝 result: ", result)
print(result.count(True))