# 피보나치 수 2 - 재귀 (top-down)

def fibo(x):
  if x == 0:
    return 0
  if x == 1 or x == 2:
    return 1
  if not d[x] == 0:
    return d[x]

  d[x] = fibo(x - 1) + fibo(x - 2)
  return d[x]

d = [0] * 91
n = int(input())
print(fibo(n))