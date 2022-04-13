# 단어 뒤집기 2

str = input()
isTag = False  # True면 제대로 출력, False면 뒤집어서 출력
temp = str
result = ''

if str[0] == "<":
  isTag = True

for i in range(len(str)):
  if isTag == False:
    if str[i] == " ":
      idx = temp.index(" ")
      result += temp[idx-1::-1] + " "
      temp = temp[idx+1:]
    elif str[i] == "<":
      isTag = True
      if str[i-1] == ">": # ">" 다음 바로 "<" 나온 경우
        continue
      idx = temp.index("<")
      result += temp[idx-1::-1]
      temp = temp[idx:]
    elif i == len(str) - 1:
      result += temp[::-1]
  else:
    if str[i] == ">":
      isTag = False
      idx = temp.index(">")
      result += temp[:idx+1]
      temp = temp[idx+1:]
    elif str[i] == "<":  # ">" 다음 바로 "<" 나온 경우
      isTag = True
print(result)