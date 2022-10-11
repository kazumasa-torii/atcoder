"""

"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
8 2
2 3

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    victory = [False] * (n+1)
    for i in range(n+1):
        for j in a:
            if i >= j and not victory[i-j]:
                victory[i] = True
                break
    print('First' if victory[n] else 'Second')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
