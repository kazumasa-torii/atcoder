"""
因数分解する
条件式を因数分解して計算し易い状態に持っていく
また答えを因数分解することも大事なので両方できるようにする
"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
7
19 23 51 59 91 99
15 45 56 65 69 94
7 11 16 34 59 95
27 30 40 43 83 85
19 23 25 27 45 99
27 48 52 53 60 81
21 36 49 72 82 84

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    ans = 1
    mod = 10 ** 9 + 7
    for i in range(n):
        ans *= (a[i][0] + a[i][1] + a[i][2] + a[i][3] + a[i][4] + a[i][5])
        ans %= mod
    print(ans)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
