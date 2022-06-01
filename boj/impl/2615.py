# 오목

import sys

# sys.stdin = open("input.txt", "r")

pan = [list(map(int, input().split())) for _ in range(19)]

dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

for i in range(19):
  for j in range(19):
    dol = 0
    if pan[i][j] == 0:
      continue
    dol = pan[i][j]  # 돌 무슨색인지 기억
    
    for k in range(4):  # 방향별로 오목인지 확인
      nx = i + dx[k]
      ny = j + dy[k]

      cnt = 1
      while 0 <= nx < 19 and 0 <= ny < 19 and pan[nx][ny] == dol:
        cnt += 1
        if cnt == 5:
          # 육목인지 확인 (육목인 경우 break하면 경계에 걸린 경우 고려 안해도 됨)
          if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 and pan[i - dx[k]][j - dy[k]] == dol:
            break
          if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and pan[nx + dx[k]][ny + dy[k]] == dol:
            break

          # 오목인 경우
          print(dol)
          print((i+1), (j+1))
          sys.exit(0)
        nx += dx[k]
        ny += dy[k]

print(0)  # 승부가 안나는 경우