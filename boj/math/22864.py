# 피로도
# 10:51~11:15
a, b, c, m = map(int, input().split())

p = 0
amountOfWork = 0

for i in range(24):
  if p + a <= m:
    p += a
    amountOfWork += b
  else:
    p -= c
    if p < 0:
      p = 0

print(amountOfWork)