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
  
  for x, y in combinations(numbers, 2):
    # 이런 방식의 for문은 2차원 리스트에서 안쪽 리스트의 크기가 모두 같고, 그 크기가 작을 때 사용한다. for과 in 사이에 쓰는 변수의 개수는 안쪽 리스트의 크기이다.
    gcd = math.gcd(x, y)
    sum += gcd
      
  result.append(sum)

for i in range(t):
  print(result[i])