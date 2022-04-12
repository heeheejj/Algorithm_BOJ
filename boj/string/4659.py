# 비밀번호 발음하기

import sys

def isSatisfiedCondition(s):
  cond1 = False
  cond2 = True
  cond3 = True
  for x in s:
    if x in vowel:
      cond1 = True
      break
  for i in range(len(s) - 2):
    if s[i] in vowel and s[i+1] in vowel and s[i+2] in vowel:
      cond1 = False
      break
    if s[i] not in vowel and s[i+1] not in vowel and s[i+2] not in vowel:
      cond2 = False
      break
  for i in range(len(s) - 1):
    if s[i] == s[i+1]:
      if (s[i] != 'o' or s[i+1] != 'o') and (s[i] != 'e' or s[i+1] != 'e'):
        cond3 = False
        break
  if cond1 == True and cond2 == True and cond3 == True:
    return True
  else:
    return False

input = sys.stdin.readline
vowel = ['a', 'e', 'i', 'o', 'u']

while True:
  str = input().rstrip()
  if str == 'end':
    break
  if isSatisfiedCondition(str):
    print(f'<{str}> is acceptable.')
  else:
    print(f'<{str}> is not acceptable.')