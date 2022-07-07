# 2+1 세일

import sys

input = sys.stdin.readline

N = int(input())
money = list()

for _ in range(N):
  money.append(int(input()))

money.sort(reverse = True)
sum = sum(money)
for i in range(N):
  if (i+1) % 3 == 0:
    sum -= money[i]
    
print(sum)