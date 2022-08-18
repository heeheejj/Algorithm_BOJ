# 잃어버린 괄호

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

str = input()
len = len(str)
result = 0
tempMinus = 0
tempPlus = 0
isFirstMinus = True
for i in range(len):
  x = str[i]
  if x == '-':
    if isFirstMinus:
      result = tempPlus
      tempPlus = ''
      isFirstMinus = False
    else:    
      result -= eval(tempStr)
      tempStr = ''
  else:
    if x == '+':
      tempPlus 
    if x == '0' and tempStr == '':
      continue
    tempStr += x

  if i == len-1:
    result -= eval(tempStr)

if isFirstMinus:  # for문이 다 끝나도 isFirstMinus가 True이면 -가 없는 수식
  result *= -1
print(result)
