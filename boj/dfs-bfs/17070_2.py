# 파이프 옮기기 1
# 완탐 - 시간초과ㅜ, dp로 다시 풀기

import sys

HOR, DIAG, VER = 0, 1, 2    # 방향 status 정의: 순서대로 가로, 대각선, 세로
'''
status, idx 둘 다 0(HOR): 가로, 1(DIAG): 대각선, 2(VER): 세로
status  |  idx  | dx[status][idx] | dy[status][idx]
---------------------------------------
   0    |   0   |        0        |       1
        |   1   |        1        |       1
---------------------------------------
   1    |   0   |        0        |       1
        |   1   |        1        |       1
        |   2   |        1        |       0
---------------------------------------
   2    |   0   |        0        |       0
        |   1   |        1        |       1
        |   2   |        1        |       0
'''
dx = [[0, 1], [0, 1, 1], [0, 1, 1]]
dy = [[1, 1], [1, 1, 0], [0, 1, 0]]
result = 0
depth = 0
def dfs(status, x, y, depth):
    print("depth:",depth, " status:",status,"x:",x,"y:",y)
    if x == N and y == N:
        global result
        result += 1
        print("도착")
        return

    size = len(dx[status])
    print(size)
    for nextStatus in range(size):
        if (status == HOR and nextStatus == VER) or (status == VER and nextStatus == HOR):  # 45도가 넘어가는경우 pass
            print("45도 넘어",status,nextStatus)
            continue
        nx, ny = x + dx[status][nextStatus], y + dy[status][nextStatus]
        if x == nx and y == ny: # status가 2인 경우 idx 0이 0,0이라서... (1, 0)으로 하면 idx 0이 세로가돼서 규칙이 깨져버림
            continue
        if map[nx][ny] == 1:
            print("전진불가 - nx:", nx, " ny:", ny, " nextStatus:", nextStatus)
            continue

        # 대각선으로 갈 경우 (1, 1) 방향뿐만 아니라 (1, 0), (0, 1) 방향도 1이 아닌지 확인해줘야함
        if nextStatus == 1 and (map[x+1][y] == 1 or map[x][y+1] == 1):
            print("대각선방향인데 옆에 1이 있어서 nextStatus방향으로 이동 불가 - nextStatus:", nextStatus)
            continue
        print("전진 - nx:", nx, " ny:", ny, " nextStatus:", nextStatus)
        dfs(nextStatus, nx, ny, depth+1)

sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())

# map 배열을 만드는데, Ц 이렇게 윗테두리 뺀 모양으로(어차피 위로갈일 없음) 벽 테두리를 만들어줌
map = [[1 for _ in range(N+2)]]+[[1]+list(map(int, input().split()))+[1] for _ in range(N)]
map.append([1]*(N+2))
print(map)
dfs(HOR, 1, 2, 0)
print(result)