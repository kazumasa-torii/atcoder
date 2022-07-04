import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
8691 20

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N, K = map(int, input().split())
    for _ in range(K):
        if N % 200 == 0:
            N = int(N / 200)
        else:
            N = int(str(N) + '200')
    print(N)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
