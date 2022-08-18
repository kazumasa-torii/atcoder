import sys
import time
from io import StringIO

_INPUT = """\
1 21
"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from math import sqrt
def main():
    a, b = input().split()
    ans = sqrt(int(a + b))
    print('Yes' if ans.is_integer() else 'No')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
