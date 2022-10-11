"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
3
cbaa
daacc
acacac

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = [[0] * n for _ in range(26)]
    for i in range(n):
        for j in list(input()):
            a[ord(j) - 97][i] += 1
    
    ans = str()
    for i in range(26):
        ans += min(a[i]) * chr(i+97)
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
