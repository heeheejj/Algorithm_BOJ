from collections import deque

queue = deque([3,5,1,2,6])

while queue:  # queue가 빌 때까지 반복! 정확한 원리는 모르겠다..
  queue.popleft()
  print(queue)