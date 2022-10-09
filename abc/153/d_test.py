"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
100

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    h = int(input())
    cnt = 0
    while h != 1:
        h //= 2
        cnt += 1
    ans = 1
    while cnt != 0:
        ans += 2 ** cnt
        cnt -= 1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
