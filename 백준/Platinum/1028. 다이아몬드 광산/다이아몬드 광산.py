import sys

input = sys.stdin.readline

r, c = map(int, input().split())

graph = [[0] * c]
lu = [[0] * c for _ in range(r + 1)]
ru = [[0] * c for _ in range(r + 1)]

for i in range(r):
    row = list(map(int, input().rstrip()))

    for j in range(c):
        if row[j] == 1:
            if j + 1 < c:
                lu[i+1][j] = lu[i][j+1] + 1
            else:
                lu[i+1][j] = 1

            if j - 1 >= 0:
                ru[i+1][j] = ru[i][j-1] + 1
            else:
                ru[i+1][j] = 1
            row[j] = min(lu[i+1][j], ru[i+1][j])

    graph.append(row)

l_max = max(max(x) for x in lu)
r_max = max(max(x) for x in ru)
max_cnt = min(l_max, r_max)


def check(i, j, ans):
    size = graph[i][j]
    ret = 0
    for k in range(ans, size+1):
        s = max(k-1, 0)
        if 0 <= j-s and j+s < c:
            if lu[i-s][j-s] >= k and ru[i-s][j+s] >= k:
                ret = k

    return ret


if l_max + r_max == 0:
    print(0)
else:
    ans = 1

    for i in range(r, 0, -1):
        for j in range(1, c-1):
            if graph[i][j] > ans:
                ans = max(ans, check(i, j, ans))

    print(ans)