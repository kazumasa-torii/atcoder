"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
12345 678901

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    ans = 0
    if n*2 <= m:
            ans += n
            m -= n*2
            ans += m // 4
    else: ans = m//2
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
