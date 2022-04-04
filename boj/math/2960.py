# 에라토스테네스의 체
# N보다 작거나 같은 모든 소수를 찾는 알고리즘
# 1. 2부터 N까지 모든 정수를 적는다.
# 2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# 3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
# 4:59~

n, k = map(int, input().split())

sieve = [True] * (n+1)  # 체를 영어로 sieve라 한다! 
# 모든 원소를 True로 일단 초기화해두고, 지우면 False로 바꾼다.
# 이 문제에서 0, 1은 소수는 아니지만 True로 두어도 ㄱㅊ...
# 어차피 for문에서 2부터 체크하고, 접근할 일이 없기 때문!

count = 0
for i in range(2, n+1):
  if sieve[i] != False:
    for j in range(i, n+1, i):  # i부터 n+1까지 step을 i로 해서 반복
      if sieve[j] != False:
        sieve[j] = False
        count += 1
        if count == k:
          print(j)