# 숫자 카드
# binary search (=이분탐색=이진탐색)
# 시간 초과.....

import sys

sys.stdin = open("input.txt","r")

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

a.sort()  # 이진탐색을 위해 a의 데이터 정렬
for x in b:  # M개의 숫자카드에 대해서
  start, end = 0, N-1
  result = 0
  while start <= end:
    mid = (start + end) // 2
    if x == a[mid]:
      result = 1
    elif x < a[mid]:  # target이 중간점보다 왼쪽에 있다면
      end = mid - 1
    else:  # target이 중간점보다 오른쪽에 있다면
      start = mid + 1
  print(result, end = ' ')