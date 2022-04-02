# 최대공약수 = gcd = greatest common divisor
# 최소공배수 = lcm = least common multiple

# 유클리드 호제법: 두 정수 a와 b(a > b)가 있을 때, a = bq + r (0 <= r < b)라 하면,
# gcd(a, b) = gcd(b, r)이 된다. (a와 b의 최대공약수 = b와 a % b의 최대공약수)
# 만약 r이 0 이면, a, b의 최대공약수는 b (식으로 표현하면 a % b = 0 이면 gcd(a, b) = b)
# a, b의 최소 공배수는 a * b를 a, b의 최대공약수로 나눈 몫이다.
# 식으로 표현하면 lcm(a, b) = a * b // gcd(a, b)

# 5618번, 2609번

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def lcm(a, b):
  return a * b // gcd(a, b)