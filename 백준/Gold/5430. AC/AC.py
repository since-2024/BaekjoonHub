from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cmd = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))

    if n == 0:
        arr = deque()

    isFail = False
    cnt = 0

    for c in cmd:
        if c == 'R':
            cnt += 1
        elif c == 'D':
            if len(arr) != 0:
                if cnt % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                isFail = True
                break

    if isFail:
        print('error')
    else:
        if cnt % 2 == 1:
            arr.reverse()
        print(f"[{','.join(arr)}]")