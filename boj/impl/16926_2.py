# 배열 돌리기 1
# 시간 초과

import sys

def rotate(level):
  nx, ny = level, level
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]
  result = [row[:] for row in arr]  
  
  for i in range(4):
    while True:
      if not ((0+level) <= nx + dx[i] < (n-level) and (0+level) <= ny + dy[i] < (m-level)):
        break
      nx += dx[i]
      ny += dy[i]
      result[nx][ny] = arr[nx - dx[i]][ny - dy[i]]
  return result

input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for r in range(r):
  for l in range(min(n, m) // 2):
    arr = rotate(l)

for i in range(n):
  for j in range(m):
    print(arr[i][j], end=' ')
  print()