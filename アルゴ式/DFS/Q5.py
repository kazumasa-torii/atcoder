import sys
import time
from io import StringIO

_INPUT = """\
4 6
1 2
0 1
3 0
2 3
1 3
2 0

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
    q.append(0)

    seen = [False] * n

    while q:
        v = q.popleft()
        if seen[v]:continue
        seen[v] = True
        for next_v in g[v]:
            q.append(next_v)

    print('Yes'if all(seen) else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
