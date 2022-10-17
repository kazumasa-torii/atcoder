"""
p パー
r グー
s ちょき
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
5 2
8 7 6
rsrpr

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = list(input())
    score = {"r":  p, "s": r, "p": s}
    tot = 0

    for i in range(k):
        tot += score[t[i]]
    
    for i in range(k, n):
        if t[i-k] == t[i]:
            t[i] = ""
            continue
        tot += score[t[i]]
    print(tot)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
