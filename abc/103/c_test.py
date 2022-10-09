"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5
7 46 11 20 11

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from math import gcd
def main():
    def lcm(a, b):
        return a * b // gcd (a, b)
    n = int(input())
    a = list(map(int, input().split()))
    tmp = lcm(a[0], a[1])
    for i in range(2, n):
        tmp = lcm(tmp, a[i])
    ans = 0
    tmp -= 1
    for i in a:
        ans = ans + (tmp%i)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
