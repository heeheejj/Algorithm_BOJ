################# 미완
# 퀵 정렬
# 재귀함수 이용!
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

pivot = array[0] # 첫 번째 원소를 피벗으로 설정

def quick_sort(array, pivot):
  smaller = pivot # pivot보다 작은 값 초기값 세팅
  larger = pivot # pivot보다 큰 값 초기값 세팅
  for i in range(1, len(array)):
    if pivot < array[i]:
      smaller = i
  for i in range(len(array), 1, -1):
    if pivot > array[i]:
      larger = i
  if array
      

quick_sort(array, array[0])