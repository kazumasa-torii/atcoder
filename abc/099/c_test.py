
"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
11 3
7 3 1 8 4 6 2 5 6 3 4

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def judge(n, i):
        i -= 1
        cnt = 1
        while n > 0:
            n -= i
            cnt += 1
        return cnt
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == k: exit(print(1))
    print(judge(n-k, k))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
