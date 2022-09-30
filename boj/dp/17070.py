# 파이프 옮기기 1
# 3차원 DP
# i > j일 때 continue하는 조건을 추가했었는데 잘못된 생각이었다.
# 대각선-세로-세로 쭉- 대각선-가로 쭉 하는 경로를 생각하면 i > j인 경우도 가능하다.

import sys

HOR, DIAG, VER = 0, 1, 2
dx = [[0, -1], [0, -1, -1], [0, -1, -1]]
dy = [[-1, -1], [-1, -1, 0], [0, -1, 0]]

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

_map = [list(map(int, input().split())) for _ in range(N)]
if _map[N-1][N-1] == 1:
    print(0)
    exit()
dp = [[[0]*N for _ in range(N)] for _ in range(3)]    # (1,1)부터 시작
dp[0][0][1] = 1

for i in range(2, N-1):
    if _map[0][i] == 1:
        break
    dp[0][0][i] = 1

for i in range(1, N):
    for j in range(2, N):
        if _map[i][j] == 1: # 지금 확인할 위치가 벽이면 continue
            continue
        dp[HOR][i][j] += (dp[HOR][i][j - 1] + dp[DIAG][i][j - 1])
        dp[VER][i][j] += (dp[DIAG][i - 1][j] + dp[VER][i - 1][j])
        if _map[i-1][j] == 1 or _map[i][j-1] == 1 or _map[i-1][j-1] == 1:  # 대각선인 경우 오른쪽 위, 왼쪽 아래가 빈칸인지도 체크
            continue
        dp[DIAG][i][j] += (dp[HOR][i - 1][j - 1] + dp[DIAG][i - 1][j - 1] + dp[VER][i - 1][j - 1])

print(dp[0][N-1][N-1]+dp[1][N-1][N-1]+dp[2][N-1][N-1])