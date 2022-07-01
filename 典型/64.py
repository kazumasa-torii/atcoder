import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
20 10
61 51 92 -100 -89 -65 -89 -64 -74 7 87 -2 51 -39 -50 63 -23 36 74 37
2 2 -45
6 19 82
2 9 36
7 13 71
16 20 90
18 20 -24
14 17 -78
10 11 -55
7 19 -26
20 20 -7

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    # 長さが1ならば変化は無いので0を出力する
    if N == 1:
        for _ in range(Q):
            print(0)
        return

    # 差をlistで持っておき差の合計値も持っておく
    diffs = [A[i+1] - A[i] for i in range(len(A) - 1)]
    inconv = sum(abs(diff) for diff in diffs)

    for _ in range(Q):
        l, r, v = map(int, input().split())
        l -= 1
        r -= 1
        if l != 0:
            before = diffs[l-1]
            diffs[l-1] += v
            inconv += -abs(before) + abs(diffs[l-1])
        if r != N-1:
            before = diffs[r]
            diffs[r] -= v
            inconv += -abs(before) + abs(diffs[r])
        print(inconv)

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
