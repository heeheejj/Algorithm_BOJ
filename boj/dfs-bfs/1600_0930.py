# 말이 되고픈 원숭이
# 이코테 미로 탈출 문제 참고

from collections import deque
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((0, 0, K))

    while queue:
        x, y, z = queue.popleft()

        if x == H - 1 and y == W - 1:
            return visited[H-1][W-1][z]

        # 상하좌우 움직임
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue

            if graph[nx][ny] != 1 and visited[nx][ny][z] == 0: # nx, ny위치에 벽이 없고, 방문한 적 없을 때
                visited[nx][ny][z] = visited[x][y][z]+1
                queue.append((nx, ny, z))

        # 말의 움직임
        if z > 0:
            for i in range(8):
                nx = x + mx[i]
                ny = y + my[i]
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                if graph[nx][ny] != 1 and visited[nx][ny][z-1] == 0:
                    queue.append((nx, ny, z-1))
                    visited[nx][ny][z-1] = visited[x][y][z]+1

    return -1


K = int(input())
W, H = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
# for i in range(h):
#     graph.append(list(map(int,input().split())))

# dx - dy 순서대로 
# 상: (-1,0), 하: (1, 0), 좌: (0, -1), 우: (0, 1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 말의 움직임
mx = [-1, 1, -1, 1, 2, -2, 2, -2]
my = [-2, -2, 2, 2, -1, -1, 1, 1]
# print(graph)

# bfs 호출!
print(bfs())