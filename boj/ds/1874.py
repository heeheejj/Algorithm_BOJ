# 스택 수열

# 1부터 N까지의 수가 스택에 있는 상태이고, pop해서 나온 순서 = 입력 수열이 되도록 만드는거

import sys

input = sys.stdin.readline

n = int(input())

stack = list()
op = list()
cnt = 1
flag = True
for i in range(n):
  seq = int(input())
  while cnt <= seq:  # cnt가 seq보다 크면 지금 input으로 들어온 수가 이미 스택에 있는거니까 안넣어도 됨
    stack.append(cnt)
    op.append("+")
    cnt += 1
  
  if stack[-1] == seq:  # cnt
    stack.pop()
    op.append("-")
  else: # 스택 맨 위의 숫자와 cnt가 동일하지 않으면 수열을 만들 수 없음
    flag = False
    break

if flag:
  for x in op:
    print(x)
else:
  print("NO")