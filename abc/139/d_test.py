"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
13

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    print((n*(n-1))//2)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
