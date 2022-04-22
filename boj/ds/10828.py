# 스택

import sys

def push(x):
  stack.append(x)

def pop():
  if stack:
    print(stack.pop())
  else:
    print("-1")

def empty():
  if not stack:
    print("1")
  else:
    print("0")

def top():
  if stack:
    print(stack[-1])
  else:
    print("-1")

input = sys.stdin.readline
stack = list()
n = int(input())
for _ in range(n):
  inputs = list(input().rstrip().split())
  cmd = inputs[0]
  if cmd == "push":
    push(inputs[1])
  elif cmd == "pop":
    pop()
  elif cmd == "size":
    print(len(stack))
  elif cmd == "empty":
    empty()
  elif cmd == "top":
    top()