"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
6 3
2 3
4 5
5 6

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

sys.setrecursionlimit(10 ** 6)
def main():
    def dp(v):
        if done[v]: return memo[v]
        ans = 0
        for to in g[v]:
            ans = max(ans, dp(to) + 1)
        done[v] = True
        memo[v] = ans
        return ans

    memo = [0] * 1100000
    done = [False] * 110000
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        g[x].append(y)
    ans = 0
    for v in range(n):
        ans = max(ans, dp(v))
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
