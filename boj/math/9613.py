# GCD 합

from itertools import combinations
import sys
import math

input = sys.stdin.readline
result = list()

t = int(input())

for i in range(t):
  sum = 0
  numbers = list(map(int, input().split()))
  del numbers[0] 
  combs = list(combinations(numbers, 2))
  for j in range(len(combs)):
    gcd = math.gcd(combs[j][0], combs[j][1])
    sum += gcd
      
  result.append(sum)

for i in range(t):
  print(result[i])