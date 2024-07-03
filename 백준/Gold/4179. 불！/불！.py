from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())

q = deque()
graph = []
escape = []

for i in range(r):
    row = list(map(str, input().rstrip()))

    for j in range(c):
        if row[j] == 'F':
            q.append([i, j, False])
            row[j] = '#'
        elif row[j] == 'J':
            q.appendleft([i, j, True])
            row[j] = 0

    graph.append(row)

while q:
    x, y, jihoon = q.popleft()

    if jihoon and (x == 0 or x == r-1 or y == 0 or y == c-1) and graph[x][y] != '#':
        escape.append(graph[x][y] + 1)
        break

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] != '#' and not jihoon:
                graph[nx][ny] = '#'
                q.append([nx, ny, False])
            elif graph[nx][ny] == '.' and graph[x][y] != '#' and jihoon:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny, True])

if escape:
    print(escape[0])
else:
    print('IMPOSSIBLE')