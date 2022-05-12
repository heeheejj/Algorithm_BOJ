# 치킨 배달

import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())

_map = list()  # 지도
houses = list()
chickens = list()

for i in range(n):
  __map = list(map(int, input().split()))
  _map.append(__map)
  for j in range(n):
    x = _map[i][j]
    if x == 1:  # 집일 때
      houses.append((i, j))
    elif x == 2:
      chickens.append((i, j))
      
city_chicken_dist = 99999 * m
for comb in combinations(chickens, m):
  chicken_dist_sum = 0
  for hx, hy in houses:  # 각 집 당 치킨거리 구하기
    chicken_dist = 9999
    for cx, cy in comb:
      dist = abs(hx - cx) + abs(hy - cy)
      # print(dist)
      chicken_dist = min(chicken_dist, dist)
    chicken_dist_sum += chicken_dist
  city_chicken_dist = min(city_chicken_dist, chicken_dist_sum)

print(city_chicken_dist)