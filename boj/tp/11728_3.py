# 배열 합치기
# 그냥 배열 합쳐서 sort - 1248ms

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

# ??? 그냥 정렬해보자
a = list(map(int, input().split()))

b = list(map(int, input().split()))

c = a + b
c.sort()

for x in c:
  print(x, end=' ')