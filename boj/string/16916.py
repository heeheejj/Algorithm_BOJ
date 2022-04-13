# 부분 문자열
# 시간 초과 - 수정 필요

import sys

input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

if p in s:
  print("1")
else:
  print("0")