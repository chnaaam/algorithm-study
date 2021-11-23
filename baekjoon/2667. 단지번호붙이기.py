from collections import deque

M = int(input())

graph = []
for i in range(M):
    graph.append([int(c) for c in input()])

# M = 7
# graph = [
#     "0110100",
#     "0110101",
#     "1110101",
#     "0000111",
#     "0100000",
#     "0111110",
#     "0111000",
# ]
#
# for i in range(len(graph)):
#     graph[i] = [int(c) for c in graph[i]]

answer = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(N, graph, i, j):
    q = deque([(i, j)])
    count = 0

    while q:
        i, j = q.popleft()

        if graph[i][j] == 1:
            count += 1
            graph[i][j] = 0

            for _dx, _dy in zip(dx, dy):
                ni, nj = i + _dx, j + _dy

                if ni < 0 or ni >= N or nj < 0 or nj >= N:
                    continue

                if graph[ni][nj] != 0:
                    q.append((ni, nj))

    return count

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] != 0:
            answer.append(bfs(M, graph, i, j))

print(len(answer))
for a in sorted(answer):
    print(a)

