"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
1500 2000 500 90000 100000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, c, x, y = map(int, input().split())
    ac = min(c*2, a+b)
    ans = 0
    while x > 0 and y > 0:
        ans += ac
        x -= 1
        y -= 1
    if x > 0:ans += min(ac, a) * x
    else:ans += min(ac, b) * y
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
