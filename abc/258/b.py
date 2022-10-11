"""
できるなら全探索
全探索できる場合はきちんと全探索を行う

まずは簡単な例から実装していき工夫していくことが大事
"""

import sys
import time
from io import StringIO
from typing import List



_INPUT = """\
4
1161
1119
7111
1811

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N = int(input())
    A = [list(map(int, list(input()))) for _ in range(N)]
    # 左上、上、右上、左、右、左下、下、右下
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1,  0,  1,-1, 1,-1, 0, 1]
    ans = 0
    for si in range(N):
        for sj in range(N):
            for v in range(8):
                i = si
                j = sj
                x = 0
                for _ in range(N):
                    x = x*10 + A[i][j]
                    i += di[v]
                    j += dj[v]
                    if i >= N:
                        i %= N
                    if j >= N:
                        j %= N
                ans = max(ans, x)
    print(ans)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
