import heapq
import sys
input = sys.stdin.readline

min_q = []
max_q = []

n = int(input())

for i in range(n):
    # num = int(input())
    if i%2 == 0:
        heapq.heappush(max_q, -int(input()))
    else:
        heapq.heappush(min_q, int(input()))

    if min_q and max_q and min_q[0] < -max_q[0]:
        sml_n = heapq.heappop(min_q)
        big_n = -heapq.heappop(max_q)

        heapq.heappush(min_q, big_n)
        heapq.heappush(max_q, -sml_n)

    print(-max_q[0])