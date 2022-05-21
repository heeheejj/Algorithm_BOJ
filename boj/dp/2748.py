# 피보나치 수 2 - 반복문 (bottom up) (재귀보다 빠름)
# 2747: 피보나치 수, 10826: 피보나치 수 4도 같은 코드 

d = list()
d.append(0)
d.append(1)
n = int(input())

for i in range(2, n + 1):
    d.append(d[i - 1] + d[i - 2])

print(d[n])