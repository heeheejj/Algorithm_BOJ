# 한수

n = int(input())

def isHan(x):
  x_str = str(x)
  if len(x_str) == 1:
    return True
  
  d = int(x_str[1]) - int(x_str[0]) # 공차 
  a = int(x_str[0])  # 첫번째 항
  # print("x:", x,", a:", a, ", d:", d)
  for n in range(1, len(x_str)):
    # print("x:", x, ", n:", n, ", x_str[n]:", x_str[n])
    if int(x_str[n]) != a + d * n:  # 등차수열이 아니게 되는 순간에 False return
      return False
  return True  # for문을 무사히 다 돌면 True return

result = 0
for i in range(1, n+1):
  if isHan(i):
    result += 1

print(result)