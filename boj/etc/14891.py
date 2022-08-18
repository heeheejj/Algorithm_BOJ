# 톱니바퀴

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

wheels = [input().rstrip() for _ in range(4)]
print(wheels)
K = int(input())
isLeftDone, isRightDone = False, False
for _ in range(K):
  wheelNum, dir = map(int, input().split())  # wheelNum: 회전시킨 톱니바퀴의 번호, dir: 회전시킨 방향
  leftNum, rightNum = wheelNum - 1, wheelNum  #leftNum: 왼쪽방향으로 톱니바퀴 번호 확인
  print("직후",rightNum, wheelNum)
  lDir, rDir = dir, dir
  
  while leftNum > 0:  # 두번째 톱니바퀴까지(왼쪽 톱니바퀴 확인해야하니까)
    if isLeftDone:
      break
    wheelStates = list(wheels[leftNum]) # 회전 방향대로 회전하기
    if lDir == 1:  # 시계 방향
      wheels[leftNum] = list(wheelStates[-1])+list(wheelStates[:-1])
    else:  # 반시계 방향
      wheels[leftNum] = list(wheelStates[1:])+list(wheelStates[0])
    
    nextNum = leftNum - 1
    print("left:",nextNum, leftNum, wheels)
    if wheels[nextNum][2] == wheels[leftNum][6]:  # 같은 극이면
      isLeftDone = True
      break
    else:  # 다른 극이면 다음 톱니바퀴의 회전방향 바꾸고 회전
      lDir *= -1
    leftNum -= 1

  while rightNum < 3:  # 세번째 톱니바퀴까지(오른쪽 톱니바퀴 확인해야하니까)
    print(rightNum,"엥")
    if isRightDone:
      break
    if rightNum != wheelNum-1:
      wheelStates = wheels[rightNum] # 회전 방향대로 회전하기
      if rDir == 1:  # 시계 방향
        wheels[rightNum] = list(wheelStates[-1])+list(wheelStates[:-1])
      else:  # 반시계 방향
        wheels[rightNum] = list(wheelStates[1:])+list(wheelStates[0])
    nextNum = rightNum + 1
    print("right:",nextNum, rightNum, wheels)
    if wheels[nextNum][6] == wheels[rightNum][2]:  # 같은 극이면
      isRightDone = True
      print("끝")
      break
    else:  # 다른 극이면 다음 톱니바퀴의 회전방향 바꾸고 회전
      rDir *= -1
    rightNum += 1 
    

result = 0
if wheels[0][0] == '1':
  result += 1
if wheels[1][0] == '1':
  result += 2
if wheels[2][0] == '1':
  result += 4
if wheels[3][0] == '1':
  result += 8

print(result)