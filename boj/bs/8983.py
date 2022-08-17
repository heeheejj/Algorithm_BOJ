# 사냥꾼

import sys
from bisect import bisect_left
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

M, N, L = map(int, input().split())
gun = list(map(int, input().split()))  # 사대의 x좌표값

gun.sort()

cnt = 0
for i in range(N):
  x, y = map(int, input().split())
  if y > L:  # 동물의 y좌표가 이미 L보다 크다면 pass
    continue

  # 동물의 x좌표가 가장 왼쪽사대보다 왼쪽이거나 가장 오른쪽사대보다 오른쪽이라면, 이분탐색을 돌려 x와 가장 가까운 사대를 찾을 필요가 없다.
  if x < gun[0]:
    if gun[0]-x+y <= L:
      cnt += 1
      continue
  elif x > gun[-1]:
    if x-gun[-1]+y <= L:
      cnt += 1
      continue
  else:  # 가장 왼쪽사대 x좌표 <= 동물의 x좌표 <= 가장 오른쪽사대 x좌표라면, 이분탐색으로 동물의 x좌표와 가장 가까운 사대를 찾는다. 
    idx = bisect_left(gun, x)  # x와 가장 가까우면서 x보다는 큰 gun의 idx값
    if x-gun[idx - 1] + y <= L or gun[idx]-x + y <= L:  # 이분탐색으로 x와 가장 가까우면서 x보다는 큰 gun을 찾았다. x보다 작은 gun 중 x와 가장 가까운 idx-1번째 gun도 생각해주면서 거리가 L이하인지 체크한다.
      cnt += 1

print(cnt)