"""
내 풀이
100,000 크기 만큼 배열을 만들고 X - 1, X + 1, 2 * X 에 대해 DFS 탐색을 하면서 각각 각 초를 기록한다.
"""
from collections import deque


# N, K = [int(n) for n in input().split(" ")]
N, K = 0, 100000

MAX_SEC = 100001
visited_list = [MAX_SEC] * MAX_SEC

def bfs(start, end):
    q = deque([start])
    idx = 0
    visited_list[start] = 0

    while q:
        point = q.popleft()

        idx += 1

        if point + 1 < MAX_SEC:
            if visited_list[point + 1] == MAX_SEC:
                q.append(point + 1)
                visited_list[point + 1] = min(visited_list[point + 1], visited_list[point] + 1)

        if 0 <= point - 1:
            if visited_list[point - 1] == MAX_SEC:
                q.append(point - 1)
                visited_list[point - 1] = min(visited_list[point - 1], visited_list[point] + 1)

        if 0 <= 2 * point < MAX_SEC:
            if visited_list[2 * point] == MAX_SEC:
                q.append(point * 2)
                visited_list[point * 2] = min(visited_list[point * 2], visited_list[point] + 1)

    return visited_list[end]

print(bfs(N, K))
