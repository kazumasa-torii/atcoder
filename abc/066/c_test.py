"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
6
0 6 7 6 7 0

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = deque()
    flag = True
    for i in range(n):
        if flag:
            b.append(a[i])
            flag = False
        else:
            b.appendleft(a[i])
            flag = True
    if n % 2 != 0:b.reverse()
    print(*b)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
