# 오목

import sys

def printResult(k, i, j):
  print(k)
  print((i+1), (j+1))

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
        if j == 0:
          printResult(k, i, j)
          break
        if pan[i][j-1] != k:
          printResult(k, i, j)
          break
    elif j+5 == 19:
      if pan[i][j-1] != k and pan[i][j+1] == k and pan[i][j+2] == k and pan[i][j+3] == k and pan[i][j+4] == k:
        printResult(k, i, j)
        break

    # 아래방향
    if i+5 < 19:
      if pan[i+1][j] == k and pan[i+2][j] == k and pan[i+3][j] == k and pan[i+4][j] == k and pan[i+5][j] != k:
        if i == 0:
          printResult(k, i, j)
          break
        if pan[i-1][j] != k:
          printResult(k, i, j)
          break
    elif i+5 == 19:
      if pan[i-1][j] != k and pan[i+1][j] == k and pan[i+2][j] == k and pan[i+3][j] == k and pan[i+4][j] == k:
        printResult(k, i, j)
        break

    # 우하향 대각선
    if j+5 < 19 and i+5 < 19:
      if pan[i+1][j+1] == k and pan[i+2][j+2] == k and pan[i+3][j+3] == k and pan[i+4][j+4] == k and pan[i+5][j+5] != k:
        if j == 0 or i == 0:
          printResult(k, i, j)
          break
        if pan[i-1][j-1] != k:
          printResult(k, i, j)
          break
        
    elif j+5==19 and i+5 < 19:
      if pan[i+1][j+1] == k and pan[i+2][j+2] == k and pan[i+3][j+3] == k and pan[i+4][j+4] == k:
        if i == 0:
          printResult(k, i, j)
          break
        if pan[i-1][j-1] != k:
          printResult(k, i, j)
          break
    elif i+5==19 and j+5 < 19:
      if pan[i+1][j+1] == k and pan[i+2][j+2] == k and pan[i+3][j+3] == k and pan[i+4][j+4] == k:
        if j == 0:
          printResult(k, i, j)
          break
        if pan[i-1][j-1] != k:
          printResult(k, i, j)
          break

    # 우상향 대각선(기준: 맨 오른쪽 위 돌이 i, j)
    if 4 <= i < 19:
      if j+5 < 19:
        if pan[i+1][j-1] == k and pan[i+2][j-2] == k and pan[i+3][j-3] == k and pan[i+4][j-4] == k and pan[i+5][j-5] != k:
          printResult(k, i, j)
          break
      elif j+5 == 19:
        if pan[i+1][j-1] == k and pan[i+2][j-2] == k and pan[i+3][j-3] == k and pan[i+4][j-4] == k:
          if i+5 == 19:
            printResult(k, i, j)
            break
          if pan[i+5][j-5] != k:
            printResult(k, i, j)
            break


      # 우상향 대각선 조건 처리하다가 포기.......... 새로운 방법을 찾자!~!~