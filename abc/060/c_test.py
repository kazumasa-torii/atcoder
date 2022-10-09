"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
1 1
0

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, t = map(int, input().split())
    li = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        tmp = abs(li[i] - li[i-1])
        ans += t if tmp > t else tmp
    ans += t
    print(ans) 
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
