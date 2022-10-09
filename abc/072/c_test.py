"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
7
3 1 4 1 5 9 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    ans = [0] * int(10e5)
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        ans[i-1] += 1
        ans[i] += 1
        ans[i+1] += 1
    print(max(ans))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
