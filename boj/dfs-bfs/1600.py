# 말이 되고픈 원숭이
# 이코테 미로 탈출 문제 참고

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y, k))
  
  while queue:
    x, y, z = queue.popleft()

    if x == h - 1 and y == w - 1:
      return graph[w-1][h-1]
  
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= h or ny < 0 or ny >= w:
        continue
      if graph[nx][ny] == 1:
        continue
      if graph[nx][ny] == 0:
        queue.append((nx, ny, z))
        graph[nx][ny] = graph[x][y] + 1 # graph는 원소가 0, 1뿐인 2차원 배열이지만 이렇게 1씩 더해주어 다시 저장해 1, 2, 3, ... 이런식으로 경로가 찍히도록 최단거리의 길이 찾기

    if z > 0:
      for i in range(8):
        nx = x + mx[i]
        ny = y + my[i]

        if nx < 0 or nx >= h or ny < 0 or ny >= w:
          continue
        if graph[nx][ny] == 1:
          continue
        if graph[nx][ny] == 0:
          queue.append((nx, ny, z - 1))
          graph[nx][ny] = graph[x][y] + 1 # graph는 원소가 0, 1뿐인 2차원 배열이지만 이렇게 1씩 더해주어 다시 저장해 1, 2, 3, ... 이런식으로 경로가 찍히도록 최단거리의 길이 찾기
  return graph[h-1][w-1]

k = int(input())
w, h = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(h)]
# for i in range(h):
#     graph.append(list(map(int,input().split())))

# dx - dy 순서대로 
# 상: (-1,0), 하: (1, 0), 좌: (0, -1), 우: (0, 1)
  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 말의 움직임
mx = [-1, 1, -1, 1, 2, -2, 2, -2]
my = [-2, -2, 2, 2, -1, -1, 1, 1]
#print(graph)

# bfs 호출!
# visited 배열 따로 만들 필요 없이, 1을 0으로 바꿔주면 될 것 같다.
result = bfs(0, 0)
# print(result)
if result == 0:
  print(-1)
else:
  print(result)