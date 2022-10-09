"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
7 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, k = map(int, input().split())
    if n % k == 0: exit(print(0))
    if n < k: exit(print(n))
    one = n - (n // k) * k
    two = abs(one - k)
    print(min(one, two))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
