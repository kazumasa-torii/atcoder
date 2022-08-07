"""
計算量が追いつかないパターン
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
10 -5 -3
9 -6 10 -1 2 10 -1 7 -15 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N,L,R=map(int,input().split())
    A=list(map(int,input().split()))

    ans = L * N

    for l in range(N+1):
        for r in range(l, N+1):
            tmp = l * L + (N - r) * R + sum(A[l:r])
            ans = min(ans, tmp)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
