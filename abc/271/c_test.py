"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
6
1 2 4 6 7 271

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))

    setA = set(a)
    remain = n

    ans = 0
    for i in range(1, n + 1):
        if i in setA:
            remain -= 1
        else:
            remain -= 2
        
        if remain < 0:
            break
        
        ans = i

    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
