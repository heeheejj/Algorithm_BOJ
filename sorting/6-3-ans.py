# 성적이 낮은 순서로 학생 출력하기 (람다함수 사용)

n = int(input())

array = []

def setting(data):
  return data[1]
  
for i in range(n):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1])))

array = sorted(array, key = lambda student: student[1])

for i in array:
  print(i[0], end = ' ')