from collections import deque

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
        

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)