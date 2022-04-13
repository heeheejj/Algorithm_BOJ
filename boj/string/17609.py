# 회문
# 시간 초과 -> 수정 필요

import sys

def getResult(str):
  if str == str[::-1]:
    return "0"
  else:
    for i in range(len(str)):
      _str = list(str)
      del _str[i]
      if _str == _str[::-1]:
        return "1"
    return "2"

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  str = input().rstrip()
  print(getResult(str))