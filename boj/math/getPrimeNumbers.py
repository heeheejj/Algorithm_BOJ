# 에라토스테네스의 체: n보다 작거나 같은 모든 소수를 찾는 알고리즘
# 범위 안에서 존재하는 모든 소수를 찾아야 하는 경우 사용

# 에라토스테네스의 체는 가장 먼저 소수를 판별할 범위만큼 리스트를 초기화하여, 해당하는 값을 넣어주고, 이후에 하나씩 지워나가는 방법을 이용한다.
# 1. 리스트를 생성하여 초기화한다.
# 2. 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지운다.(지울 때 자기자신은 지우지 않고, 이미 지워진 수는 건너뛴다.)
# 3. 2부터 시작하여 남아있는 수를 모두 출력한다.


def getPrimeNumbers(n):  # n 이하의 모든 소수를 리스트로 반환
  primes = list()  # 소수를 따로 저장할 리스트
  sieve = [True] * (n+1)
  
  for i in range(2, n + 1):
    if sieve[i] != False:
      primes.append(i)
    for j in range(i * 2, n + 1, i):
        sieve[j] = False
  return primes

n = int(input()) 

print(getPrimeNumbers(n))









# getPrimeNumbers()의 주석추가 version
def getPrimeNumbers_descriptions(n):  # 위 코드 설명!
  primes = list()  # 소수를 따로 저장할 리스트
  sieve = [True] * (n+1)
  
  for i in range(2, n + 1):
    if sieve[i] != False:  # sieve[i] == True면 소수리스트에 추가, sieve[i]가 True라면 이미 i는 2부터 (i-1)까지의 수들의 배수가 아닌 수이므로 그 수는 소수이다. i의 배수들은 이제 True에서 False로 바뀌고, 그 다음 True인 수는 무조건 소수일 것이다.. 이렇게 이해하면 되나
      primes.append(i)
    for j in range(i * 2, n + 1, i):  # i의 배수들을 False로 바꿔주는데, i는 소수니까 True를 유지해야하므로 i * 2부터 False로 바꿔줌.. 근데 사실 True/False 여부로 소수를 확인하는 것이 아니라 primes라는 리스트에 따로 저장해주므로 i라고 해도 상관없다.(i도 False로 바꿔줘도 상관 없다)
        sieve[j] = False
  return primes

sieve_description = [True] * (n+1)   # 체를 영어로 sieve라 한다! 
# sieve = [False, False] + ([True] * (n - 1))
# # 모든 원소를 True로 일단 초기화해두고, 지우면 False로 바꾼다.
# # 0, 1은 소수는 아니지만 True로 두어도 ㄱㅊ...
# # 어차피 for문에서 2부터 체크하고, 접근할 일이 없기 때문!
