# 배열 합치기
# 투 포인터 - 1324ms

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ap, bp = 0, 0
result = list()
while ap != n or bp != m:
  if ap == n:
    result.append(b[bp])
    bp += 1
  elif bp == m:
    result.append(a[ap])
    ap += 1
  elif a[ap] < b[bp]:
    result.append(a[ap])
    ap += 1
  elif a[ap] >= b[bp]:
    result.append(b[bp])
    bp += 1

print(*result)  # list 앞에 * 붙이면 unpacking