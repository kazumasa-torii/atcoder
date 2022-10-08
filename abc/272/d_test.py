"""
pow(i-k, 2) + pow(j - l, 2)
"""
import re
import sys
import time
from io import StringIO
from typing import List

sys.setrecursionlimit(10**6)

_INPUT = """\
10 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
def main():
    def bfs():
        q = deque()
        si, sj = 0, 0
        q.append((si, sj, 0))
        A[si][sj] = 0
        while q:
            i, j, d = q.popleft()
            for x, y in dist_xy:
                ni = i + x
                nj = j + y
                if 0 <= ni <= n-1 and 0 <= nj <= n-1 and A[ni][nj] == -1:
                    A[ni][nj] = d + 1
                    q.append((ni, nj, d+1))
    n, m = map(int, input().split())
    A = [[-1] * n for _ in range(n)]
    dist_xy = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (i-1)**2 + (j-1)**2 == m:
                x = i - 1
                y = j - 1
                dist_xy.append((x, y))
                dist_xy.append((x, -y))
                dist_xy.append((-x, y))
                dist_xy.append((-x, -y))
    dist_xy = list(set(dist_xy))
    bfs()
    for a in A:
        print(*a)
if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')