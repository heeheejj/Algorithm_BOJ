# 괄호 제거
# exp가 왜 변하는지 모르겠다............................
from itertools import combinations

exp = list(input())
brk_idx = list()  # 튜플(여는괄호idx, 닫는괄호idx)을 담는 리스트
left_brk_idx = list() # 여는 괄호를 잠시 저장해놓는 스택
result = list()  # 결과 문자열을 리스트에 저장
for i in range(len(exp)):
  if exp[i] == ')': # 닫는 괄호면
    brk_idx.append((left_brk_idx.pop(), i))
  elif exp[i] == '(':  # 여는 괄호면
    left_brk_idx.append(i)

for i in range(1, len(brk_idx)+1):
  print("before",exp[:])
  for x in combinations(brk_idx, i):
    print("x", x)
    
    for l, r in x:
      temp = exp[:]
      
      print("l",l,' r',r)
      temp[l] = ''
      temp[r] = ''
      print("after",temp)
    # 여기서 지워서 result에 저장
    # print("heee",''.join(temp))
    result.append(''.join(temp))

# result.sort()
for x in result:
  print(x)