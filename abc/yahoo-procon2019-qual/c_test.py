"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
314159265 35897932 384626433

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, a, b = map(int, input().split())
    if b-a <= 2: exit(print(n+1))
    n -= a
    n += 1
    ans = a
    ans += (b-a) * (n // 2)
    if n % 2 != 0: ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')