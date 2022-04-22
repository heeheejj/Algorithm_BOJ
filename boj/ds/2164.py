# 카드2

import sys
from collections import deque

def task(q):
  while q:
    if len(q) == 1:
      print(q.popleft())
      break
    q.popleft()
    q.append(q.popleft())

input = sys.stdin.readline

n = int(input().rstrip())

q = deque([x for x in range(1, n+1)])

task(q)