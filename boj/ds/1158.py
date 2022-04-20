# 요세푸스 문제 - 220ms
from collections import deque
n, k = map(int, input().split())

print("<", end = '')
q = deque([x+1 for x in range(n)])

for i in range(n):
  q.rotate(1-k)  
  if i == n-1:
    print(q.popleft(), end=">")
  else:
    print(q.popleft(), end=", ")
print()