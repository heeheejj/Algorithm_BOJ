n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
result = 0
for i in range(n):
  count += 1
  if count >= a[i]:
    result += 1
    count = 0
print(result)