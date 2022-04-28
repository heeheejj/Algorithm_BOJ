# 괄호 제거
# exp가 왜 변하는지 모르겠다............................-> 19행에 exp 뒤에 [:]
# 주의: a = list() 가 있을 때,
# b = a 이렇게 대입하면 a 리스트의 reference가 대입된다.
# 그래서 b 리스트의 원소를 변경하면 a 리스트도 변경됨
# 그냥 복제를 해서 넣고싶다면 b = a[:]라고 대입해야한다.
# https://stackoverflow.com/questions/4081561/what-is-the-difference-between-list-and-list-in-python
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
  for x in combinations(brk_idx, i):
    # print("x", x)
    temp = exp[:]    
    for l, r in x:
      temp[l] = ''
      temp[r] = ''
    # 여기서 지워서 result에 저장
    result.append(''.join(temp))
result = list(set(result))  # 괄호가 여러개 중첩돼있다면 ex) (((1)))(2) 조합을 돌려도 같은 결과가 나올 수 있음! 중복제거해주자
for x in sorted(result):
  print(x)