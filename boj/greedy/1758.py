# 알바생 강호

import sys

input = sys.stdin.readline
N = int(input())
money = list()

for i in range(N):
  money.append((int(input()), i))

money.sort(reverse = True)

tip = 0
for i in range(N):
  temp = money[i][0] - i
  if temp > 0:
    tip += temp

print(tip)