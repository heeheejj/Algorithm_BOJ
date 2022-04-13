# 듣보잡

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
deutmot = set()  # 듣도 못한 사람 리스트
bomot = set()    # 보도 못한 사람 리스트

for _ in range(n):
  deutmot.add(input().rstrip())

for _ in range(m):
  bomot.add(input().rstrip())

deutbo = list(deutmot.intersection(bomot))  # 듣보 리스트

deutbo.sort()
print(len(deutbo))
for x in deutbo:
  print(x)