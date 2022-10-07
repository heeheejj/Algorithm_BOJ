# 연구소 (다시풀음)
# 54분 걸렸당..
# 436ms
# 0 좌표를 리스트에 저장 -> zeroCnt(0의 개수)개 중 3개 고르는 조합!에 벽을 세우기
# 2 좌표를 리스트에 저장 -> 바이러스 bfs에 쓰일 것임
# 조합마다 바이러스를 bfs 돌린다.(1을 만나면 못가) 그 후 0의 개수 구하기 => 안전영역의 크기!! 지금까지 최댓값과 비교해서 갱신해줌

import sys
from itertools import combinations
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def virusBfs(arr, virusPos):
    global result
    # arr는
    virus = virusPos.copy()
    visited = [[False]*M for _ in range(N)]

    while virus:
        x, y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if arr[nx][ny] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                arr[nx][ny] = 2
                virus.append((nx, ny))

    # for i in range(N):
    #     print(arr[i])
    # print("================")

    # 0 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
    result = max(cnt, result)

def createWall(arr):
    combs = list(combinations(zeroPos, 3))
    for comb in combs:
        temp = [row[:] for row in arr]  # 초기화 잘 됨
        for x, y in comb:
            temp[x][y] = 1
        virusBfs(temp, virusPos)
        # if result == 32:
        #     for i in range(N):
        #         print(temp[i])
        #     return

N, M = map(int, input().split())

_map = list()
zeroPos = list()
virusPos = deque()
result = -1
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 0:
            zeroPos.append((i, j))
        elif line[j] == 2:
            virusPos.append((i, j))
    _map.append(line)

createWall(_map)
print(result)