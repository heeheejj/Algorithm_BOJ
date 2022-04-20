# 조건1: 소수인 두 수 가져올 때 조합으로 가져오도록 수정하기
# 조건2: 소수인 두 수 가져올 때 중복조합으로 가져오도록 수정하기

import sys
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

def getPrimeNumbers(x):  # 부울 리스트 반환하도록 변경했는데..음
  numbers = list(range(10**(k-1), 10**k))
  start, end = numbers[0], numbers[-1]+1
  if start < 2:
    start = 2
  # _primes = list()
  sieve = [True] * end
  
  for i in range(2, end):
    # if sieve[i] != False:
    #   _primes.append(i)
    for j in range(i * 2, end, i):
        sieve[j] = False
  return sieve

# def getPrimeNumbers(x):
#   numbers = list(range(10**(k-1), 10**k))
#   start, end = numbers[0], numbers[-1]+1
#   if start < 2:
#     start = 2
#   _primes = list()
#   sieve = [True] * end
  
#   for i in range(2, end):
#     if sieve[i] != False:
#       _primes.append(i)
#     for j in range(i * 2, end, i):
#         sieve[j] = False
#   return _primes

def isSumOfDifferentPrimeNumber(x):
  for i, j in combinations(primes, 2):
    if i + j == x:
      return True
  return False

def isSatisfied2ndCondition(x, m):
  num = x
  while num % m == 0:
    num //= m
  for i, j in combinations_with_replacement(primes, 2):
    if num == i * j:
      return True
  return False
  
input = sys.stdin.readline

k, m = map(int, input().split())

result = [False for x in range(10**k)]

primes = getPrimeNumbers(k)

for number in permutations(['0', '1', '2', '3', '4', '5', '6', '7','8', '9'], k):
  if(number[0] == '0'): continue
  number = int(''.join(number))
  if isSumOfDifferentPrimeNumber(number):
    result[number] = True
    if isSatisfied2ndCondition(number, m) == False:
      result[number] = False

print(result.count(True))