"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
1 1
1000000000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from math import gcd
def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, x)
    gcdList = []
    for i in range(1, n+1):
        gcdList.append(abs(a[i] - a[i-1]))
    ans = gcdList[0]
    for i in range(1, len(gcdList)):
        ans = gcd(ans, gcdList[i])
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
