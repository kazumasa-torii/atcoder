"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5
5 5 5 5 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    mod = 998244353

    res = 0
    for i in range(1,n+1):
        dp = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
        dp[0][0][0] = 1
        for j in range(n):
            for k in range(i+1):
                for l in range(i):
                    dp[j+1][k][l] += dp[j][k][l]
                    dp[j+1][k][l] %= mod
                    if k != i:
                        dp[j+1][k+1][(l+a[j])%i] += dp[j][k][l]
                        dp[j+1][k+1][(l+a[j])%i] %= mod
        res += dp[n][i][0]
        res %= mod
    print(res)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
