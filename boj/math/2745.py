# 진법 변환
# 4:18~

# 공백없는 문자열 분리: 문자열을 그냥 리스트에 넣는다! list(string) 이렇게
# 아스키코드 활용(알파벳 문자 <-> 숫자) 문자->숫자는 ord('A')이렇게, 참고: ord('A') == 65

# inputs = input().split()
# n = inputs[0]
# n_str = list(n)
# b = int(inputs[1])
# result = 0

# for i in range(len(n_str), 0, -1):
#   if type(n_str[i-1]) != type(1):  # 각 자리수의 값이 숫자가 아닌 문자일 때
#     num = 10 + ord(n_str[i-1]) - ord('A')
#     result += num * (b**(i-1))
#   else:
#     print(int(n_str[i-1]))
#     result += int(n_str[i-1])
    
# print(result)

# inputs = input().split()
# n_str = list(inputs[0])
# n_str.reverse()
# print(n_str)
# num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# b = int(inputs[1])
# result = 0

# for i in range(len(n_str)-1, -1, -1):
#   result += num.index(n_str[i]) * (b**i)
    
# print(result)
# 틀렸습니다.... 왜 틀렸을까

n, b = input().split()
print(int(n, int(b)))