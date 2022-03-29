# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
 
for i in range(1, len(array)):
  # array = [0, 5, 7, 9, 3, 1, 6, 2, 4, 8] / i = 4, array[i] = 3
  for j in range(i,0,-1):    # 첫판: i = 4, j = 4 //3, 2, 1, 0 ...
    if array[j-1] > array[j]:
      array[j-1], array[j] = array[j], array[j-1]
    else:
      break

print(array)