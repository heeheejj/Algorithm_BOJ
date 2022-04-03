# 더하기 사이클

count = 0
def func(x):
  
  global count
  
  if x == n and count != 0:
    return
    
  count += 1
  
  if x < 10:
    return func((x % 10)*10 + x) 
  else:
    return func((x % 10)*10 + (x // 10 + x % 10) % 10)
    
n = int(input())

func(n)
print(count)