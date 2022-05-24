# 1, 2, 3 더하기

import sys

input = sys.stdin.readline
d = [0] * 11
d[1], d[2], d[3] = 1, 2, 4
t = int(input())
for _ in range(t):
  n = int(input())
  for i in range(4, n+1):
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]
  print(d[n])