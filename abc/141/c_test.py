"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
10 13 15
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, k, q = map(int, input().split())
    ans = [int(input()) for _ in range(q)]
    syo = k - q
    p = [syo for _ in range(n)]
    for i in ans:
        p[i-1] += 1

    for i in p:
        if i >= 1: print('Yes')
        else: print('No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
