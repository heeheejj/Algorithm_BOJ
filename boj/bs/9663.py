# N-Queen
# 1차원 리스트에서 인덱스 번호를 행으로, 인덱스 값을 열로 지정해 사용: row[i] = j
# 같은 줄에는 두 개의 퀸이 있을 수 없으므로, 결국 한 줄에는 무조건 하나의 퀸만 존재할 수 있다.
# 퀸을 놓을 수 없는 칸을 체크할 때, 8개의 모든 방향에 대해서 체크할 필요 없이
# 아래쪽, 왼쪽 아래 대각선, 오른쪽 아래 대각선의 3 방향만 체크해주면 된다.
# 오른쪽, 왼쪽 가로방향을 체크해주지 않는 이유는 어차피 한 줄에 하나의 퀸만 들어가도록 코드를 작성하였기 때문
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())

def check(x):
    # 왼쪽 방향으로는 체크할 필요 x, 윗 방향과 왼쪽 대각선 방향만 체크하면 된
    for i in range(x):
        if row[i] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def dfs(depth):
    if depth == N:
        global result
        result += 1
        return

    for j in range(N):
        row[depth] = j
        if check(depth):
            dfs(depth + 1)

row = [0 for _ in range(N)]
result = 0
dfs(0)
print(result)