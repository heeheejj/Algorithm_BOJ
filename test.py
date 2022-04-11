# 조건1: 소수인 두 수 가져올 때 조합으로 가져오도록 수정하기
# 조건2: 소수인 두 수 가져올 때 중복조합으로 가져오도록 수정하기
import time
start = time.time()
import sys
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
import math

def getPrimeNumbers(x):
  numbers = list(range(10**(k-1), 10**k))
  start, end = numbers[0], numbers[-1]+1
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
  for i, j in comb_primes:
    if i + j == x:
      return True
  return False

def isSatisfied2ndCondition(x, m):
  num = x
  while num % m == 0:
    num //= m
  for i in range(0, int(math.sqrt(num)) + 1):
    if num == cwr_primes[i][0] * cwr_primes[i][1]:
      return True
  return False
  
input = sys.stdin.readline

k, m = map(int, input().split())

result = [False for x in range(10**k)]

primes = getPrimeNumbers(k)
comb_primes = list(combinations(primes, 2))
cwr_primes = list(combinations_with_replacement(primes, 2))

for number in permutations(['0', '1', '2', '3', '4', '5', '6', '7','8', '9'], k):
  if(number[0] == '0'): continue
  number = int(''.join(number))
  if isSumOfDifferentPrimeNumber(number):
    result[number] = True
    if isSatisfied2ndCondition(number, m) == False:
      result[number] = False

print(result.count(True))

print("time :", time.time() - start)