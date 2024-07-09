from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    v = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    w = [-1] + [0] * n
    dp = [-1] + v
    q = deque()

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        w[b] += 1

    win = int(input())

    for i in range(1, n + 1):
        if w[i] == 0:
            q.append(i)

    while q:
        idx = q.popleft()

        for i in graph[idx]:
            dp[i] = max(dp[i], dp[idx] + v[i - 1])

            if w[i] == 1:
                q.append(i)

            w[i] -= 1

    print(dp[win])