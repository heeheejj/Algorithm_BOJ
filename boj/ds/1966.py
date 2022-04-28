# 프린터 큐
# 3:26~32 3:47~
# 문제 이해: 중요도 숫자가 큰 것을 먼저 인쇄.. 1이 제일 중요도 작음

import sys
from collections import deque

input = sys.stdin.readline

k = int(input())  # 테스트케이스의 수
for _ in range(k):
  n, m = map(int, input().split())  # n: 문서의 개수, m: 타켓문서의 처음 인덱스(0부터)
  q = deque(map(int, input().split()))
  idx = deque([x for x in range(0, n)])
  order = 1
  while True:
    if q[0] == max(q):
      if idx[0] == m:
        print(order)
        break
      else:
        q.popleft()
        idx.popleft()
        order += 1
    else:  # 큐의 첫번째 원소가 가장 큰 원소가 아니면 맨뒤로 보내기
      q.append(q.popleft())
      idx.append(idx.popleft())