import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
0 3 1 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, c, d = map(int, input().split())
    l = max(a, c)
    r = min(b, d)
    print(r-l)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
