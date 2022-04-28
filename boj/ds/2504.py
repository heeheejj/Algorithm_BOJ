# 괄호의 값
# test case: ]], ()(]]
# 반례: ()[[()]()()]()

exp = ""  # expression:수식
stack = list()
flag = False # 이전 괄호가 닫힘 괄호일 때 True
last = ""

inputs = input()
if not inputs.count("(") == inputs.count(")") and inputs.count("[") == inputs.count("]"):
  print("0")
  exit()
for x in inputs:
  if x == '(' or x == '[':  # 열림 괄호일 때
    stack.append(x)
    if flag:  # 이전 괄호가 닫힘 괄호이고 현재 열림 괄호일 때
      exp += "+"
      print(exp)
    flag = False
    last = x
  else:  # 닫힘 괄호일 때
    if stack:
      stack.pop()
    else:  # 스택에 아무것도 없는데 닫힘괄호가 나오면 올바르지 못한 괄호열
      print("0")
      exit()
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
      exp = str(eval(exp))  # exp = "(" + exp + ")" 이랑 같은건데 그냥 괄호를 미리 계산해줌
      print(exp)
    else: # 닫힘괄호인데 (뒤에 바로 ]가 오거나 [뒤에 바로 )가 오게된 경우일 때 입력이 올바르지 못한 괄호열
      print("0")
      exit()
    flag = True
    last = x

print(eval(exp))