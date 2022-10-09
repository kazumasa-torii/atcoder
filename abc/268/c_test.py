"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
4
1 2 0 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0]*n
    for i in range(n):
        for j in range(3):
            print(a[i]-1-i+j+n, (a[i]-1-i+j+n)%n)
            cnt[(a[i]-1-i+j+n)%n] += 1
    print(cnt)
    ans = 0
    for i in range(n):
        ans = max(ans, cnt[i])
    print(ans) 
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
