import heapq
import sys
input = sys.stdin.readline

n = int(input())
t = sorted([list(map(int, input().split())) for _ in range(n)])

table = []
heapq.heappush(table, t[0][1])

for i in range(1, n):
    if t[i][0] >= table[0]:
        heapq.heappop(table)
    
    heapq.heappush(table, t[i][1])

print(len(table))