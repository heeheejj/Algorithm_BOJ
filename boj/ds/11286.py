# 절댓값 힙

import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
  x = int(input().rstrip())
  if x == 0:  # 절댓값이 가장 작은 값을 출력 + 제거
    if heap:
      print(heapq.heappop(heap)[1])
    else:
      print("0")
  elif x > 0:
    heapq.heappush(heap, (x, x))
  else:  # x < 0 일 때
    heapq.heappush(heap, (-x, x))