# 음료수 얼려 먹기
# dfs()함수가 파라미터로 행번호, 열번호를 가짐
# dfs()함수가 True를 반환하도록 하고 True가 되는 개수를 세기

def dfs(x, y):
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    return True
  return False
    
n, m = map(int,input().split())
# a = list(map(int,input()))
# print(a)


graph = []
for i in range(n):
    graph.append(list(map(int,input())))

result = 0

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)