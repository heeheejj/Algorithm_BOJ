# 진법 변환
# 4:18~

# 공백없는 문자열 분리: 문자열을 그냥 리스트에 넣는다! list(string) 이렇게
# 아스키코드 활용(알파벳 문자 <-> 숫자) 문자->숫자는 ord('A')이렇게, 참고: ord('A') == 65

n, b = input().split()
b = int(b)

result = 0
for i in range(len(n)):
  if ord(n[i]) >= 65:
    result += (ord(n[i]) - 65 + 10) * b**(len(n) - 1 - i)
  else:
    result += int(n[i])*b**(len(n) - 1 - i)
print(result)

# 라이브러리 써서 쉽게 풀기 - 위 코드보다 24ms 정도 느림
# n, b = input().split()
# print(int(n, int(b)))