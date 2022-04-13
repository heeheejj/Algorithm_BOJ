# 염색체

import re, sys

input = sys.stdin.readline
regex = re.compile('^[A-F]{0,1}A+F+C+[A-F]{0,1}$')
t = int(input())

for i in range(t):
  str = input().rstrip()
  if regex.match(str) != None:
    print("Infected!")
  else:
    print("Good")