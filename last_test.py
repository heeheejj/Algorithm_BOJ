import sys
from itertools import permutations

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
  for i in primes:
    for j in primes:
      if i == j:
        continue
      if i + j == x:
        # print("True: 조건1: x = ", x)
        return True
  return False

def isSatisfied2ndCondition(x, m):
  num = x
  while num % m == 0:
    num //= m
  for i in primes:
    for j in primes:
      if num == i * j:
        # print("True: 조건2: x = ", x)
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





# for i in range(10**(k-1), 10**k):
#   if isSumOfDifferentPrimeNumber(i):
#     result[i] = True
#     if isSatisfied2ndCondition(i, m) == False:
#       result[i] = False

# for i in range(10**k):
#   if result[i]:
#     print(i, end = ' ')
print(result.count(True))