"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
4 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    mod = 2019
    l, r = map(int, input().split())
    ans = int(1e19)
    if r > l+mod: exit(print((0)))
    l %= mod
    r %= mod
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            ans = min(ans, (i*j)%mod)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
