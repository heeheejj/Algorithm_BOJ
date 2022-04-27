# 풍선 터뜨리기
from collections import deque
n = int(input())
bal = deque(map(int, input().split()))
idx = deque([x+1 for x in range(n)])
for _ in range(n):
  step = bal.popleft()
  print(idx.popleft(), end=' ')

  if step > 0:
    step -= 1 # 첫번째 원소를 pop했기때문에 오른쪽으로 이동할 경우(=step > 0일 경우) 한칸 덜 옮겨준다.
  bal.rotate(step*-1)  # 양수일 때 오른쪽으로 회전, 음수일 때 왼쪽으로 회전하므로 문제의 조건과 반대 -> -1 곱해주기
  idx.rotate(step*-1)
