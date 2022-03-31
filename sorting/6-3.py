# 성적이 낮은 순서로 학생 출력하기

n = int(input())

array = []

def setting(data):
  return data[1]
  
for i in range(n):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1])))

result = sorted(array, key = setting)

for i in range(n):
  print(result[i][0], end = ' ')