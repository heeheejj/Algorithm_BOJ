# 입국심사
# 입국 심사 시간을 인자로 받아 몇 명을 심사할 수 있는지를 체크하는 함수를 작성
# :직접적으로 문제에서 요구하는 것은 입국 심사 시간의 최솟값이나 이를 바로 구하기 어려우므로
# 역으로 가능한 시간들을 함수에 대입해서 범위를 줄여나가는 방식 선택
# count함수에서 나온 인원수가 m명보다 많으면 그 시간이 가능한 것이다. & 나온 인원수가 m명보다 적으면 그 시간은 불가능하다.
# 출처: https://junhwanlog.tistory.com/16

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
time = [int(input()) for _ in range(N)]

left, right = 1, M*(min(time))
result = 0
while left <= right:
  mid = (left + right)//2
  sum = 0
  for t in time:
    sum += (mid // t)
  if sum < M:
    left = mid + 1
  else:
    right = mid - 1
    result = mid
print(result)