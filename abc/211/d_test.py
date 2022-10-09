"""

"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
4 5
2 4
1 2
2 3
1 3
3 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
import sys
from collections import deque
input = sys.stdin.readline

def main():
    INF = 100100010
    mod = 10 ** 9 + 7
    n, m = map(int, input().split())
    maps = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        maps[a].append(b)
        maps[b].append(a)
    dist = [INF] * n
    q = deque()
    q.append(0)
    dist[0] = 0
    vs = []

    while q:
        v = q.popleft()
        vs.append(v)
        for u in maps[v]:
            if dist[u] != INF: continue
            dist[u] = dist[v] + 1
            q.append(u)
    dp = [0] * n
    dp[0] = 1
    for v in vs:
        for u in maps[v]:
            if dist[u] == dist[v] + 1:
                dp[u] += dp[v]
                dp[v] %= mod
    print(dp[n-1])
    return

if __name__ == '__main__':
    main()

    print(f'[Sec] {str(time.time() - StartTime)}')
