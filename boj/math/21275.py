# 폰 호석만
# 4:57~
# ep jh 일 때도 Impossible 나옴...
Xa, Xb = input().split()

# x = list('0123456789abcdefghijklmnopqrstuvwxyz')
count = 0
X, A, B = 0, 0, 0

for a in range(2, 37):
  for b in range(2, 37):
    try:
      Xa = int(Xa, a)
      Xb = int(Xb, b)
      A = a
      B = b
      print(str(Xa)+"/"+str(Xb))
      if Xa == Xb:
        count += 1
        X = Xa
      else:
        continue
    except:
      continue
  
if count > 1:
  print("Multiple")
elif count == 1:
  if X == 0:
    print("Multiple")
  else:
    print(X, end = " ")
    print(A, end = " ")
    print(B, end = " ")
else:
  print("Impossible")