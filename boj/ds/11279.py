# 최대 힙

import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
  x = int(input())
  if x == 0:
    # 힙에서 index == 0 출력 + 제거
    if heap:
      print(-1 * heapq.heappop(heap))
    else:
      print("0")
  else:
    # 힙에 x 넣기
    heapq.heappush(heap, -x)