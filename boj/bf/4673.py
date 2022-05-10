# 셀프 넘버

nums = set(range(1, 10001))
generated_nums = set()
def d(n):
  return n + sum(map(int, str(n)))

for num in range(1, 10001):
  generated_nums.add(d(num))  # d(n)으로 생성된 수 = 생성자가 있는 수!

self_nums = nums - generated_nums

for num in sorted(self_nums):
  print(num)