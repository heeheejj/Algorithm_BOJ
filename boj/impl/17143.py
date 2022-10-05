# 낚시왕
import sys

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

def moveSharks():
    global _map
    temp_map = [[-1]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            now = _map[i][j]
            if now != -1:
                s, d, z = sharks[now][0], sharks[now][1], sharks[now][2]
                _map[i][j] = -1
                nx, ny = i, j
                for k in range(1, s+1):
                    if d == 1:
                        nx += dx[d]
                        if nx < 0:
                            d = 2
                            sharks[now][1] = 2
                            nx += 2*dx[d]
                        elif nx == 0:
                            d = 2
                            sharks[now][1] = 2
                    elif d == 2:
                        nx += dx[d]
                        if nx >= R:
                            d = 1
                            sharks[now][1] = 1
                            nx += 2*dx[d]
                        elif nx == R-1:
                            d = 1
                            sharks[now][1] = 1
                    elif d == 3:
                        ny += dy[d]
                        if ny >= C:
                            d = 4
                            sharks[now][1] = 4
                            ny += 2*dy[d]
                        elif ny == C-1:
                            d = 4
                            sharks[now][1] = 4
                    elif d == 4:
                        ny += dy[d]
                        if ny < 0:
                            d = 3
                            sharks[now][1] = 3
                            ny += 2*dy[d]
                        elif ny == 0:
                            d = 3
                            sharks[now][1] = 3
                prev = temp_map[nx][ny]
                if prev != -1:
                    if sharks[prev][2] < sharks[now][2]:
                        temp_map[nx][ny] = now
                        isEaten[prev] = True
                    else:
                        isEaten[now] = True
                else:
                    temp_map[nx][ny] = now
    _map = temp_map

def moveFisher():
    global result
    fX, fY = 0, 0
    while fY < C:
        fX = 0
        while fX < R:
            value = _map[fX][fY]
            if value != -1:
                _map[fX][fY] = -1
                isEaten[value] = True
                result += sharks[value][2]
                break
            fX += 1
        moveSharks()
        fY += 1

input = sys.stdin.readline

R, C, M = map(int, input().split())
sharks = list()
_map = [[-1]*C for _ in range(R)]
isEaten = [False]*M
result = 0
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    if d == 1 or d == 2:
        s = s % (2*(R-1))
    else:
        s = s % (2*(C-1))
    sharks.append([s, d, z])
    _map[r-1][c-1] = i
moveFisher()
print(result)