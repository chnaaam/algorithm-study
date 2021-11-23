from collections import deque, defaultdict


N, M = [int(n) for n in input().split(" ")]
inputs = []
for _ in range(M):
    a, b = [int(n) for n in input().split(" ")]
    inputs.append((a, b))

graph = defaultdict(list)

visited = [False] * (N + 1)

graph[0] = []
for s, e in inputs:
    graph[s].append(e)
    graph[e].append(s)

def bfs(v):
    q = deque([v])
    visited[v] = True

    while q:
        v = q.popleft()

        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True

    return True

answer = 0
for n in range(1, N + 1):
    if not visited[n]:
        bfs(n)
        answer += 1

print(answer)
