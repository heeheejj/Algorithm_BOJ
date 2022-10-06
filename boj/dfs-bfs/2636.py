# 치즈

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
H, W = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(H)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]
cntList = []

def bfs():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = True
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W or visited[nx][ny] == True:
                continue
            if _map[nx][ny] == 1:  # 가장자리(만) 녹이기 - 가장자리만 녹이기 위해서 큐에 넣지 않음
                _map[nx][ny] = 0
                visited[nx][ny] = True
                cnt += 1
            elif _map[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append([nx, ny])

    cntList.append(cnt)
    return cnt

time = 0
while True:
    time += 1
    visited = [[False] * W for _ in range(H)]
    cnt = bfs()    # 판의 가장자리에는 치즈가 없으므로 0,0에서 bfs 돌리면 문제에서 말하는 구멍으로는 접근할 일이 없다.
    if cnt == 0:
        break

print(time-1)
print(cntList[-2])
