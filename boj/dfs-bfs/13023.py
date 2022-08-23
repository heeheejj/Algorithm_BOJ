# ABCDE

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False]*N

def dfs(idx, cnt):
    if cnt == 4:
        print(1)
        exit()

    for i in graph[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt+1)
            visited[i] = False

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
