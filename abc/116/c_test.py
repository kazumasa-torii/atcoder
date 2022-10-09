"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
8
4 23 75 0 23 96 50 100

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i-1] > a[i]:ans += a[i-1] - a[i]
    ans += a[-1]
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
