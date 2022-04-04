# 파이썬의 기본 input() 함수는 동작속도가 느려서 시간 초과 오답판정을 받을수도 있다.
# 입력받아야 할 변수가 많은경우 입력만 받다가 시간이 끝나기 때문에 다른언어들 처럼 기존 인풋함수 말고 다른걸 써야한다.
# sys라이브러리를 쓰면 해결된다. -> sys.stdin.readline()

import sys

# input = sys.stdin.readline
# 활용할 때는 input()쓰던것처럼 그대로 쓰면 됨! input() 자리에 sys.stdin.readline()을 써준다고 생각하자!

input = sys.stdin.readline

n, m = map(int, input().split())
print(n)
print(m)

# 문자열 n줄을 입력받아 리스트에 저장할 때에는 .strip()을 붙여주자
# strip()은 문자열 맨 앞과 맨 끝의 공백문자를 제거한다.
# strip()을 붙여주는 이유: readline() 을 쓰면 끝에 엔터까지도 받아들이는 문자에 포함이 되버린다 그렇기 때문에 떼준다. 
# 만약 strip() 이 없으면 print() 할때 엔터 두번 됨!

k = int(input())  # 몇 줄 입력받을건지 입력
data = [input().strip() for i in range(k)]  # 한 줄 입력받을때마다 앞뒤 공백문자와 맨뒤 개행문자 제거
print(data)


# 아래와 같이 입력하면
# 3
# 안녕하세요 여러분
# 반가워요
# 따뜻한 녹차라떼 먹고싶어요
# 아래처럼 출력됨
# ['안녕하세요 여러분', '반가워요', '따뜻한 녹차라떼 먹고싶어요']