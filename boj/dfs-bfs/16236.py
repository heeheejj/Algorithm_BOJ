# 16236 - 아기 상어

import sys
from collections import deque
def bfs(N, map, sx, sy):  # 상어와 목표물고기까지 최단거리 반환하는 함수
    queue = deque()
    queue.append((sx, sy))

    # dx, dy 순서 중요한것같음??
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
    # 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    global result
    while queue:
        result += 1
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:  # 범위 벗어나면 pass
                continue

            temp = map[nx][ny]
            if temp != 0:    # 해당 위치에 물고기가 있을 때
                global sharkSize
                if temp > sharkSize:    # 물고기가 상어보다 크면 못지나간다. pass
                    continue
                elif temp == sharkSize: # 물고기크기가 상어크기와 같으면 지나간다.
                    queue.append((nx, ny))
                    continue
                else:   #물고기가 상어보다 작으면 먹는다. (최단거리의 물고기 먹음)
                    map[nx][ny] = 0
                    bfs(N, map, nx, ny)
                    return
            else:   # 해당 위치에 물고기가 없으면 지나간다.
                queue.append((nx, ny))
                continue
    return result

input = sys.stdin.readline

result = 0  # 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간
sharkSize = 2
