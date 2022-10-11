"""
(初項 + 末項) * 項数 // 2
を行うけど文字数をカウントする必要があるのでそこが工夫が必要

意味合いとしては
1～9 1
10～99 2
100～999 3
のように文字数を増やしていけるので
"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
98 100

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def cnt(a, b):
        if b < a: return 0
        return (a + b) * (b - a + 1) // 2
    L, R = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(1, 20):
        l, r = 10 ** (i-1), (10 ** i) - 1
        ans += i * cnt(max(l, L), min(r, R))
    print(ans % mod)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
