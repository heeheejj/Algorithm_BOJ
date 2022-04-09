# 그룹 단어 체커 - 다른 풀이

import sys

input = sys.stdin.readline

n = int(input())

count = 0
for i in range(n):
  word = input().rstrip()
  if list(word) == sorted(word, key=word.find): # 기존 위치 그대로 같은 알파벳끼리 붙어있게 정렬(그룹단어 그 자체)
    count += 1

print(count)