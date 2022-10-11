import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
2 11

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)


def main():
    a, b = map(int, input().split())
    max_si = 6*a
    min_si = 1*a
    print('Yes' if max_si >= b >= min_si else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
