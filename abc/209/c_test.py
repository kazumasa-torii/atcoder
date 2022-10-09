"""

"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
2
1 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    mod = 10 ** 9 + 7
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    maina = 0
    for i in range(n):
        c[i] -= maina
        maina += 1
    ans = c[0]
    for i in range(1, n):
        ans *= c[i]
        ans %= mod
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
