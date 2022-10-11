"""
2nのニム和に帰着することができるらしいけどよくわからん
"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
2 8 4
6 4
7 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, h, w = map(int, input().split())
    nim_h = 0
    nim_w = 0
    for _ in range(n):
        a, b = map(int, input().split())
        nim_h = nim_h ^ (a-1)
        nim_w = nim_w ^ (b-1)
    print('First' if nim_h ^ nim_w != 0 else 'Second')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
