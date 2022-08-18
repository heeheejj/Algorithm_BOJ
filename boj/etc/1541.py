# 잃어버린 괄호

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
str = input()
len = len(str)
result = 0
tempStr = ''
isFirstMinus = True
for i in range(len):
  x = str[i]
  if x == '-':
    tempSum = sum(list(map(int, tempStr.split('+'))))
    tempStr = ''
    if isFirstMinus:
      result = tempSum
      isFirstMinus = False
    else:    
      result -= tempSum
  else:
    tempStr += x

  if i == len-1:
    tempSum = sum(list(map(int, tempStr.split('+'))))
    result -= tempSum

if isFirstMinus:
  result *= -1
print(result)