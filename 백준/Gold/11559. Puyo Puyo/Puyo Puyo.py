from collections import deque
import sys
input = sys.stdin.readline

moving = [[-1, 0], [0, 1], [1, 0], [0, -1]]

graph = [list(input().rstrip()) for _ in range(12)]
ans = 0


def bfs(a, b, color):
    block = [[a, b]]
    cnt = 0

    q = deque([[a, b]])

    while q:
        cnt += 1
        x, y = q.popleft()

        for dx, dy in moving:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < 12 and 0 <= ny < 6:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    q.append([nx, ny])
                    block.append([nx, ny])
                    visited[nx][ny] = True

    if cnt >= 4:
        return block
    else:
        return []


def down():
    for j in range(6):
        for i in range(10, -1, -1):
            for k in range(11, i, -1):
                if graph[i][j] != "." and graph[k][j] == ".":
                    graph[k][j] = graph[i][j]
                    graph[i][j] = "."
                    break


def clean(block):
    for i, j in block:
        graph[i][j] = '.'


while 1:
    flag = False
    visited = [[False] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                block = bfs(i, j, graph[i][j])

                if block:
                    clean(block)
                    flag = True

    if not flag:
        break

    ans += 1
    down()

print(ans)