"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
3
10
20
30

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        tmp = int(input())
        a.append(tmp)
        if tmp % 10 != 0: b.append(tmp)
    b.sort()
    sumA = sum(a)
    if sumA % 10 == 0:
        if not b: sumA = 0
        else: sumA -= b[0]
    print(sumA)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
