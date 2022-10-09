"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
10
2184 2126 1721 1800 1024 2528 3360 1945 1280 1776

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    cnt = 0
    n = int(input())
    for i in map(int, input().split()):
        while i%2==0:
            i = i/2
            cnt = cnt + 1
    print(cnt)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
