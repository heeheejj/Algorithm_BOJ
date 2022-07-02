# 알바생 강호

import sys

input = sys.stdin.readline
N = int(input())
money = list()

for i in range(N):
  money.append(int(input()))

money.sort(reverse = True)

tip = 0
for i in range(N):
  temp = money[i] - i
  if temp > 0:
    tip += temp

print(tip)