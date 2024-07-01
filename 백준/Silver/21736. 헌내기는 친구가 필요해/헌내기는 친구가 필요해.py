from collections import deque
import sys
input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

ans = 0
graph = []
q = deque()

for i in range(n):
  row = list(input().rstrip())
  graph.append(row)
  
  if 'I' in row:
    idx = row.index('I')
    q.append([i, idx])
    graph[i][idx] = 'X'

while q:
  x, y = q.popleft()
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < m:
      if graph[nx][ny] != 'X':
        q.append([nx, ny])
        
        if graph[nx][ny] == 'P':
          ans += 1
  
        graph[nx][ny] = 'X'

if ans > 0:
  print(ans)
else:
  print('TT')