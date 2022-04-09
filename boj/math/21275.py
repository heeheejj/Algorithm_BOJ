# 폰 호석만
# 4:57~
import time
start = time.time()

def transform(x, n):
  result = 0
  for i in range(len(x)):
    if ord(x[i]) >= ord('a'):
      result += (ord(x[i]) - ord('a') + 10) * n**(len(x) - 1 - i)
    else:
      result += int(x[i])*n**(len(x) - 1 - i)
  return result

Xa, Xb = input().split()

alph = '0123456789abcdefghijklmnopqrstuvwxyz'
count = 0
X, A, B = -1, 0, 0

max_Xa, max_Xb = 2, 2
for i in range(len(Xa)):
  max_Xa = max(max_Xa, alph.find(Xa[i])+1)
  # 10(a)진법이면 0~9까지 쓰니까
  # 예를들어 p가 최대값이면, (p+1)진법부터 가능성 있음

for i in range(len(Xb)):
  max_Xb = max(max_Xb, alph.find(Xb[i])+1)

# print("max_Xa = ", max_Xa)
# print("max_Xb = ", max_Xb)


for a in range(max_Xa, 37): 
  for b in range(max_Xb, 37):
    temp_Xa = transform(Xa, a)
    if a == b or temp_Xa >= 2**63:
      break
    if temp_Xa == transform(Xb, b):
      A, B = a, b
      X = temp_Xa
      count += 1
      # print("A = ", A, ", B = ", B, ", X = ", X, ", count = ", count)

if count > 1 or X == 0:
  print("Multiple")
elif count == 1:
  print(X, " ", A, " ", B)
else:
  print("Impossible")

print("time :", time.time() - start)