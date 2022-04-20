# 요세푸스 문제 - 116ms (더 빠름)
n, k = map(int, input().split())

a = [x+1 for x in range(n)]
result = list()
jmp = 0
while len(result) != n:
  jmp += (k - 1)
  if jmp >= len(a):
    jmp %= len(a)
  result.append(str(a.pop(jmp)))
print("<", ", ".join(result), ">", sep = "")  # sep = ""하는 이유 -> print("<", ~) 하면 콤마할 때 자동띄어쓰기되는데 sep = ""해서 없앰 