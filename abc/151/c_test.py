"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
2 5
1 WA
1 AC
2 WA
2 AC
2 WA

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, m = map(int, input().split())
    ac = [False] * n
    wa = [0] * n
    for i in range(m):
        x, y = input().split()
        x = int(x) - 1
        if ac[x]: continue
        if y == 'AC': ac[x] = True
        else:wa[x] += 1
    ans = 0
    for i, j in zip(ac, wa):
        ans += i*j
    print(sum(ac), ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
