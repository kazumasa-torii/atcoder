"""
計算量をどれだけ落とせるか
もとの内容を変えずに質問に答える内容を想像してそれに合わせて実装させる

abc
↓ 1つシフト
cab
このときは、abcの列を一番右から読み始めた内容と一緒なのでそう読み替える

知らなかったのは、-1を%NとかするとそれにするとあまりはNになるがそこから引き算してくれる
かしこい
"""
import sys
import time
from io import StringIO
from typing import List

from setuptools import sic
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
10 8
dsuccxulnl
2 4
2 7
1 2
2 7
1 1
1 2
1 3
2 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N, Q = map(int, input().split())
    S = list(input())
    shift = 0
    for _ in range(Q):
        x, y = map(int, input().split())
        if x == 1:
            shift -= y
            print(shift, N)
            shift %= N
            print(shift)
        if x == 2:
            print(S[(shift + y - 1) % N])

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
