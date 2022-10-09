"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
6 15
6 5
5 6
6 4
6 6
3 5
7 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, w = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1] * (w + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(w):
            if dp[i][j] == -1: continue
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j + li[i][0] <= w:
                dp[i+1][j+li[i][0]] = max(dp[i+1][j+li[i][0]], dp[i][j] + li[i][1])
    print(max(dp[-1]))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
