# 조건1: 소수인 두 수 가져올 때 조합으로 가져오도록 수정하기
# 조건2: 소수인 두 수 가져올 때 중복조합으로 가져오도록 수정하기

import sys
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

def getPrimeNumbers(x):
  numbers = list(range(10**(k-1), 10**k))
  start, end = numbers[0], numbers[-1]+1
  # print("x = ", x, ", start = ", start, ", end = ", end)
  if start < 2:
    start = 2
  _primes = list()
  sieve = [True] * end
  
  for i in range(2, end):
    if sieve[i] != False:
      _primes.append(i)
    for j in range(i * 2, end, i):
        sieve[j] = False
  return _primes

def isSumOfDifferentPrimeNumber(x):
  for i, j in combinations(primes, 2):
    print("comb: i = ", i, ", j = ", j)
    if i + j == x:
      print("True: 조건1: x = ", x, ", i = ", i, ", j = ", j)
      return True
  print("False: 조건1: x = ", x, ", i = ", i, ", j = ", j)
  return False

def isSatisfied2ndCondition(x, m):
  num = x
  while num % m == 0:
    num //= m
  for i, j in combinations_with_replacement(primes, 2):
    print("cwr: i = ", i, ", j = ", j)
    if num == i * j:
      # print("True: 조건2: x = ", x)
      return True
  return False
  

input = sys.stdin.readline

k, m = map(int, input().split())

result = [False for x in range(10**k)]

primes = getPrimeNumbers(k)
# comb_primes = combinations(primes, 2)  # 소수 조합
# cwr_primes = combinations_with_replacement(primes, 2)  # 소수 중복조합

for number in permutations(['0', '1', '2', '3', '4', '5', '6', '7','8', '9'], k):
  if(number[0] == '0'): continue
  number = int(''.join(number))
  print("number =", number)
  if isSumOfDifferentPrimeNumber(number):
    result[number] = True
    if isSatisfied2ndCondition(number, m) == False:
      result[number] = False





# for i in range(10**(k-1), 10**k):
#   if isSumOfDifferentPrimeNumber(i):
#     result[i] = True
#     if isSatisfied2ndCondition(i, m) == False:
#       result[i] = False

for i in range(10**k):
  if result[i]:
    print(i, end = ' ')
print("")
print(result.count(True))