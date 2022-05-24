# 2×n 타일링 2
# 이코테 8-4: 바닥공사와 같은 문제

n = int(input())
d = [1, 1] + [0]*999

for i in range(2, n+1):
    d[i] = (d[i-2]*2 + d[i-1]) % 10007
  
print(d[n])