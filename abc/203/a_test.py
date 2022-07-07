import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
4 5 6

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
