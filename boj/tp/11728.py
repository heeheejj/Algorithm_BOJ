# 배열 합치기
# 투 포인터

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

a = list(input().split())
b = list(input().split())

ap, bp = 0, 0

while ap != n or bp != m:
  if ap == n:
    b_temp = b[bp:]
    print(" ".join(b_temp))
    break
  elif bp == m:
    a_temp = a[ap:]
    print(" ".join(a_temp))
    break
  elif int(a[ap]) < int(b[bp]):
    print(a[ap], end=' ')
    ap += 1
  elif int(a[ap]) >= int(b[bp]):
    print(b[bp], end=' ')
    bp += 1