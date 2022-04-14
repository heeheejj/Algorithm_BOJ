# 회문
# 투 포인터 적용

import sys

# 투 포인터 이용하여 유사팰린드롬인지 확인
def getResult(string):  # 문자열리스트와 뒤집은 문자열리스트를 파라미터로
  if string == string[::-1]:
    return 0
  
  n = len(string)  # string의 길이 = reversed string의 길이
  l, r = 0, n-1
  while l < r:
    if string[l] != string[r]:
      # l을 +1해서 회문 확인
      if string[l+1:r+1] == string[r:l:-1]:
        return 1
        
      # r을 -1해서 회문 확인
      if l == 0:  # l == 0인 경우 string[r-1:l-1:-1] 할 때 두번째 인자가 -1이 되어서 null을 반환하므로 0일때를 따로 빼줌
        if string[l:r] == string[r-1::-1]:
          return 1
      elif string[l:r] == string[r-1:l-1:-1]:
        return 1
      return 2
    else:  # l의 문자와 r의 문자가 같으면 l++, r--해줌
      l += 1
      r -= 1
  
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  str = input().rstrip()
  print(getResult(str))