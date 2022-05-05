# N번째 큰 수

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
  nums = list(map(int, input().split()))
  if not heap:  # 힙에 값이 없다면 n개 전부 넣어줌
    for num in nums:
      heapq.heappush(heap, num)
  else:  # 힙에 값이 있다면 최솟값 확인하는 과정
    for num in nums:
      if num > heap[0]:  # 힙의 최솟값보다 현재 값이 크면 교체
        heapq.heappop(heap)
        heapq.heappush(heap, num)
    
print(heap[0])