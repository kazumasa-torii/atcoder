"""
一旦条件を整理してから対処を変更
"""

import sys
input = sys.stdin.readline
from math import factorial
def main():
    mod = 10**9 + 7
    n, m = map(int, input().split())
    if abs(n-m) >= 2:exit(print(0))
    ans = factorial(n) * factorial(m)
    ans %= mod
    if n == m:
        ans *= 2
    print(ans%mod)
    return

if __name__ == '__main__':
    main()