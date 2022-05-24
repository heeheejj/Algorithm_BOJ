# 평범한 배낭
# 냅색(Knapsack) 알고리즘

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
inputs = [[0, 0]]
d = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    inputs.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = inputs[i][0]
        v = inputs[i][1]
        if w > j:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j-w] + v, d[i-1][j])

print(d[n][k])