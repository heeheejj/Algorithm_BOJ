# 블랙잭

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

sums = list()
for x, y, z in combinations(nums, 3):
  sums.append(x + y + z)
sums.sort()

result = 0
for sum in sums:
  if sum > m:
    break
  result = sum

print(result)