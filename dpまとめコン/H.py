"""
遷移は逆順というのは思いついたが実装が出来なかった…。
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5 5
..#..
.....
#...#
.....
..#..

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    mod = 10 ** 9 + 7
    h, w = map(int, input().split())
    filid = [input() for i in range(h)]
    dp = [[0] * w for _ in range(h)]
    dp[h-1][w-1] = 1

    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if i == h-1 and j == w-1: continue
            if i+1 < h: dp[i][j] += dp[i+1][j]
            if j+1 < w: dp[i][j] += dp[i][j+1]
            dp[i][j] %= mod

            if filid[i][j] == '#': dp[i][j] = 0
    print(dp[0][0])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
