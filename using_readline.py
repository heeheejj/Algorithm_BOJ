# 파이썬의 기본 input() 함수는 동작속도가 느려서 시간 초과 오답판정을 받을수도 있다.
# 입력받아야 할 변수가 많은경우 입력만 받다가 시간이 끝나기 때문에 다른언어들 처럼 기존 인풋함수 말고 다른걸 써야한다.
# sys라이브러리를 쓰면 해결된다. -> sys.stdin.readline().rstrip()

import sys

# data = sys.stdin.readline().rstrip()
# 활용할 때는 input()쓰던것처럼 그대로 쓰면 됨! input() 자리에 sys.stdin.readline().rstrip()을 써준다고 생각하자!
n, m = map(int, sys.stdin.readline().rstrip().split())
print(n)
print(m)

# rstrip()을 붙여주는 이유: readline() 을 쓰면 끝에 엔터까지도 받아들이는 문자에 포함이 되버린다 그렇기 때문에 떼준다.
# data = sys.stdin.readline()    # rstrip() 이 없으면 print() 할때 엔터 두번 됨