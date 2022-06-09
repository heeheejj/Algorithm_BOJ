# 상어 초등학교

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
classroom = [[0]*N for _ in range(N)]  # 자리표 2차원 리스트
likes = dict()  # 학생 번호에 따른 좋아하는 학생 딕셔너리

# classroom [0] * (N*N + 1)
# 2차원리스트를 1차원 리스트로 만들기
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(N*N):
  key, s1, s2, s3, s4 = map(int, input().split())
  likes[key] = [s1, s2, s3, s4]

  mx, my = 0, 0 # 위치 업데이트
  max_like, max_blank = -1, -1
  for i in range(N):
    for j in range(N):
      if classroom[i][j] == 0:
        lCnt, bCnt = 0, 0
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]
          if 0 <= nx < N and 0 <= ny < N:
            
            try:
              if classroom[nx][ny] in likes[key]:
                lCnt += 1
                continue
            except:
              pass
            if classroom[nx][ny] == 0:
              bCnt += 1
              continue
        if max_like < lCnt or (max_like == lCnt and max_blank < bCnt):
          max_like = lCnt
          max_blank = bCnt
          mx, my = i, j
  classroom[mx][my] = key

# 학생의 만족도의 총 합 구하기
result = 0
for i in range(N):
  for j in range(N):
    cnt = 0
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      if 0 <= nx < N and 0 <= ny < N:
        key = classroom[i][j]
        if classroom[nx][ny] in likes[key]:
          cnt += 1

    if cnt == 0:
      result += 0
    elif cnt == 1:
      result += 1
    elif cnt == 2:
      result += 10
    elif cnt == 3:
      result += 100
    elif cnt == 4:
      result += 1000

print(result)