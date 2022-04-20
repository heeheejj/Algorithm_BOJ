# 2×n 타일링

n = int(input())

d = [0] * 1001  # [0] * (n + 1)로 하면 n = 1일 때 6행에서 존재하지 않는 인덱스에 값을 대입하는 오류가 남
d[1], d[2] = 1, 2
for i in range(3, n + 1):
  d[i] = (d[i - 1] + d[i - 2]) % 10007

print(d[n])