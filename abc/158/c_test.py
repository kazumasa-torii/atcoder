"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
8 10
"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b = map(int, input().split())
    for i in range(10000):
        if (i*8)//100 == a and (i*10)//100 == b:exit(print(i))
    print(-1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
