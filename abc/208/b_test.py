import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
10000000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    p = int(input())
    li = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    idx = 10
    ans = 0
    while p > 0:
        if p - li[idx] >= 0:
            p -= li[idx]
            ans += 1
        else:
            idx -= 1
        if p == 0:
            break
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
