"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
9
1 2 4 9 5 8 7 3 6

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if a[i] == i+1:
            s += 1
            if i == n-1:
                a[i-1], a[i] = a[i], a[i-1]
            else:
                a[i+1], a[i] = a[i], a[i+1]
    print(s)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
