"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
6 2 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, a, b = map(int, input().split())
    victory = [False] * (n+1)
    for i in range(n+1):
        if i >= a and victory[i-a] == False: victory[i] = True
        elif i >= b and victory[i-b] == False: victory[i] = True
    print('First' if victory[n] else 'Second')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
