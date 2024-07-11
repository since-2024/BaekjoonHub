from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    dic[input().rstrip()] += 1

ans = dict(sorted(dic.items()))

print(max(ans, key=lambda x: dic[x]))