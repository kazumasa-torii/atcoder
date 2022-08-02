"""
累積和を使った解法
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
10
1 1 1 1 1 1 1 1 1 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N = int(input())
    A = list(map(int, input().split()))

    accum = [0]
    for a in A:
        accum.append(accum[-1]+a)

    length = accum[-1]
    if length % 10 != 0:
        print("No")
        exit()

    accum = set(accum)

    for x in accum:
        if (x + length // 10) % length in accum:
            print("Yes")
            exit()
    print("No")
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
