# 배열 돌리기 1
# 큐 사용

import sys
from collections import deque

def rotate(level):
  nx, ny = level, level
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1] 

  queue = deque()
  global arr
  
  for i in range(4):
    while True:
      if not ((0+level) <= nx + dx[i] < (n-level) and (0+level) <= ny + dy[i] < (m-level)):
        break
      nx += dx[i]
      ny += dy[i]
      queue.append(arr[nx - dx[i]][ny - dy[i]])
  queue.rotate(r)

  nx, ny = level, level
  for i in range(4):
    while True:
      if not ((0+level) <= nx + dx[i] < (n-level) and (0+level) <= ny + dy[i] < (m-level)):
        break
      arr[nx][ny] = queue.popleft()
      nx += dx[i]
      ny += dy[i]

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for l in range(min(n, m) // 2):
  rotate(l)

for i in range(n):
  for j in range(m):
    print(arr[i][j], end=' ')
  print()