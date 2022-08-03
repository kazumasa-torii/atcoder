"""
多くないので全探索する
四角の中身が一斉に切り替わるので最終的に
左上から見ていき一番右行と一番下の列は見なくても確定する

これがB==AならばOK
"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
5 5
6 17 18 29 22
39 50 25 39 25
34 34 8 25 17
28 48 25 47 42
27 47 24 32 28
4 6 3 29 28
48 50 21 48 29
44 44 19 47 28
4 49 46 29 28
4 49 45 1 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    h, w = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(h)]
    B = [list(map(int, input().split())) for _ in range(h)]
    ans = 0

    for i in range(h-1):
        for j in range(w-1):
            diff = B[i][j] - A[i][j]
            ans += abs(diff)
            A[i][j] += diff
            A[i+1][j] += diff
            A[i][j+1] += diff
            A[i+1][j+1] += diff
    if A == B:
        print('Yes')
        print(ans)
    else:
        print('No')
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
