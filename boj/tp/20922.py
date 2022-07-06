# 겹치는 건 싫어 - 실버1
# https://khu98.tistory.com/187
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
counter = [0] * (max(nums) + 1)

s, e = 0, 0
max_length = 0
while e < n:
  if counter[nums[e]] < k:  # end가 가리키는 수의 개수 확인
    counter[nums[e]] += 1
    e += 1
  else:  # end가 가리키는 수의 개수가 k개 이상이면 
    counter[nums[s]] -= 1
    s += 1
  max_length = max(max_length, e - s)
print(max_length)