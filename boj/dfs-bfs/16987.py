# 계란으로 계란치기

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
result = -1 # 최대로 깰 수 있는 계란
def dfs(depth, cnt):
     if depth == N:
         global result
         result = max(result, cnt)
         return

     if info[depth][0] <= 0:
         dfs(depth+1, cnt)

# isBroken = [False]*N
# for i in range(N):
#     if isBroken[i]:
#         continue
#
#     for j in range(i+1, N):
#         iNGD, iWeight = info[i][0], info[i][1]
#         jNGD, jWeight = info[j][0], info[j][1]
#         diff1, diff2 = jNGD - iWeight, iNGD - jWeight
#         if diff1 <= 0 and diff2 <= 0:
    # isBroken[i] = True0