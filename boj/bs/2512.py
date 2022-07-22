# 예산

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())

maxBudget = -1

if sum(arr) <= M:  # 모든 요청이 배정될 수 있는 경우 -> 요청한 금액 그대로 배정
  maxBudget = max(arr)

else:  # 모든 요청이 배정될 수 없는 경우 -> 상한액 정하기
  low, high = 0, max(arr)
  while low <= high:
    mid = (low + high) // 2
    # mid를 상한액으로 해서 예산을 배정하고,
    # 총 예산이 M 이상이면 -> high를 바꿔
    # M보다 작으면 -> low를 바꿔
    sum = 0
    for i in range(N):
      if arr[i] > mid:
        sum += mid
      else:
        sum += arr[i]
    if sum <= M:
      low = mid + 1
    else:
      high = mid - 1
  maxBudget = high

print(maxBudget)