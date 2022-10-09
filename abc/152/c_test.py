"""
, セグ木
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
4
4 3 2 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    num_min = int(1e19)
    for i in a:
        num_min = min(num_min, i)
        if i == num_min: ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')

