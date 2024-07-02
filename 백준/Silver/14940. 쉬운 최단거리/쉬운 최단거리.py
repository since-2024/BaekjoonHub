from collections import deque
import sys
input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

ans = 0
graph = []
visited = [[False] * m for _ in range(n)]
q = deque()

for i in range(n):
  row = list(map(int, input().split()))
  graph.append(row)
  
  if 2 in row:
    idx = row.index(2)
    q.append([i, idx])
    graph[i][idx] = 0

while q:
  x, y = q.popleft()
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < m:
      if graph[nx][ny] != 0 and not visited[nx][ny]:
        q.append([nx, ny])
        visited[nx][ny] = True
        
        graph[nx][ny] += graph[x][y]

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and not visited[i][j]:
      graph[i][j] = -1

for i in graph:
  print(*i)