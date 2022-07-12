import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
100 10 100 180 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N, M, X, T, D = map(int, input().split())
    print(T if X < M else T - (D * (X-M)))

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
