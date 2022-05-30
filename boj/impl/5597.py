# 과제 안 내신 분..?

import sys

# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

inputs = [int(input()) for _ in range(28)]

for i in range(1, 31):
  if i not in inputs:
    print(i)