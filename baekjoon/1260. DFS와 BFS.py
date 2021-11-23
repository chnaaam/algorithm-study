"""
* 문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

* Input
4 5 1
1 2
1 3
1 4
2 4
3 4

* Output
1 2 4 3
1 2 3 4
"""

from collections import deque


def dfs(N, graph, v, visited, path):
    visited[v] = True
    path.append(v)

    for i in range(1, N + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(N, graph, i, visited, path)

    return path

def bfs(N, graph, v, visited):
    path = [v]
    q = deque([v])
    visited[v] = True

    while q:
        v = q.popleft()

        for i in range(1, N + 1):
            if not visited[i] and graph[v][i] == 1:
                q.append(i)
                path.append(i)
                visited[i] = True

    return path


N, M, V = [int(n) for n in input().split(" ")]
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    start, end = [int(n) for n in input().split()]
    graph[start][end] = graph[end][start] = 1


print(" ".join(map(str, dfs(N, graph, V, [False] * (N + 1), []))))
print(" ".join(map(str, bfs(N, graph, V, [False] * (N + 1)))))
