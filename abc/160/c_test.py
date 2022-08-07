"""
一番長い辺を使わずに合計を調べる
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
20 3
0 5 15

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))

    acc = []
    for i in range(n):
        if i == n-1:
            acc.append(a[0] + abs(k - a[i]))
            continue
        acc.append(abs(a[i] - a[i+1]))
    acc.sort()
    print(sum(acc[:-1]))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
