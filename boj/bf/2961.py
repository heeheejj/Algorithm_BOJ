# 도영이가 만든 맛있는 음식

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

ingredients = list()

for _ in range(n):
  x, y = map(int, input().split())
  ingredients.append((x, y))

result = 1000000000
for i in range(1, n+1):
  for johap in combinations(ingredients, i):  # 재료 구성을 정함
    sin, sseun = 1, 0
    for s, ss in johap:  # 재료 하나의 신맛, 쓴맛값을 계산
      sin *= s
      sseun += ss
      # print("i:",i, ", johap:", johap, ", s:",s,", ss", ss)

    result = min(result, abs(sin - sseun))
    # print(abs(sin - sseun))

print(result)