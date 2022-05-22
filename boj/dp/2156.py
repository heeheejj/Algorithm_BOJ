# 포도주 시식

import sys

input = sys.stdin.readline

n = int(input())
wine = [0] * 10001
for i in range(n):
  wine[i] = int(input())

d = [0] * 10001
d[0], d[1], d[2] = wine[0], wine[0] + wine[1], max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])

for i in range(3, n+1):
  d[i] = max(d[i -2] + wine[i], d[i - 3] + wine[i - 1] + wine[i], d[i - 1])

print(d[n])