# 탑

n = int(input())

height = list(map(int, input().split()))
stack = list()  # 기둥의 번호 담는 스택

for i in range(n):
  h = height[i]
  while stack and height[stack[-1]] < h:  # stack의 마지막 원소를 인덱스값으로 하는 기둥의 높이가 현재 idx의 기둥의 높이보다 더 큰게 나올때까지(문제에서 서로 다른 높이 -> 같은 높이는 없음) stack에서 pop하면서 확인  
    stack.pop()
  if stack:
    print(stack[-1] + 1, end = ' ')
  else:
    print(0, end = ' ')
  stack.append(i)
print("")