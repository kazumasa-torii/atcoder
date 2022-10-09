"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
7
300 400 500 600 750 320 400

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = (a[0] + a[1])/2
    for i in range(2, n):
        ans += a[i]
        ans /= 2
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
