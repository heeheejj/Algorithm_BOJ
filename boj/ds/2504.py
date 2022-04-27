# 괄호의 값

exp = ""  # expression:수식
stack = list()
flag = False # 이전 괄호가 닫힘 괄호일 때 True
isLast = False  # x가 input()의 마지막인지 아닌지
for x in input():
  if x == '(' or x == '[':  # 열림 괄호일 때
    stack.append(x)
    if flag:  # 이전 괄호가 닫힘 괄호이고 현재 열림 괄호일 때
      exp += "+"
      print(exp)
    flag = False
  else:  # 닫힘 괄호일 때
    last = stack.pop()
    if last == '(' and x == ')':
      exp += "2"
      print(exp)
    elif last == '[' and x == ']':
      exp += "3"
      print(exp)
    elif flag:  # 닫힘괄호인데 이전 괄호도 닫힘괄호였을 경우
      if x == ")": # 이전 괄호가 ")"든 "]"든 닫힘이었고, 현재 ")" 괄호일 때
        exp += "*2"
        print(exp)
      else:   # 이전 괄호가 ")"든 "]"든 닫힘이었고, 현재 "]" 괄호일 때
        exp += "*3"
        print(exp)
    else: # 닫힘괄호인데 (뒤에 바로 ]가 오거나 [뒤에 바로 )가 오게된 경우일 때 입력이 올바르지 못한 괄호열
      print("0")
      exit()
    if not stack:  # 스택이 비어있다면 현재까지 모든 괄호가 짝이 맞춰져 없어진 것. "(", ")"를 수식 앞뒤에 추가
      exp = "(" + exp + ")"
      print(exp)
    flag = True

print(exp)