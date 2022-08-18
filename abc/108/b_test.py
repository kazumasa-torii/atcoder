import sys
import time
from io import StringIO

_INPUT = """\
2 3 6 6
"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b, c, d = map(int, input().split())
    x, y = c - a, d - b
    print(c-y, d + x, a - y, b + x)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
