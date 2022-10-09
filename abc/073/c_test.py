"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
3
6
2
6

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    n=int(input())
    s=set()
    for _ in range(n):
        tmp = int(input())
        print(s)
        s^={tmp}
        print(s)
    print(len(s))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
