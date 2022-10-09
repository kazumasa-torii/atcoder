"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
chchokudai

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    mod = 10 ** 9 + 7
    s = input().strip()
    n = len(s)
    t = 'chokudai'
    dp = [[0] * 9 for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(n):
        for j in range(8):
            dp[i+1][j+1] = dp[i][j+1]
            if s[i] == t[j]:
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= mod
    print(dp[n][8])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
"""
chokudai
"""
