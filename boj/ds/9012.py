# 괄호

import sys

input = sys.stdin.readline

def isVPS(str):
  stack = list()
  for x in str:
    if x == "(":
      stack.append(x)
    else:
      try:
        stack.pop()
      except:
        return False
  if not stack:  # 스택이 비어있으면
    return True
  else:
    return False
        
t = int(input())
for _ in range(t):
  a = list(input().rstrip())
  if isVPS(a):
    print("YES")
  else:
    print("NO")