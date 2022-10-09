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
20
7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    N = int(input())
    A = list(map(int, input().split()))
    li = defaultdict(int)
    idx = 0
    ans = 0
    for i in A:
        idx += 1
        li[i] += 1
        ans += idx - li[i]
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
