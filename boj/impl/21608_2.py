# 상어 초등학교

import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
classroom = [[0]*N for _ in range(N)]  # 자리표 2차원 리스트
likes = [0]*(N*N+1)  # 학생 번호에 따른 좋아하는 학생 리스트 (학생 번호를 인덱스로 하는 1차원 리스트) (만족도 구할때 써야함)

queue = deque()  # 비어있는 칸의 좌표를 튜플로 넣는 큐

# 비어있는 칸 초기화
for i in range(1, N+1):
  for j in range(1, N+1):
    queue.append((i, j, 0, 0))

# classroom [0] * (N*N + 1)
# 2차원리스트를 1차원 리스트로 만들기
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(N*N):
  k, s1, s2, s3, s4 = map(int, input().split())
  like = [s1, s2, s3, s4]
    
  likes[k] = like
  while queue:
    focus = queue.popleft()
    x, y = focus[0], focus[1]
    lCnt, bCnt = 0, 0  # 각 위치의 상하좌우에 있는 좋아하는 학생수, 빈칸수
    for j in range(4):
      if not (0 <= x + dx[j] < N and 0 <= y + dy[j] < N):
        continue
      if classroom[x + dx[j]][y + dy[j]] == 0:
        bCnt += 0
        continue
      if likes.contains(classroom[x + dx[j]][y + dy[j]]):
        lCnt += 1
    focus[2], focus[3] = lCnt, bCnt
    queue.append(focus)