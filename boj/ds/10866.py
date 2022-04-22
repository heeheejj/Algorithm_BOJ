# 덱

import sys
from collections import deque

def push_front(x):
  q.appendleft(x)

def push_back(x):
  q.append(x)

def pop_front():
  if q:
    print(q.popleft())
  else:
    print("-1")

def pop_back():
  if q:
    print(q.pop())
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
  if cmd == "push_front":
    push_front(inputs[1])
  elif cmd == "push_back":
    push_back(inputs[1])
  elif cmd == "pop_front":
    pop_front()
  elif cmd == "pop_back":
    pop_back()
  elif cmd == "size":
    print(len(q))
  elif cmd == "empty":
    empty()
  elif cmd == "front":
    front()
  elif cmd == "back":
    back()