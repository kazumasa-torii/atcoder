"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
1 7

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    if n == 1 and m == 1: exit(print(1))
    elif n == 1: exit(print(m-2))
    n -= 2
    m -= 2
    print(n*m)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')