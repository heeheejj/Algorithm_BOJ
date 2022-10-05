# 낚시왕
# 주석 추가 ver

import sys

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

def moveSharks():   # (idx 1부터 시작) 상, 하, 우, 좌 순서
    global _map
    temp_map = [[-1]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            now = _map[i][j]
            if now != -1:
                s, d, z = sharks[now][0], sharks[now][1], sharks[now][2]   # 속력, 이동방향, 크기
                _map[i][j] = -1
                nx, ny = i, j
                # print(f"now: {now} / init d: {d}")
                for k in range(1, s+1):
                    if d == 1:  # nx == 1   # nx == 2, 5번째
                        nx += dx[d] # nx == 0   # nx == 1, 6번쨰
                        if nx < 0:
                            d = 2
                            sharks[now][1] = 2  # 이거 안해줘서 틀렸었다. 방향 바뀔때마다 sharks리스트의 방향도 바꿔줘야함
                            nx += 2*dx[d]
                            # print(f"now: {now} / 방향꺾기 위-> 아래 nx: {nx}")
                        elif nx == 0:
                            d = 2   # nx == 0, 아래
                            sharks[now][1] = 2
                        #     print(f"now: {now} / 가장자리인데 방향이 위로되어있을 때 x: {nx}")
                    elif d == 2:    # nx == 3
                        nx += dx[d] # nx == 4   # nx == 1, 2, 3, 4
                        if nx >= R: # nx >= 4
                            d = 1
                            sharks[now][1] = 1
                            nx += 2*dx[d]   # nx == 2
                            # print(f"now: {now} / 방향꺾기 아래-> 위 nx: {nx}")
                        elif nx == R-1:   # nx == 3
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
                        # print(f"now: {now} / ny: {ny}, d: {d}")
                    elif d == 4:
                        ny += dy[d]
                        if ny < 0:
                            d = 3
                            sharks[now][1] = 3
                            ny += 2*dy[d]
                        elif ny == 0:
                            d = 3
                            sharks[now][1] = 3
                        # print(f"now: {now} / ny: {ny}")
                prev = temp_map[nx][ny]
                if prev != -1:      # 이제껏 이동완료한 상어 중에 현재 이동완료한 상어와 위치가 겹치는게 있을 때
                    if sharks[prev][2] < sharks[now][2]:    # 참고: 두 상어는 같은 크기를 갖는 경우가 없다.
                        temp_map[nx][ny] = now
                        isEaten[prev] = True
                        # print(f"{prev} is eaten by {now}: {sharks[prev]}")
                    else:
                        # temp_map[nx][ny]는 prev로 유지
                        isEaten[now] = True
                        # print(f"{now} is eaten by {prev}")
                else:
                    temp_map[nx][ny] = now

                # print(f"now: {now} / ({i}, {j}) -> ({nx}, {ny}, {d})")
    # 모든 상어 이동 완료!
    _map = temp_map
    # for i in range(R):
    #     print(_map[i])
    # print("========================")

def moveFisher():
    global result
    fX, fY = 0, 0
    while fY < C:
        # 상어 잡기
        fX = 0  # 낚시왕이 오른쪽으로 이동할때마다 fX를 0으로 초기화
        while fX < R:
            value = _map[fX][fY]
            if value != -1:
                _map[fX][fY] = -1   # _map에서 상어의 위치 삭제
                isEaten[value] = True
                result += sharks[value][2]
                break
            fX += 1
        moveSharks()    # 상어 이동하기 -- 얘를 처음에 상어가 낚였을 때 같이 호출해줬는데, 반복문 빠져나와서 해주는게 시간복잡도가 적을 듯 하다.
        fY += 1
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

R, C, M = map(int, input().split())
sharks = list() # 인덱스에 따라 상어를 구분하므로 잡아먹혀도 지우면 안된다.
_map = [[-1]*C for _ in range(R)]   # _map에서 0번째~ (M-1)번째 idx 상어가 위치한 곳에 해당 idx를 표시
isEaten = [False]*M # 상어가 잡아먹혔을 때 True로 바꿔준다.
result = 0
for i in range(M):
    r, c, s, d, z = map(int, input().split())

    # s(속력)는 예를 들어 상, 하 이동일 때 s == 1인경우와 s == 1 + 2*(R-1)인 경우가 같다!!
    # 이 코드를 안넣으면 시간초과난다.
    if d == 1 or d == 2:    # 상, 하 이동 -> R
        s = s % (2*(R-1))
    else:                   # 좌, 우 이동 -> C
        s = s % (2*(C-1))
    sharks.append([s, d, z])    # 속력, 이동 방향, 크기
    _map[r-1][c-1] = i  # 편의상 1행, 1열을 1, 1이 아닌 0, 0으로 한다.
moveFisher()
print(result)