# 부분 문자열

import sys

input = sys.stdin.readline
while True:
  try:
    s, t = input().rstrip().split()
    k = 0
    j = 0
    flag = 0
    for i in range(len(t)):
      if s[j] == t[i]:
        j += 1
        if j == len(s):
          flag = 1
          break
    if flag == 0:
      print("No")
    else:
      print("Yes")
  except:
    break