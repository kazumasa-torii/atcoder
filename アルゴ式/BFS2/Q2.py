import sys
import time
from io import StringIO

_INPUT = """\
6 7
0 1
0 5
1 3
1 5
2 3
3 4
4 5

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

    dist = [-1] * n
    dist[0] = 0
    while q:
        v = q.popleft()
        for next_v in g[v]:
            if dist[next_v] != -1: continue
            dist[next_v] = dist[v] + 1
            q.append(next_v)
    print(max(dist))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
