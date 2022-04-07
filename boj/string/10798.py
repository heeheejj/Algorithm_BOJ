# 세로읽기
import sys

input = sys.stdin.readline
inputs = list()
result = ""

for i in range(5):
  inputs.append(input().rstrip())

max_length = len(max(inputs, key = len))

for j in range(max_length):
  t_string = ""
  for i in range(5):
    if (len(inputs[i]) - 1) >= j:  # inputs[i] 문자열의 마지막 인덱스가 j보다 작으면 pass
      t_string += inputs[i][j]
  result += t_string

print(result)