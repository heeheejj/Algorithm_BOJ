# 블로그
# 슬라이딩 윈도우
# while문 사용 - 168ms
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
hits = list(map(int, input().split()))

start = 0 # 윈도우의 시작 포인터
sum_max = 0
window_sum = sum(hits[:x])
sum_max_cnt = 0

while start <= n - x:
  if n == x:
    sum_max = window_sum
    sum_max_cnt = 1
    break
  if sum_max < window_sum:
    sum_max = window_sum
    sum_max_cnt = 1
    
  elif sum_max == window_sum:
    sum_max_cnt += 1

  if start == n - x:
    break
  window_sum += hits[start+x] - hits[start]
  start += 1

if sum_max == 0:
  print("SAD")
else:
  print(sum_max)
  print(sum_max_cnt)