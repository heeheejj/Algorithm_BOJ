# 그룹 단어 체커

import sys

def isGroupWord(word):
  alph = list()
  for i in range(len(word)):
    temp_alph = word[i]
    if temp_alph not in alph:  # 지금까지 확인한 알파벳 리스트에 없으면 추가
      alph.append(temp_alph)
    else:  # 리스트에 있으면,
      if temp_alph != word[i-1]:  # 리스트에 있는데 이전 인덱스의 단어와 일치하지 않으면 그룹단어가 아님
        return False
  return True

input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
  if isGroupWord(input().rstrip()):
    count += 1

print(count)