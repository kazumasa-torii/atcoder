"""
漸化式を立てる
基本のDP
"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
6783 125

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, l = map(int, input().split())
    mod = 10 ** 9 + 7

    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        dp[i+1] += dp[i]
        dp[i+1] %= mod
        if i + l <= n:
            dp[i+l] += dp[i]
            dp[i+l] %= mod

    print(int(dp[-1]%mod))

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
