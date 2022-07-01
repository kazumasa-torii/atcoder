import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
2021 617

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N, K = map(int, input().split())
    mod = (10 ** 9) + 7
    if N == 1: print(K)
    else: print(K * (K-1) * pow(K-2, N-2, mod) % mod)

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
