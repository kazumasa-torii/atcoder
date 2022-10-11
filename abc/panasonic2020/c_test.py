"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
2 3 9

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, c = map(int, input().split())
    d = c - a - b
    if d > 0 and d * d > 4 * a * b: print('Yes')
    else: print('No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
