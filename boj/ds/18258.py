# 큐 2

import sys
from collections import deque

def push(x):
  q.append(x)

def pop():
  if q:
    print(q.popleft())
  else:
    print("-1")

def empty():
  if not q:
    print("1")
  else:
    print("0")

def front():
  if q:
    print(q[0])
  else:
    print("-1")

def back():
  if q:
    print(q[-1])
  else:
    print("-1")

input = sys.stdin.readline
q = deque()
n = int(input())
for _ in range(n):
  inputs = list(input().rstrip().split())
  cmd = inputs[0]
  if cmd == "push":
    push(inputs[1])
  elif cmd == "pop":
    pop()
  elif cmd == "size":
    print(len(q))
  elif cmd == "empty":
    empty()
  elif cmd == "front":
    front()
  elif cmd == "back":
    back()