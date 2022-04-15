# 위에서 아래로

n = int(input())
list = []
for i in range(n):
    list.append(int(input()))

# list.sort()
# for i in range(len(list), 0, -1):
#   print(list[i-1], end=' ')
# 위 코드는 아래처럼 가능

result = sorted(list, reverse = True)
for i in range(n):
  print(result[i], end=' ')