# 오목

import sys

sys.stdin = open("input.txt", "r")

pan = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
  for j in range(19):

    if pan[i][j] == 1:  # 검은색
      k = 1
    elif pan[i][j] == 2:  # 흰색
      k = 2
    else:
      continue

    # 오른쪽 방향
    if j+5 < 19:
      if pan[i][j+1] == k and pan[i][j+2] == k and pan[i][j+3] == k and pan[i][j+4] == k and pan[i][j+5] != k:
        print(k)
        print((i+1), (j+1))
        break
    elif j+5 == 19:
      if pan[i][j+1] == k and pan[i][j+2] == k and pan[i][j+3] == k and pan[i][j+4] == k:
        print(k)
        print((i+1), (j+1))
        break

    # 아래방향
    if i+5 < 19:
      if pan[i+1][j] == k and pan[i+2][j] == k and pan[i+3][j] == k and pan[i+4][j] == k and pan[i+5][j] != k:
        print(k)
        print((i+1), (j+1))
        break
    elif i+5 == 19:
      if pan[i+1][j] == k and pan[i+2][j] == k and pan[i+3][j] == k and pan[i+4][j] == k:
        print(k)
        print((i+1), (j+1))
        break

    # 우하향 대각선
    if j+5 < 19 and i+5 < 19:
      if pan[i+1][j+1] == k and pan[i+2][j+2] == k and pan[i+3][j+3] == k and pan[i+4][j+4] == k and pan[i+5][j+5] != k:
        print(k)
        print((i+1), (j+1))
        break
    elif (j+5==19 and i+5 < 19) or (i+5==19 or j+5 < 19):
      if pan[i+1][j+1] == k and pan[i+2][j+2] == k and pan[i+3][j+3] == k and pan[i+4][j+4] == k:
        print(k)
        print((i+1), (j+1))
        break

    # 우상향 대각선(기준: 맨 오르쪽 위 돌이 i, j)
    if 4 <= i < 19:
      if j+5 < 19:
        if pan[i+1][j-1] == k and pan[i+2][j-2] == k and pan[i+3][j-3] == k and pan[i+4][j-4] == k and pan[i+5][j-5] != k:
          print(k)
          print((i+1), (j+1))
          break
      elif j+5 == 19:
        if pan[i+1][j-1] == k and pan[i+2][j-2] == k and pan[i+3][j-3] == k and pan[i+4][j-4] == k:
          print(k)
          print((i+1), (j+1))
          break