N = int(input())
map = [[0] * N for _ in range(N)]


def is_possible_location(queen, row):

    for col in range(row):
        # 세로 방향에서 겹치는 지 or 대각선 방향에서 겹치는 지
        if queen[col] == queen[row] or abs(queen[col] - queen[row]) == row - col:
            return False

    return True

def dfs(queen, N, row):
    count = 0

    # 종료 조건 - row가 맨 마지막까지 내려왔다는 것은 Queen을 놓을 수 있다는 것
    if row == N:
        return 1

    for c in range(N):
        queen[row] = c

        if is_possible_location(queen, row):
            count += dfs(queen, N, row + 1)

    return count

print(dfs([0] * N, N, 0))