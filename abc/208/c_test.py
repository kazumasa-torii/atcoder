"""

"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
7 1000000000000
99 8 2 4 43 5 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
from copy import deepcopy
def main():
    n, k = map(int, input().split())
    hand = k // n
    amari = k % n
    a = list(map(int, input().split()))
    b = deepcopy(a)
    b.sort()
    num = defaultdict(int)
    for i in b:
        num[i] = hand
    while amari > 0:
        for _, i in enumerate(num):
            if amari == 0:
                break
            num[i] += 1
            amari -= 1
    for i in range(n):
        print(num[a[i]])
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
