# 테트로미노

import sys

def dfs(i, j, cnt, sum):
  global result

  # 현재 dfs에서 남은 블록이 모두 최댓값(max_sum)과 같더라도 현재 result보다 작다면 바로 return
  if result >= sum + max_sum * (4 - cnt):
    return
  
  if cnt == 4:
    result = max(result, sum)
    return
  else:
    for k in range(4):  # 동서남북 방향으로 이동해서 dfs 다시 호출
      ny = i + dy[k]
      nx = j + dx[k]

      if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False:  # 종이 안에 있고 방문한 적이 없는 위치인지 확인
        if cnt == 2:  # 'ㅗ' 모양 고려: 2번째 블록차례라면 2번째 블록에서 다시 dfs 호출
          visited[ny][nx] = True  # dfs 새로 호출해야하니까 방문도장 임시로 찍어주고 dfs 끝나면 풀어줌
          dfs(i, j, cnt + 1, sum + paper[ny][nx])
          visited[ny][nx] = False
        visited[ny][nx] = True
        dfs(ny, nx, cnt + 1, sum + paper[ny][nx])
        visited[ny][nx] = False
        
input = sys.stdin.readline
n, m = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(n)]
visited = [([False] * m) for _ in range(n)]

# 동서남북 방향으로 이동하기 위해 dx, dy 리스트 각각 만들기
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

result = 0

max_sum = max(map(max, paper))  # array가 2차원 리스트일 때 map(max, array)하면 각 행의 최대값들을 추출할 수 있음, 각 행의 최대값들 중 최대값을 구하면 2차원 리스트 전체의 최댓값~!

for row in range(n):
  for col in range(m):
    visited[row][col] = True
    dfs(row, col, 1, paper[row][col])
    visited[row][col] = False  # 방문도장 초기화(?)

print(result)