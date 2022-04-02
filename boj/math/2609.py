# 최대공약수와 최소공배수

n, m = map(int, input().split())

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def lcm(a, b):
  return a * b // gcd(a, b)

print(gcd(n, m))
print(lcm(n, m))