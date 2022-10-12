"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
8
WWWWWEEE

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    s = list(input())
    w = [0] * n
    e = [0] * n
    cnt = 0
    for i in range(n):
        if s[i] == 'W':
            cnt += 1
        w[i] = cnt
    cnt = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'E':
            cnt += 1
        e[i] = cnt
    ans = int(1e18)
    for i in range(n):
        tmp = 0
        if i != 0: tmp += w[i-1]
        if i < n-1: tmp += e[i+1]
        ans = min(ans, tmp)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
