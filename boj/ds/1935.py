# 후위 표기식2

import sys

input = sys.stdin.readline

n = int(input())

string = list(input())
num = list()
stack = list()

for i in range(n):
  num.append(input().rstrip())  # num : 알파벳에 대응하는 숫자 ABC 순서대로 (string으로 저장)

for x in string:
  _x = ord(x)
  if (ord('A') <= _x) & (_x <= ord('Z')):
    stack.append(num[_x - ord('A')])  # ex) _x = 'B'일 때, _x - ord('A') = 1이고 num[1]에 있는 수는 곧 B에 대응하는 숫자임 
  else:
    x1 = stack.pop()
    if not stack: # 스택이 비어있으면
      print("%.2f" %float(x1))
      break
    x2 = stack.pop()
    result = eval(x2+x+x1)
    stack.append(str(result))