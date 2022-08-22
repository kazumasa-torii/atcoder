import sys
import time
from io import StringIO

_INPUT = """\
1 3
"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    a, b = map(int, input().split())
    mcnt = 0
    if a < 0 and b > 0:exit(print('Zero'))
    for i in range(a, b + 1):
        if i < 0: mcnt += 1
    print('Positive' if mcnt % 2 == 0 else 'Negative')
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
