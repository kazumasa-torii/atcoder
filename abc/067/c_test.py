"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
11
1 2 3 4 5 6 7 -10 1 7 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = int(1e19)
    sa = sum(a)
    ass = 0
    for i in range(n):
        ass += a[i]
        if i + 1 < n: ans = min(ans, abs(sa-(ass*2)))
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
