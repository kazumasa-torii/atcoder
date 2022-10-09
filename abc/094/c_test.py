"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
6
5 5 4 4 3 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    for i in range(n):
        if a[i] < b[n//2]:print(b[n//2])
        else: print(b[n//2-1])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
