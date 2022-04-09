# 단어 정렬

import sys
  
input = sys.stdin.readline

n = int(input())
words = list()

for _ in range(n):
  word = input().rstrip()
  words.append(word)

words = list(set(words))  #중복 제거

# 알파벳 순 정렬 후 길이순 정렬을 해야 길이가 같을 때 알파벳 순 정렬이 된다.
# 반대로 길이순 정렬을 하고 알파벳 순 정렬을 하면 그냥 알파벳 순 정렬이 될 것이다!
words.sort()  
words.sort(key = len)

for word in words:
  print(word)