"""

"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
1 0 1
2 1 2
1 0 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a = [list(map(int, input().split())) for i in range(3)]
    x = [0] * 3
    y = [0] * 3
    for i in range(3): y[i] = a[0][i] - x[0]
    for i in range(3): x[i] = a[i][0] - y[0]
    good = True
    for i in range(3):
        for j in range(3):
            if x[i] + y[j] != a[i][j]: good = False
    print('Yes' if good else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
