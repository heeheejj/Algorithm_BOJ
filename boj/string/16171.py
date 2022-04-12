# 나는 친구가 적다 (Small)

str = input()
key = input()
new_str = str
for i in range(len(str)):
  if str[i].isdigit():
    new_str = new_str.replace(str[i], "")

if key in new_str:
  print("1")
else:
  print("0")