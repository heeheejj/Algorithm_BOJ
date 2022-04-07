# !밀비 급일

import sys

input = sys.stdin.readline

while True:
  inputString = input().rstrip()
  if inputString == "END":
    break
  print(inputString[::-1])