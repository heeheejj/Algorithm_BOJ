# 블로그
# 슬라이딩 윈도우
# for문, 21921_2.py 이해쉽게 고친ver - 172ms

import sys

input = sys.stdin.readline

n, x = map(int, input().split())
hits = list(map(int, input().split()))

sum_max = 0
window_sum = sum(hits[:x])
sum_max_cnt = 0

for start in range(n-x+1):
  if sum_max < window_sum:
    sum_max = window_sum
    sum_max_cnt = 1
  elif sum_max == window_sum:
    sum_max_cnt += 1

  if start == n - x:  # start가 n-x면 마지막 윈도우이므로 다음 window_sum을 구하지 않음
    break
  window_sum += hits[start+x] - hits[start]

if sum_max == 0:
  print("SAD")
else:
  print(sum_max)
  print(sum_max_cnt)