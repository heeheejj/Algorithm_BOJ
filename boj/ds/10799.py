# 쇠막대기

# 반복문으로 문자열 하나씩 검사 -> 스택에 '(' 만 push, pop
# flag : '('가 나오면 true, ')'가 나오면 False. 다음 iteration에서 전에꺼가 '('가 맞는지 체크, 즉 맞으면 '()'쌍임
# if '(' 나오면: push, flag = True
# else: (')'나오면)
#   if flag: '()'쌍일 때 '('하나 pop, pop하고나서 cnt += stack 길이(=스택에있는 '('의 개수)
#   else: 쌍이 아닌 ')'일 때 '('하나 pop, cnt += 1
#   flag = False

string = input()
stack = list()
flag = False # '('가 나오면 true, ')'가 나오면 False 다음 iteration에서 전에꺼가 '('가 맞는지 체크하기 위한 용도
result = 0
for x in string:
  if x == '(':
    stack.append(x)
    flag = True
  else:  # ')'일 때
    stack.pop()
    if flag:  # '()'쌍일 때
      result += len(stack)
    else:  # '()'쌍이 아닌 ')'일 때
      result += 1
    flag = False
print(result)