# 중앙값 구하기

import sys
import heapq
import math

def getMiddle(inputs):  #입려값 전체를 파라미터로 받음
  left_heap = []  # max heap
  right_heap = []  # min heap
  # 1. left_heap(최대 힙)의 첫번째 값 = 최댓값,
  # 2. right_heap(최소 힙)의 첫번째 값 = 최솟값
  # 3. 현재값
  # 1~3을 비교해서 중앙에 오는 값을 middle로
  # 2에서 중앙값이 나오면 2에서 pop해서 middle로 만들고 현재값을 2로 push 
  # 1에서 중앙값이 나오면 1에서 pop해서 middle로 만들고 현재값을 1로 push  
  middle = inputs[0]  # 첫 번째 중앙값(데이터 하나일 때)(min_heap, max_heap 없이 구할 수 있음)

  print(middle, end = ' ')
  
  for i, x in enumerate(inputs[1:], start = 1):
    if x > middle:
      heapq.heappush(left_heap, x)
    else:
      heapq.heappush(right_heap, (-x, x))

    if i % 2 == 0: #홀수번째 수일때(=i는 짝수)
      if len(right_heap) < len(left_heap):
        heapq.heappush(right_heap, (-middle, middle))
        middle = heapq.heappop(left_heap)
      elif len(right_heap) > len(left_heap):
        heapq.heappush(left_heap, middle)
        middle = heapq.heappop(right_heap)[1]

      print(middle, end = ' ')   
    if (i+1) % 20 == 0 or i == len(inputs) - 1:
      print()
      
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  m = int(input())
  inputs = []
  print(math.ceil(m / 2))
  if m % 10 == 0:
    for _ in range(m // 10):
      inputs.extend(list(map(int, input().split())))
  else:
    for _ in range(m // 10 + 1):
      inputs.extend(list(map(int, input().split())))
  getMiddle(inputs)