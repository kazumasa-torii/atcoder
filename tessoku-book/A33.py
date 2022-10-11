"""

"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
6
7 7 7 7 6 6

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    check = a[0]
    for i in range(1, n):
        check = check ^ a[i]
    print('First' if check != 0 else 'Second')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
