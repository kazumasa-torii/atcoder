"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
6
0 153 10 10 23

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    b = list(map(int, input().split()))
    ans = []
    ans.append(b[0])
    for i in range(1, n-1):
        ans.append(min(b[i], b[i-1]))
    ans.append(b[-1])
    print(sum(ans))
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
