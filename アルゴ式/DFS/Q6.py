import sys
import time
from io import StringIO

_INPUT = """\
5 1
3 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    q = deque()
    seen = [False] * n
    cnt = 0

    for i in range(n):
        if seen[i]: continue
        q.append(i)
        cnt += 1
        while q:
            v = q.popleft()
            if seen[v]: continue
            seen[v] = True
            for next_v in g[v]:
                q.append(next_v)
    print(cnt)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
