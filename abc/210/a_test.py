import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
5 3 20 15

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, a, x, y = map(int, input().split())
    low = n-a
    if low > 0:
        print((low * y) + (a * x))
    else:
        print(n*x)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
