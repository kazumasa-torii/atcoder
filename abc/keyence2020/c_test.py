"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5 3 100

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, k, s = map(int,input().split())
    ans = []
    for _ in range(k):
        ans.append(s)
    for _ in range(n-k):
        if 1 == s:
            ans.append(s+1)
        else:
            ans.append(s-1)
    print(*ans) 
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
