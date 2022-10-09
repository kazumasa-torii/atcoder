"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    A = 0
    B = 0
    C = 0
    for i in range(n):
        a, b, c = map(int, input().split())
        if i == 0:
            A += a
            B += b
            C += c
            continue
        ab = max(A, B)
        bc = max(C, B)
        ac = max(A, C)
        A = bc + a
        B = ac + b
        C = ab + c
    print(max(A, B, C))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
