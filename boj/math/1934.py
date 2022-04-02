# 최소공배수

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def lcm(a, b):
  return a * b // gcd(a, b)

t = int(input())
tc = list()

for i in range(t):
  n, m = map(int, input().split())
  tc.append((n, m))
  
for i in range(t):
  print(lcm(tc[i][0], tc[i][1]))