# 프린터 큐
# 3:26~32 3:47~
# 문제 이해: 중요도 숫자가 큰 것을 먼저 인쇄.. 1이 제일 중요도 작음

import sys
from collections import deque

def printer(q, m):
  result = 1
  idx = m
  while True:
    print("mddj", max(list(q)))
    print("q[idx]", q[idx]," idx", idx)
    max_q = max(list(q))
    if idx == 0 & max_q == q[idx]:
      print(result)
      break
    if q[0] == max_q:
      q.popleft()
      result += 1
      if idx != 0:
        idx -= 1
      else:  # 타겟 문서가 첫번째에 왔지만 맨뒤로 보내져야 하는 경우
        idx = len(q)
    else:
      q.append(q.popleft())

      # 다른 문서가 뒤로 감으로써 타겟문서 인덱스 옮겨짐
      if idx != 0:
        idx -= 1
      else:  
        idx = len(q) - 1
input = sys.stdin.readline

k = int(input())  # 테스트케이스의 수
for _ in range(k):
  n, m = map(int, input().split())  # n: 문서의 개수, m: 타켓문서의 처음 인덱스(0부터)
  q = deque(map(int, input().split()))
  print("q",q)
  if n == 1:
    print("1")
  else:
    printer(q, m)