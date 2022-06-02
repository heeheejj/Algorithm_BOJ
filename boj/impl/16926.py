# 배열 돌리기 1

import sys

def rotate(level):  # 파라미터는 시작 원소
  nx, ny = level, level
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]
  result = [row[:] for row in arr]  
  
  for i in range(4):
    while True:
      # nx += dx[i]
      # ny += dy[i] 
      if not ((0+level) <= nx + dx[i] < (n-level) and (0+level) <= ny + dy[i] < (m-level)):
        break
      nx += dx[i]
      ny += dy[i]
      print("nx", nx, "/ ny", ny)
      result[nx][ny] = arr[nx - dx[i]][ny - dy[i]]

  return result

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for l in range(min(n, m) // 2):
  # 시작 원소(좌측 상단)((0,0)부터 시작)
  print(rotate(l))