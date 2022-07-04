"""
割りと単純な問題
結果の最適解が進んでいくだけなので貪欲法で進めていくのが良い
"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
10 1000000000
3 3
1 6
4 7
1 8
5 7
9 9
2 4
6 4
5 1
3 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N, X = map(int, input().split())
    tmp = 0
    ret = float('inf')
    MIN = float('inf')
    for i in range(1, N+1):
        x, y = map(int, input().split())
        tmp += x + y
        MIN = min(MIN, y)
        ret = min(ret, tmp + (X - i) * MIN)
    print(ret)

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
