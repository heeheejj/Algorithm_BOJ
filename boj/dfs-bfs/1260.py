# DFS와 BFS

import sys
from collections import deque

def dfs(graph, start, visited):
  visited[start] = True
  print(start, end=' ')

  for i in graph[start]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  queue = deque()
  queue.append(start)
  # 위 두 줄 합쳐서 queue = deque([start]) 가능
  visited[start] = True

  while queue:
    curr = queue.popleft()
    print(curr, end=' ')
    
    for i in graph[curr]:
      if visited[i] == False:
        queue.append(i)
        visited[i] = True

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  e1, e2 = map(int, input().split())
  graph[e1].append(e2)
  graph[e2].append(e1)

for i in range(n + 1):  # 정렬을 안해주면 '방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문한다'는 조건에 맞지 않게됨!
  graph[i].sort()

visited = [False] * (n + 1)
dfs(graph, v, visited)

print()
visited = [False] * (n + 1)
bfs(graph, v, visited)
print()