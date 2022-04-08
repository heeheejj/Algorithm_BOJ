# 이 구역의 승자는 누구야?

nums = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1 ,1, 2, 2, 2, 1]

str = input()

sum = 0
for alph in str:
  sum += nums[ord(alph) - ord('A')]
  sum %= 10

if sum % 2 != 0:
  print("I'm a winner!")
else:
  print("You're the winner?")