import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
10 2
1 3 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * (n+1) for _ in range(2)]
    for i in range(1, n+1):
        max_now = 0
        min_now = int(1e19)
        for k in a:
            if i - k < 0: continue
            max_now = max(max_now, dp[1][i-k] + k)
            min_now = min(min_now, dp[0][i-k])
        dp[0][i] = max_now
        dp[1][i] = min_now
    print(dp[0][-1])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
