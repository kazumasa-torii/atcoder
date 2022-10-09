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
3 4 2
1 7 7 9
9 6 3 7
7 8 6 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    INF = 10 ** 10
    ans = INF
    for _ in range(2):
        dp = [[INF] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if i > 0: dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j > 0: dp[i][j] = min(dp[i][j], dp[i][j-1])
                ans = min(ans, a[i][j] + c * (i+j) + dp[i][j])
                dp[i][j] = min(dp[i][j], a[i][j] - c*(i+j))
        a.reverse()
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
