import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input().rstrip().replace(' ', '')
    cnt = [0] * 26

    for i in s:
        cnt[ord(i) - 97] += 1

    m = max(cnt)
    if cnt.count(m) == 1:
        print(chr(cnt.index(m) + 97))
    else:
        print('?')