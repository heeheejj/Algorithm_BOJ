# 피보나치 수 5 - 반복(bottom up) - 재귀보다 더 빠름

d = [0] * 21
d[1], d[2] = 1, 1
n = int(input())

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])