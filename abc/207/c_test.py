"""

"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
3
1 1 2
2 2 3
3 2 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N = int(input())
    I = []
    L = []
    R = []
    for i in range(N):
        t, l, r = map(int, input().split())
        l *= 2
        r *= 2
        if t%2 == 0:
            r -= 1
        if t >= 3:
            l += 1
        L.append(l)
        R.append(r)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] > R[j]: continue
            if L[j] > R[i]: continue
            ans += 1
    print(ans)

    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
