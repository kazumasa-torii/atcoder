import sys
import time
from io import StringIO
from turtle import Turtle

_INPUT = """\
4 4
0 1
2 1
3 0
1 3

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

    dist = [-1] * n
    ans = [[] for _ in range(n)]

    dist[0] = 0
    ans[0].append(0)
    q = deque()
    q.append(0)

    while q:
        v = q.popleft()
        for next_v in g[v]:
            if dist[next_v] != -1: continue
            dist[next_v] = dist[v] + 1
            ans[dist[v]+1].append(next_v)
            q.append(next_v)

    for i in ans:
        i.sort()
        print(*i)

    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
