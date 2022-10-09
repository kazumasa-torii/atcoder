"""

"""
from re import I
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5 3
1 2 2 4 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def exNum(x):
        return (((x + 1) * x) // 2) / x
    n, k = map(int, input().split())
    a = list(map(lambda x: exNum(int(x)), input().split()))
    ans = 0
    acc = [0]
    for i in a:
        acc.append(acc[-1]+i)
    for i in range(n+1):
        l = i
        r = i+k
        if r > n:break
        ans = max(ans, acc[r] - acc[l])
    print(ans)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
