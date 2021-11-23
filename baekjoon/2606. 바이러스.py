from collections import deque

computer_num = int(input())
edge_num = int(input())
graph = [[0] * (computer_num + 1) for _ in range(computer_num + 1)]

for _ in range(edge_num):
    start, end = [int(n) for n in input().split()]
    graph[start][end] = graph[end][start] = 1

def bfs(N, graph, V):
    path = [V]
    visited = [False] * (N + 1)
    q = deque([V])
    visited[V] = True

    while q:
        v = q.popleft()

        for i in range(N + 1):
            if graph[v][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True
                path.append(i)

    return len(path) - 1

print(bfs(computer_num, graph, 1))