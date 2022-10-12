"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
100 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    print(((1900*m) + (100*(n-m))) * (2 ** m))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
