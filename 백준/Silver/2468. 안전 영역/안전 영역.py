from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(a, b, depth, visited):
    q = deque()
    q.append([a, b])
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > depth and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])


n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dep_max = max(max(x) for x in graph)
ans = []

for i in range(dep_max):
    visited = [[False] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and not visited[j][k]:
                bfs(j, k, i, visited)
                cnt += 1

    ans.append(cnt)

print(max(ans))