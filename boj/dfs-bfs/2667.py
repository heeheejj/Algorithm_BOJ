# 단지번호붙이기 - 이코테 5-3.음료수 얼려먹기 문제와 유사
import sys

input = sys.stdin.readline
n = int(input())
_map = [list(map(int, input().rstrip())) for _ in range(n)]


def dfs(x, y):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        # print("범위 밖:",x,",",y)
        return False

    if _map[x][y] == 1:  # 방문하지 않은 집이라면
        # print("x:",x, " y:", y)
        _map[x][y] = 0  # 방문 처리
        global house_count
        house_count += 1

        # print("dfs1: x:",x - 1, ",",y)
        dfs(x - 1, y)
        # print("dfs2: x:", x, ",", y - 1)
        dfs(x, y - 1)
        # print("dfs3: x:", x + 1, ",", y)
        dfs(x + 1, y)
        # print("dfs4: x:", x, ",", y + 1)
        dfs(x, y + 1)
        return True
    # print("이미 방문:",x,',',y)
    return False  # 이미 방문한 집이면 dfs 호출할 필요 X, house_count에도 포함 X, False 리턴


total_count = 0
house_counts = list()
for i in range(n):
    for j in range(n):
        house_count = 0
        # print("i:",i," j:", j)
        if dfs(i, j) == True:
            total_count += 1
            house_counts.append(house_count)

print(total_count)
for cnt in sorted(house_counts):
    print(cnt)