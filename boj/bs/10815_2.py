# 숫자 카드
# set 이용

import sys

sys.stdin = open("input.txt","r")

input = sys.stdin.readline

N = int(input())
a = set(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

for x in b:  # M개의 숫자카드에 대해서
  if a & set([x]):
    print("1", end=' ')
  else:
    print("0", end=' ')
print()