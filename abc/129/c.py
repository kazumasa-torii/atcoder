import sys
from typing import List
input = sys.stdin.readline

def main():
    mod: int = 10 ** 9 + 7
    N, M = map(int, input().split())
    li: List[int] = [int(input()) for _ in range(M)]
    dp: List[int] = [-1] * (N+1)

    dp[0] = 1
    dp[1] = 1

    for i in li:
        dp[i] = 0

    for j in range(2, N+1):
        if dp[j] == -1:
            dp[j] = dp[j-1] + dp[j-2]
            dp[j] %= mod

    print(dp[N] % mod)
    return

main()
