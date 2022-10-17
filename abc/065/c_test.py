"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
100000 100000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

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
    print(f'[Sec] {str(time.time() - StartTime)}')
