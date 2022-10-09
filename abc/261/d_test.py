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
6 3
2 7 1 8 2 8
2 10
3 1
5 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    limit = n+1
    x = list(map(int, input().split()))
    b = [0 for i in range(limit)]
    for i in range(m):
        c, y = map(int, input().split())
        b[c] = y

    INF = int(1e18)
    dp = [[-INF] * (limit) for _ in range(limit)]
    dp[0][0] = 0
    mx = 0

    for i in range(1, limit):
        dp[i][0] = mx
        mx = 0
        for j in range(1, limit):
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + x[i-1] + b[j])
            mx = max(dp[i][j], mx)
    print(max(dp[-1]))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
