"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
11

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    x = int(input())
    total = 0
    i = 1
    while True:
        total += i
        if total >= x:break
        i += 1
    print(i)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')