# 회전 초밥
# 916ms
# 슬라이딩 윈도우
# 두번째 for문 range의 끝값을 N으로 잘못설정해서 아래 반례를 만족하지 못했다.
# 8 30 4 30
# 9
# 25
# 7
# 9
# 7
# 30
# 2
# 7
# 정답: 5
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = dict()
inputs = [int(input()) for _ in range(N)]
inputs = inputs + inputs
sushi[c] = 1    # 쿠폰초밥은 무조건 먹고 시작
# 처음 k개 setting
init = inputs[:k]
for x in init:
    if x not in sushi:
        sushi[x] = 1
    else:
        sushi[x] += 1

result = len(sushi)  # 가짓수의 최댓값 초기화

for i in range(k, k+N-1):
    sushi[inputs[i-k]] -= 1 # 이전 윈도우의 첫번째 원소 빼기
    if sushi[inputs[i-k]] == 0:
        del sushi[inputs[i-k]]
    pushX = inputs[i]
    if pushX not in sushi:
        sushi[pushX] = 1
    else:
        sushi[pushX] += 1

    result = max(result, len(sushi))
print(result)