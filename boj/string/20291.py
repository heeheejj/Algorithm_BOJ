# 파일 정리

import sys

input = sys.stdin.readline

n = int(input())

result = {}
for _ in range(n):
  ext = input().rstrip().split(".")[1]
  if ext in result:
    result[ext] += 1
  else:
    result[ext] = 1
    
keys = list(result.keys())
keys.sort()

for key in keys:
  print(key, result[key])