# 계수 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array)+1)

# for i in range(len(count)):
#   for j in range(len(array)):
#     if i == array[j]:
#       count[i] += 1

# 위 코드를 아래와 같이 줄일 수 있음
# 시작
for i in range(len(array)):
  count[array[i]] += 1
# 끝
  
for i in range(len(count)):
  for j in range(count[i]):
    print(i, end = ' ')
  
  