# 나무 자르기
import sys

input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

lo, hi = 0, max(heights)
result = 0
while lo <= hi:
  sum = 0
  mid = (lo + hi) // 2
  for h in heights:
    temp = h - mid
    if temp > 0:
      sum += temp

  if M > sum:
    hi = mid - 1
  else:
    lo = mid + 1
    result = mid
    
print(result)