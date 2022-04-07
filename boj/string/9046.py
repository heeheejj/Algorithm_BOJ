# 복호화

import sys

input = sys.stdin.readline 
t = int(input())
inputs = list()
result = list()

for i in range(t):
  inputs = input().split()

print(max(len(inputs)))