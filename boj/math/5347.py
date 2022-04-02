# LCM
def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def lcm(a, b):
  return a * b // gcd(a, b)

n = int(input())
results = list()
for i in range(n):
  a, b = map(int, input().split())
  results.append(lcm(a, b))
for i in results:
  print(i)