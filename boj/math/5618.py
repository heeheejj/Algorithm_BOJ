# 공약수
# 5:43~
# 유클리드 호제법: 두 정수 a와 b(a > b)가 있을 때, a = bq + r (0 <= r < b)라 하면,
# gcd(a, b) = gcd(b, r)이 된다. (a와 b의 최대공약수 = b와 a % b의 최대공약수)
# 만약 r이 0 이면, a, b의 최대공약수는 b (식으로 표현하면 a % b = 0 이면 gcd(a, b) = b)
# gcd: greatest common divisor

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
    
n = int(input())
inputs = list(map(int, input().split()))

gcd_value = gcd(inputs[0], gcd(inputs[1], inputs[-1]))  # 인덱스 -1는 리스트의 마지막을 의미

for i in range(1, gcd_value // 2 + 1):
  if gcd_value % i == 0:
    print(i, end='\n')
print(gcd_value)