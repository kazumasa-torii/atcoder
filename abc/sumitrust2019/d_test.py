"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
4
0224

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    s = list(input())
    cnt = 0
    for i in range(1000):
        num = str(i).zfill(3)
        process = 0
        for j in range(n):
            if process <= 2 and num[process] == s[j]: process += 1
        if process == 3: cnt += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
