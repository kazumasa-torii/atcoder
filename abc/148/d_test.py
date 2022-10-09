"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
10
3 1 4 1 5 9 2 6 5 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    idx = 0
    cnt = 0
    ans = [0]
    if 1 not in a:exit(print(-1))
    while idx != n:
        if ans[-1] + 1 == a[idx]:
            ans.append(ans[-1]+1)
            idx += 1
            continue
        cnt += 1
        idx += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
