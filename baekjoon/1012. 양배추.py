# 맞은 코드
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(M, N, map, x, y):
    q = deque([(x, y)])
    map[y][x] = 0

    while q:
        x, y = q.popleft()

        for _dx, _dy in zip(dx, dy):
            nx, ny = x + _dx, y + _dy

            if 0 <= nx < M and 0 <= ny < N:
                if map[ny][nx] == 1:
                    q.append((nx, ny))

                    # 탐색할 때 map 값을 0으로 바꿔준다면, dx, dy for 문에서 총 4번을 모두 검사해야하기 때문에
                    map[ny][nx] = 0

    return True


T = int(input())
for _ in range(T):
    count = 0

    M, N, K = [int(n) for n in input().split(" ")]
    map = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = [int(n) for n in input().split(" ")]
        map[y][x] = 1

    for y in range(N):
        for x in range(M):
            if map[y][x] == 1:
                if bfs(M, N, map, x, y):
                    count += 1

    print(count)



# 시간 초과 코드
# from collections import deque
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def bfs(M, N, map, x, y):
#     q = deque([(x, y)])
#
#     while q:
#         x, y = q.popleft()
#         map[y][x] = 0
#
#         for _dx, _dy in zip(dx, dy):
#             nx, ny = x + _dx, y + _dy
#
#             if 0 <= nx < M and 0 <= ny < N:
#                 if map[ny][nx] == 1:
#                     q.append((nx, ny))
#
#     return True
#
#
# T = int(input())
# for _ in range(T):
#     count = 0
#
#     M, N, K = [int(n) for n in input().split(" ")]
#     map = [[0] * M for _ in range(N)]
#
#     for _ in range(K):
#         x, y = [int(n) for n in input().split(" ")]
#         map[y][x] = 1
#
#     for y in range(N):
#         for x in range(M):
#             if map[y][x] == 1:
#                 if bfs(M, N, map, x, y):
#                     count += 1
#
#     print(count)
