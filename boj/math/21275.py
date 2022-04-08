# 폰 호석만
# 4:57~
# ep jh 일 때도 Impossible 나옴...

def transform(x, n):
  result = 0
  for i in range(len(x)):
    if ord(x[i]) >= 97:
      result += (ord(x[i]) - 97 + 10) * n**(len(x) - 1 - i)
    else:
      result += int(x[i])*n**(len(x) - 1 - i)
  return result

Xa, Xb = input().split()

alph = list('0123456789abcdefghijklmnopqrstuvwxyz')
count = 0
X, A, B = 0, 0, 0


# for a in range(2, 37):
#   for b in range(2, 37):
#     temp_Xa = transform(Xa, a)
#     if temp_Xa == transform(Xb, b):
#       A, B = a, b
#       X = temp_Xa
#       count += 1
#       print("A = ", A, ", B = ", B, ", X = ", X, ", count = ", count)

# if count > 1 or X == 0:
#   print("Multiple")
# elif count == 1:
#   print(X, end = " ")
#   print(A, end = " ")
#   print(B, end = " ")
# else:
#   print("Impossible")