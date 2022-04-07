# 복호화

import sys

input = sys.stdin.readline 
t = int(input())
input_string = ""

alp = 'abcdefghijklmnopqrstuvwxyz'

for i in range(t):
  input_string = input().rstrip()
  frequency = [0] * 26
  for alphabet in input_string:
    try:
      frequency[alp.index(alphabet)] += 1
    except:
      continue
  mf = max(frequency)
  if frequency.count(mf) == 1:
    print(alp[frequency.index(mf)])
  else:
    print("?")