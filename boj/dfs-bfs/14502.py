# 연구소

import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

def createWall(locations):  #조합의 결과 (3개의 튜플 리스트)
  for x, y in locations:
    global temp_map
    temp_map[x][y] = '1'

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      
      if temp_map[nx][ny] == '0':
        temp_map[nx][ny] = '2'
        queue.append((nx, ny))        
      elif temp_map[nx][ny] == '1': #벽인경우 무시
        continue

input = sys.stdin.readline
n, m = map(int, input().split())
# _map = [list(map(int, input().split())) for _ in range(n)]
_map = list()
zeros = list()
viruses = list()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  _map.append(list(input().split()))
  for j in range(m):
    x = _map[i][j]
    if x == '0':
      zeros.append((i, j))
    elif x == '2':
      viruses.append((i, j))

result = 0
# 벽 세울 위치 3군데 고르기 (조합 이용)
for locations in combinations(zeros, 3):
  temp_map = list()
  temp_map = deepcopy(_map) # 리스트 복제해서 temp_map 초기화
  # print(locations)
  createWall(locations)
  # print(temp_map)
  for x, y in viruses:
    bfs(x, y)  # 기존 바이러스가 있는 위치를 기준으로 bfs
  # print("느아",temp_map)
  _temp_map = sum(temp_map,[])
  result = max(result, _temp_map.count('0'))

print(result)