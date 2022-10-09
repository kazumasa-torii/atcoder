"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
10 4
-3 1 -4 1 -5 9 -2 6 -5 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    acc = [0]
    for i in range(n): acc.append(acc[-1]+a[i])
    now = 0
    si = []
    for i in range(m): now += a[i]*(i+1)
    si.append(now)
    for i in range(n-m):
        si.append(si[-1] - ((acc[i+m] - acc[i] )- (a[i+m] * m)))
    print(max(si))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
