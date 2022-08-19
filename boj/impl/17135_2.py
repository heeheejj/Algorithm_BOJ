# 캐슬 디펜스

import sys, itertools

def getDeletedEnemyCnt(enemyPosList, N):
  enemyCnt = len(enemyPosList)
  deletedCnt = 0
  print("enemyPosList: ",enemyPosList)
  tempN = N
  lastEnemyPos = min(enemyPosList)  #가장 멀리있는 적의 x, y좌표
  lastEnemyX = lastEnemyPos[0]
  while lastEnemyX < tempN:  # 모든 적이 격자판에서 삭제될때까지 반복
    minDist = 99
    minDistEnemyPosSet = set()
    for i in range(len(enemyPosList)):  # 공격 대상 적을 찾기
      curX, curY =  enemyPosList[i][0], enemyPosList[i][1]
      dist = getDistance(archerYPos, curX, curY, tempN)
      if dist < minDist:
        minDist = dist
        minDistEnemyPosSet.add(i)

    # 공격 대상 적들을 삭제
    print("minDistEnemyPos 집합:",minDistEnemyPosSet)
    minDistEnemyPosList = list(minDistEnemyPosSet)
    for i in range(len(minDistEnemyPosList)):
      delEnemyPos = minDistEnemyPosList[i]
      print("삭제 전 enemyPosList:",enemyPosList, "delEnemyPos",delEnemyPos)
      print(str()+str(delEnemyPos)+"번째 적 삭제")
      del enemyPosList[delEnemyPos]
      deletedCnt += 1
      print("삭제 후enemyPosList:",enemyPosList)

    # 모든 적 아래로 한칸 이동 == 성 위치 N을 -1하는걸로 대체
    tempN -= 1
  print("삭제한 적의 수:",deletedCnt)
  return deletedCnt

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
for i in range(N):
  arr = list(map(int, input().split()))
  for j in range(M):
    if arr[j] == 1:
      enemyPosList.append((i, j))
print(enemyPosList)
# lastEnemyPos = min(enemyPosList)  #가장 멀리있는 적의 x, y좌표
# lastEnemyX = lastEnemyPos[0]
# print(lastEnemyX)

print("궁수조합")
tempArr = [i for i in range(N)]
archerYPosCombs = list(itertools.combinations(tempArr, 3))
result = 0
for archerYPosComb in archerYPosCombs:
  # 공격하기: 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적
  # 가장 가까운 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다.
  # 같은 적이 여러 궁수에게 공격당할 수 있다.
  print("=========================궁수 조합:",archerYPosComb)
  deletedCnt = 0
  for archerYPos in archerYPosComb:  #  궁수 위치 선정
    tempEnemyPosList = [row[:] for row in enemyPosList]
    print("궁수 y좌표"+str(archerYPos))
    deletedCnt += getDeletedEnemyCnt(tempEnemyPosList, N)
    print("삭제한 적의 수:",deletedCnt)
    if result < deletedCnt:
      result = deletedCnt
print(result)
    
    
#   print()

# pr# int("궁수조합")
# tempArr = [i for i in range(N)]
# archerYPosCombs = list(itertools.combinations(tempArr, 3))
# for archerYPosComb in archerYPosCombs:
#   for archerYPos in archerYPosComb:
#     print(archerYPos, end=' ')
#     while True:
#       # 공격하기
#       if isEnemyInRange(archerYPos, )
#       lastEnemyPos = min(enemyPosList)  #가장 멀리있는 적의 x, y좌표
#       lastEnemyX = lastEnemyPos[0]
#     if lastEnemyX == N:
#       break
#   print()