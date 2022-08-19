# 캐슬 디펜스

import sys, itertools

def startGame(archYPosList, enemyPosList):
  global result
  global tempN
  global target
  targetCnt = 0
  while enemyPosList:
    lastEnemyPos = min(enemyPosList, key = lambda x:x[0])
    lastEnemyX = lastEnemyPos[0]
    if lastEnemyX == tempN:
      break
    targetCnt = getTarget(archYPosList, enemyPosList)
    attack(enemyPosList)
    moveEnemy(enemyPosList)
  result = max(result, targetCnt)
      
def getTarget(archYPosList, enemyPosList):
  # 공격 대상 적 찾기(적 인덱스), 적의 수 리턴
  global target  
  print("target 추가 전"+str(target))
  for aY in archYPosList:
    targetX, targetY = -1, -1
    minDist = 99
    enemyCnt = len(enemyPosList)
    for enemyIdx in range(enemyCnt):
      eX, eY = enemyPosList[enemyIdx][0], enemyPosList[enemyIdx][1]
    # for eX, eY in enemyPosList:
      dist = getDistance(aY, eX, eY, N)
      if dist < minDist:
        minDist = dist
        targetX, targetY = eX, eY
    if targetX != -1 and targetY != -1:
      target.append(enemyIdx)
  target = list(set(target))
  print("target 추가 후"+str(target))
  print("target: ",target," targetCnt:",len(target))
  return len(target)

def attack(enemyPosList):
  global target
  while target:
    print("targetIdx:"+str(target[0])+str(target[-1]))
    targetIdx = target.pop()
    
    del enemyPosList[targetIdx]
  print("공격 후 적 리스트:",enemyPosList)  

def moveEnemy(enemyPosList):
  global tempN
  tempN -= 1  # 모든 적 아래로 한칸 이동 == 성 위치 N을 -1하는걸로 대체

# def getDeletedEnemyCnt(enemyPosList, N):
#   enemyCnt = len(enemyPosList)
#   deletedCnt = 0
#   print("enemyPosList: ",enemyPosList)
#   tempN = N
#   lastEnemyPos = min(enemyPosList)  #가장 멀리있는 적의 x, y좌표
#   lastEnemyX = lastEnemyPos[0]
#   while lastEnemyX < tempN:  # 모든 적이 격자판에서 삭제될때까지 반복
#     minDist = 99
#     minDistEnemyPosSet = set()
#     for i in range(len(enemyPosList)):  # 공격 대상 적을 찾기
#       curX, curY =  enemyPosList[i][0], enemyPosList[i][1]
#       dist = getDistance(archerYPos, curX, curY, tempN)
#       if dist < minDist:
#         minDist = dist
#         minDistEnemyPosSet.add(i)

#     # 공격 대상 적들을 삭제
#     print("minDistEnemyPos 집합:",minDistEnemyPosSet)
#     minDistEnemyPosList = list(minDistEnemyPosSet)
#     for i in range(len(minDistEnemyPosList)):
#       delEnemyPos = minDistEnemyPosList[i]
#       print("삭제 전 enemyPosList:",enemyPosList, "delEnemyPos",delEnemyPos)
#       print(str()+str(delEnemyPos)+"번째 적 삭제")
#       del enemyPosList[delEnemyPos]
#       deletedCnt += 1
#       print("삭제 후enemyPosList:",enemyPosList)

#     # 모든 적 아래로 한칸 이동 == 성 위치 N을 -1하는걸로 대체
#     tempN -= 1
#   print("삭제한 적의 수:",deletedCnt)
#   return deletedCnt

def getDistance(archerYPos, enemyX, enemyY, N):
  global D
  if N - enemyX > D:  # 적의 x좌표가 이미 D보다 크면 거리계산 안하고 False
    return 99
  dist = abs(N-enemyX)+abs(archerYPos-enemyY)
  if dist <= D:
    return dist
  else:
    return 99

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M, D = map(int, input().split())
enemyPosList = list()  #적의 x, y 좌표값의 리스트
archerYPos = list()  #궁수의 y좌표값 리스트 (x좌표값은 모든궁수 동일)
target = list()  # 타겟 적의 x, y 좌표값 리스트
tempN = N
for i in range(N):
  arr = list(map(int, input().split()))
  for j in range(M):
    if arr[j] == 1:
      enemyPosList.append((i, j))
print(enemyPosList)

enemyPosList.sort(key=lambda x: x[1])  # 가장 가까운 적이 여럿일 경우 가장 왼쪽에 있는 적 공격하기위해 y좌표가 작은 값이 앞에오도록 정렬
print(enemyPosList)
print("궁수조합")
tempArr = [i for i in range(N)]
archerYPosCombs = list(itertools.combinations(tempArr, 3))
result = 0
for archerYPosComb in archerYPosCombs:
  tempEnemyPosList = [row[:] for row in enemyPosList]
  tempN = N
  startGame(list(archerYPosComb), tempEnemyPosList)
print(result)