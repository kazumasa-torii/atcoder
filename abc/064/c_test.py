"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5
1100 1900 2800 3200 3200

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [False] * 8
    ex = 0
    for i in a:
        if 1 <= i <= 399:ans[0] = True
        elif 400 <= i <= 799: ans[1] = True
        elif 800 <= i <= 1199: ans[2] = True
        elif 1200 <= i <= 1599: ans[3] = True
        elif 1600 <= i <= 1999: ans[4] = True
        elif 2000 <= i <= 2399: ans[5] = True
        elif 2400 <= i <= 2799: ans[6] = True
        elif 2800 <= i <= 3199: ans[7] = True
        elif 3200 <= i: ex += 1
    print(max(1, sum(ans)), sum(ans) + ex)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
