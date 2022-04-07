# 세로읽기
import sys

input = sys.stdin.readline
inputs = list()
result = list()

for i in range(5):
  inputs = input().split()

print(len(max(inputs, key = len)))
