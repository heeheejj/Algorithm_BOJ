# 유기농 배추

import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  global _map
  _map[x][y] = 0
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= M or ny < 0 or ny >= N or _map[nx][ny] == 0:
        continue
      queue.append((nx, ny))
      _map[nx][ny] = 0

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  M, N, K = map(int, input().split())
  cabbageLoc = [list(map(int, input().split())) for _ in range(K)]
  
  _map = [[0]*N for _ in range(M)]
  for x in cabbageLoc:
    _map[x[0]][x[1]] = 1
  
  
  result = 0
  for i in range(M):
    for j in range(N):
      if _map[i][j] == 1:
        bfs(i, j)
        result += 1

  print(result)